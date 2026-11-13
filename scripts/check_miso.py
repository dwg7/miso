#!/usr/bin/env python3
"""A light checker for miso instances (CONCEPT.md section 5.3, FORMAT.md; provisional).

Standard library only. Errors are the core invariants; warnings are the
checks that should start soft.

Usage:

    python3 scripts/check_miso.py examples/*.md
    python3 scripts/check_miso.py --instance a.md b.md   # the files are ONE instance

Without --instance, every file is its own instance (virtual paths need to be
unique only within a file). With --instance, uniqueness and references are
checked across all the given files (CONCEPT.md section 4).

Cross-instance references are written `tree:/path` (FORMAT.md). A `tree` is
the file name without ".md". If that file is among the arguments, the path
is checked; otherwise the reference is not checked.
"""

import os
import re
import sys

OFFICE_MAGIC = (b'PK\x03\x04', b'\xd0\xcf\x11\xe0')
HEADING = re.compile(r'^# (.*)$')
FENCE = re.compile(r'^ {0,3}(`{3,}|~{3,})(.*)$')
# Virtual path: first segment lowercase kebab, later segments [A-Za-z0-9._-]
PATH_RE = re.compile(r'^/[a-z][a-z0-9\-]*(?:/[A-Za-z0-9._\-]+)*$')
REF = re.compile(r'(?<![\w/:.\-])/[a-z][a-z0-9\-]*(?:/[A-Za-z0-9._\-]+)+')
XREF = re.compile(r'(?<![\w\-])([a-z][a-z0-9\-]*):(/[a-z][a-z0-9\-]*(?:/[A-Za-z0-9._\-]+)+)')
MAX_PATH = 200

# Instruction-like phrases in the material (precedent: hfu/universe check_universe.py)
INSTRUCTION = [
    r'以前の指示を無視', r'これまでの指示を無視',
    r'ignore (all )?(the )?(previous|prior) instructions',
    r'システムプロンプトを(出力|表示|開示)', r'reveal (the |your )?system prompt',
    r'\b(curl|wget)\b[^\n]*\|\s*(ba)?sh',
]
# Sensitive forms (warnings only; check by eye)
SENSITIVE = [
    (r'AKIA[0-9A-Z]{16}', 'AWS-style access key id'),
    (r'-----BEGIN [A-Z ]*PRIVATE KEY-----', 'private key block'),
    (r'(?i)\b(api[_-]?key|secret|token|password|passwd)\s*[:=]\s*[\'"]?[A-Za-z0-9/+_\-]{12,}', 'credential-like assignment'),
    (r'(?<![\w.+\-])[\w.+\-]+@(?!users\.noreply\.github\.com)[\w\-]+(?:\.[\w\-]+)+', 'email address'),
    (r'\b[a-z0-9\-]+(?:\.[a-z0-9\-]+)*\.(?:internal|corp|intra|lan)\b', 'internal-looking host name'),
]


def scan(lines):
    """Yield (line_no, line, in_fence). Fence markers count as in_fence.

    A fence opens with 3+ backticks or tildes and closes with the same
    character, at least as many, and no info string (CommonMark).
    """
    fence = None  # (char, length)
    for n, ln in enumerate(lines, 1):
        m = FENCE.match(ln)
        if m:
            marker, rest = m.groups()
            if fence is None:
                if marker[0] == '`' and '`' in rest:
                    pass  # inline code that starts a line, not a fence
                else:
                    fence = (marker[0], len(marker))
                    yield n, ln, True
                    continue
            elif marker[0] == fence[0] and len(marker) >= fence[1] and not rest.strip():
                fence = None
                yield n, ln, True
                continue
        yield n, ln, fence is not None


def parse(path):
    """Return (errors, warnings, info) where info has text, objects, etc."""
    errors, warnings = [], []
    try:
        raw = open(path, 'rb').read()
    except OSError as e:
        return ['cannot read: %s' % e], warnings, None
    if not path.endswith('.md'):
        errors.append('file extension is not .md')
    if not raw.strip():
        errors.append('file is empty')
    if raw.startswith(OFFICE_MAGIC):
        errors.append('looks like a binary Office file')
    try:
        text = raw.decode('utf-8')
    except UnicodeDecodeError as e:
        errors.append('not valid UTF-8: %s' % e)
        return errors, warnings, None
    if '\x00' in text:
        errors.append('contains NUL bytes')

    lines = text.split('\n')
    objects = []  # [path or None, start_line, body_lines]
    cur = None
    plain = []  # (n, line) outside fences
    for n, ln, in_fence in scan(lines):
        m = None if in_fence else HEADING.match(ln)
        if not in_fence:
            plain.append((n, ln))
        if m:
            title = m.group(1).strip()
            if not title.startswith('/'):
                errors.append('line %d: first-level heading is not a virtual path: %r' % (n, title[:60]))
                title = None
            elif not PATH_RE.match(title) or len(title) > MAX_PATH:
                warnings.append('line %d: virtual path breaks the grammar in FORMAT.md: %r' % (n, title[:60]))
            cur = [title, n, []]
            objects.append(cur)
        elif cur is not None:
            cur[2].append(ln)
    return errors, warnings, {'text': text, 'lines': lines, 'objects': objects, 'plain': plain}


def check_objects(info, warnings):
    objects, text = info['objects'], info['text']
    sys_rec = [o for o in objects if o[0] and o[0].startswith('/system-record/')]
    if not sys_rec:
        warnings.append('no /system-record/ object (scope, out-of-scope, observer position are declared there)')
    else:
        sys_text = '\n'.join('\n'.join(o[2]) for o in sys_rec)
        if '範囲外' not in sys_text and 'out-of-scope' not in sys_text:
            warnings.append('/system-record/ does not declare the out-of-scope')
        if 'concept-version' not in sys_text:
            warnings.append('/system-record/ has no concept-version declaration')
        if '観察者' not in sys_text and '外部観察' not in sys_text and '現地' not in sys_text and 'observer' not in sys_text:
            warnings.append('/system-record/ does not state the observer position')

    if '<External>' in text:
        warnings.append('placeholder <External>…</External> found (sources need identifier, date, location)')

    for p, start, body in objects:
        if not p:
            continue
        btxt = '\n'.join(body)
        if p.startswith('/sources/'):
            if not re.search(r'取得|確認日|参照|fetched|retrieved|取り込み状況', btxt):
                warnings.append('line %d: %s has no retrieval date or ingest status' % (start, p))
            if re.search(r'^- status:.*partial', btxt, re.M):
                warnings.append('line %d: %s uses "partial" in status (use ingest-status wording)' % (start, p))
        if p.startswith('/acceptance-tests/') and not p.endswith('/') and '/run' not in p:
            if 'query' not in btxt:
                warnings.append('line %d: %s has no query' % (start, p))
            if not re.search(r'result|結果', btxt):
                warnings.append('line %d: %s has no result' % (start, p))
            elif re.search(r'^- result[^:]*:\s*(pass|partial|fail|volatile)', btxt, re.M) and not re.search(r'executor|実行者', btxt):
                warnings.append('line %d: %s has a result but no executor' % (start, p))
        if p.startswith('/traces/') and not re.search(r'status', btxt):
            warnings.append('line %d: %s has no status' % (start, p))
        # `verified` needs a basis (CONCEPT.md 5.1, FORMAT.md): a source, a method or a confirmer.
        if (re.search(r'^- status:.*verified', btxt, re.M) and not p.startswith('/sources/')
                and not re.search(r'source|出典|/sources/|確認者|確認の方法|確認日|取得|引用|原文|reviewed|verified-by', btxt)):
            warnings.append('line %d: %s is `verified` but states no source, method or confirmer' % (start, p))


def check_text(info, warnings):
    text = info['text']
    for pat in INSTRUCTION:
        for m in re.finditer(pat, text, re.I):
            line = text.count('\n', 0, m.start()) + 1
            warnings.append('line %d: instruction-like phrase in the material: %r' % (line, m.group(0)[:40]))
    for pat, label in SENSITIVE:
        for m in re.finditer(pat, text):
            line = text.count('\n', 0, m.start()) + 1
            warnings.append('line %d: possible sensitive value (%s): %r' % (line, label, m.group(0)[:3] + '…'))


def check_refs(info, pathset, trees, warnings):
    """pathset: virtual paths that resolve (this file, or the whole instance).
    trees: {tree name: set of paths} for files given on the command line."""
    def resolves(ref, ps):
        ref = ref.rstrip('.,;:)')
        return ref in ps or any(p.startswith(ref + '/') for p in ps)

    unresolved, xunresolved = {}, {}
    for n, ln in info['plain']:
        if HEADING.match(ln):
            continue
        for ref in REF.findall(ln):
            if not resolves(ref, pathset):
                unresolved.setdefault(ref.rstrip('.,;:)'), n)
        for tree, ref in XREF.findall(ln):
            if tree in trees and not resolves(ref, trees[tree]):
                xunresolved.setdefault('%s:%s' % (tree, ref.rstrip('.,;:)')), n)
    for ref, n in sorted(unresolved.items(), key=lambda kv: kv[1]):
        warnings.append('line %d: reference %s does not resolve to a heading' % (n, ref))
    for ref, n in sorted(xunresolved.items(), key=lambda kv: kv[1]):
        warnings.append('line %d: cross-instance reference %s does not resolve' % (n, ref))


def main(argv):
    instance = False
    if argv and argv[0] == '--instance':
        instance, argv = True, argv[1:]
    parsed = {}
    for path in argv:
        parsed[path] = parse(path)

    # unique virtual paths
    seen_global = {}
    trees = {}
    for path, (errors, warnings, info) in parsed.items():
        if info is None:
            continue
        paths = {o[0] for o in info['objects'] if o[0]}
        trees[os.path.basename(path)[:-3] if path.endswith('.md') else path] = paths
        seen = seen_global if instance else {}
        for p, start, _ in info['objects']:
            if p is None:
                continue
            key = p
            if key in seen:
                where = seen[key]
                errors.append('line %d: duplicate virtual path %s (first at %s)' % (start, p, where))
            else:
                seen[key] = '%s:%d' % (path, start) if instance else 'line %d' % start

    all_paths = set()
    if instance:
        for ps in trees.values():
            all_paths |= ps

    status = 0
    for path, (errors, warnings, info) in parsed.items():
        if info is not None:
            check_objects(info, warnings)
            check_text(info, warnings)
            mine = {o[0] for o in info['objects'] if o[0]}
            check_refs(info, all_paths if instance else mine, trees, warnings)
        print('%s: %d error(s), %d warning(s)' % (path, len(errors), len(warnings)))
        for e in errors:
            print('  ERROR', e)
        for w in warnings:
            print('  WARN ', w)
        if errors:
            status = 1
    return status


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
