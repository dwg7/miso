#!/usr/bin/env python3
"""A light checker for miso instances (CONCEPT.md section 5.3, provisional).

Standard library only. Errors are the core invariants; warnings are the
checks that should start soft. Usage:

    python3 scripts/check_miso.py examples/*.md
"""

import re
import sys

OFFICE_MAGIC = (b'PK\x03\x04', b'\xd0\xcf\x11\xe0')
HEADING = re.compile(r'^# (.*)$')
REF = re.compile(r'(?<![\w/:.\-])/[a-z][a-z0-9\-]*(?:/[A-Za-z0-9_\-]+)+')


def check(path):
    errors, warnings = [], []
    raw = open(path, 'rb').read()
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
        return errors, warnings

    lines = text.split('\n')
    in_fence = False
    objects = []  # (path, start_line, body_lines)
    cur = None
    for i, ln in enumerate(lines, 1):
        if ln.lstrip().startswith('```'):
            in_fence = not in_fence
        m = None if in_fence else HEADING.match(ln)
        if m:
            title = m.group(1).strip()
            if not title.startswith('/'):
                errors.append('line %d: first-level heading is not a virtual path: %r' % (i, title[:60]))
                title = None
            cur = [title, i, []]
            objects.append(cur)
        elif cur is not None:
            cur[2].append(ln)

    paths = [o[0] for o in objects if o[0]]
    seen = {}
    for o in objects:
        if o[0] is None:
            continue
        if o[0] in seen:
            errors.append('line %d: duplicate virtual path %s (first at line %d)' % (o[1], o[0], seen[o[0]]))
        else:
            seen[o[0]] = o[1]

    pathset = set(paths)

    def resolves(ref):
        ref = ref.rstrip('.,;:)')
        return ref in pathset or any(p.startswith(ref + '/') for p in pathset)

    # warnings
    sys_rec = [o for o in objects if o[0] and o[0].startswith('/system-record/')]
    body_all = '\n'.join(text.split('\n'))
    if not sys_rec:
        warnings.append('no /system-record/ object (scope, out-of-scope, observer position are declared there)')
    else:
        sys_text = '\n'.join('\n'.join(o[2]) for o in sys_rec)
        if '範囲外' not in sys_text:
            warnings.append('/system-record/ does not declare the out-of-scope')
        if 'concept-version' not in sys_text:
            warnings.append('/system-record/ has no concept-version declaration')
        if '観察者' not in sys_text and '外部観察' not in sys_text and '現地' not in sys_text:
            warnings.append('/system-record/ does not state the observer position')

    if '<External>' in text:
        warnings.append('placeholder <External>…</External> found (sources need identifier, date, location)')

    for o in objects:
        p, start, body = o
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

    # internal references (outside code fences)
    unresolved = {}
    in_fence = False
    for i, ln in enumerate(lines, 1):
        if ln.lstrip().startswith('```'):
            in_fence = not in_fence
            continue
        if in_fence or HEADING.match(ln):
            continue
        for ref in REF.findall(ln):
            if not resolves(ref):
                unresolved.setdefault(ref.rstrip('.,;:)'), i)
    for ref, i in sorted(unresolved.items(), key=lambda kv: kv[1]):
        warnings.append('line %d: reference %s does not resolve to a heading' % (i, ref))
    return errors, warnings


def main(argv):
    status = 0
    for path in argv:
        errors, warnings = check(path)
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
