# /system-record/title

KCAIM-Scala(題。旧称 KCAIM 期の作成で、名称は新陳代謝の方針により当面そのまま)

> Scala 3 を通してプログラミングと計算機科学を学ぶための KCAIM。
>
> 本インスタンスの目的は Scala 言語仕様の再録ではない。
> Scala の主要概念、その背景にある思想、
> 学習時につまずきやすい点、
> そして現代的なプログラミング教育についての知見を蓄積する。

---

# /system-record/instance

- name: kcaim-scala
- language: Japanese
- version: 0.3
- status: derived

## mission

Scala を学ぶことを通じて、

- 型
- 値
- データ構造
- 抽象化
- 関数型プログラミング

を理解することを支援する。

## 準拠の補記(2026-11-10、miso 準拠化の際に形式のみ補った。内容は作成者のもの)

- concept-version: miso コンセプト(CONCEPT.md)2026-11-07 版の形式に合わせた。
- 範囲外: Scala 言語仕様の再録(冒頭に明記)。および、このインスタンスに取り込んでいない事項(`/inventory/backlog` の項目)。範囲外・未取り込みの問いには、そう答える。
- 観察者の位置: 外部観察。Scala 処理系の実装者の立場ではなく、学習者を支援する立場で書かれている。
- 単位と責任者: 単位は Scala 3 の学習用の概念群。内容の責任者(オーナー)は作成者(未記載。要確認)。
- 状態の補記: `/traces/` の各オブジェクトは、作成者の記録を AI が整理した `derived` として扱う。受け入れテストの `query` と実行者は、作成時に記録されていない。

---

# /authorities/language-specification

- authority:
  Scala 3 Language Specification

- role:
  言語仕様の最終的権威

- status:
  normative

---

# /authorities/scala-knowledge-sources

## Scala Language Specification

最終的権威。

---

## Scaladoc

APIの一次資料。

実務上は仕様書より参照頻度が高い。

---

## Compiler

最終的にコードの正否を決定する。

---

## IntelliJ IDEA

学習支援環境。

型表示、
補完、
定義ジャンプなどを提供する。

---

# /assets/scala-language

- creator:
  Martin Odersky

- first-release:
  2004

- status:
  verified

- description:

  オブジェクト指向と
  関数型プログラミングを統合する
  静的型付け言語。

---

# /decision-support/what-is-scala

Scalaは

- オブジェクト指向
- 関数型
- 静的型システム
- JVM

を統合した言語である。

---

# /decision-support/why-scala

Scalaを学ぶことで

- 型システム
- 関数型設計
- 不変データ
- 並行処理

を学べる。

---

# /decision-support/who-uses-scala

利用者:

- データエンジニア
- バックエンド開発者
- 金融システム開発者
- 分散システム開発者

代表例:

- Apache Spark
- Akka/Pekko 系

---

# /decision-support/is-scala-an-educational-language

Scala は教育専用言語ではない。

実用言語である。

しかし教育価値は高い。

---

# /decision-support/pascal-vs-scala

Pascal:

- 構造化プログラミング

Scala:

- 型
- 不変性
- 関数型設計

共通点:

- 良いプログラミング習慣を重視

---

# /reference-concepts/language-lineage

Scala理解のための背景概念。

- オブジェクト指向
- 関数型プログラミング
- ML系言語
- Haskell
- Java

---

# /traces/history-001-two-traditions

- status: derived

- observation:

  Scala は

  オブジェクト指向

  と

  関数型プログラミング

  の両方の伝統を持つ。

- lesson:

  Scalaは
  Javaを改良しただけの言語ではない。

---

# /traces/history-002-pattern-matching-lineage

- status: derived

- observation:

  Pattern Matching は

  ML
  OCaml
  Haskell

  などで発展してきた。

- lesson:

  Pattern Matching は

  switch文の拡張ではなく

  関数型言語文化の継承である。

---

# /traces/history-003-option-lineage

- status: derived

- observation:

  Option の考え方は

  関数型言語圏で広く利用されてきた。

- lesson:

  Option は

  null の代用品

  というより

  存在可能性を型に取り込む思想である。

---

# /assets/core-scala-3-curriculum

## stage-1

- value
- expression
- type

## stage-2

- function
- collection

## stage-3

- map
- filter
- Option

## stage-4

- case class
- pattern matching
- trait

## stage-5

- immutability
- Either
- for-comprehension

---

# /traces/spec-reading-001-values

- status: derived

- observation:

  Scalaでは val が中心である。

- interpretation:

  mutable state より

  immutable value を重視している。

---

# /traces/spec-reading-002-expression

- status: derived

- observation:

  if は式である。

- interpretation:

  Scalaは

  処理を書くより

  値を構築する視点を持つ。

---

# /traces/spec-reading-003-transformation

- status: derived

- observation:

  map と filter は分かれている。

- interpretation:

  変換(transform)

  と

  選別(select)

  を区別している。

---

# /traces/spec-reading-004-value-vs-variable

- status: derived

- observation:

  val が標準である。

  var は変更可能状態を導入する。

---

# /traces/spec-reading-005-expression-orientation

- status: derived

- observation:

  if

  block

  match

  は値を返す。

---

# /traces/spec-reading-006-type-inference

- status: derived

- observation:

  Scalaは型推論を持つ。

- interpretation:

  型を書かないことではなく

  型と対話することが目的。

---

# /traces/spec-reading-007-option-as-type

- status: derived

- observation:

  Option は型である。

  Some(value)

  または

  None

  を表現する。

---

# /traces/spec-reading-008-option-vs-null

- status: derived

- observation:

  Option は

  値がない可能性を

  型に含める。

---

# /traces/spec-reading-009-option-and-collection-thinking

- status: derived

- observation:

  Option は

  map

  filter

  flatMap

  を持つ。

- lesson:

  0個または1個の要素を持つ
  コレクションとして理解できる。

---

# /traces/spec-reading-010-option-and-pattern-matching

- status: derived

- observation:

  Option は

  Pattern Matching と自然に結び付く。

---

# /traces/spec-reading-011-pattern-matching-is-not-switch

- status: derived

- observation:

  Pattern Matching は

  switch の高機能版ではない。

- lesson:

  分解(decomposition)の仕組みである。

---

# /traces/spec-reading-012-pattern-matching-as-deconstruction

- status: derived

- observation:

  case Some(x)

  は

  値を取り出している。

---

# /traces/spec-reading-013-option-requires-pattern-matching

- status: derived

- observation:

  Option利用者は

  Some

  と

  None

  の両方を扱う必要がある。

---

# /traces/spec-reading-014-match-is-expression

- status: derived

- observation:

  match は式である。

- lesson:

  分岐も値構築の一部である。

---

# /lessons/value-before-variable

Scalaでは

変数より

値を中心に考える。

---

# /lessons/everything-produces-value

Scalaでは

if

も

match

も

値を返す。

---

# /lessons/type-inference-is-communication

型推論は

型を書かない技術ではない。

型との対話である。

---

# /lessons/absence-is-information

値が存在しないことも

情報である。

---

# /lessons/null-is-hidden-branch

null は

存在しない可能性を隠す。

Option は見えるようにする。

---

# /lessons/make-the-possibility-visible

Scalaは

重要な可能性を

型に表現する。

---

# /lessons/option-as-gateway

Optionは

- 型
- map
- flatMap
- Pattern Matching

への入口である。

---

# /lessons/patterns-describe-shapes

Pattern Matching は

値の形を記述する仕組みである。

---

# /lessons/shape-before-algorithm

Scalaでは

アルゴリズム以前に

データの形を考える。

---

# /lessons/scala-is-about-making-things-explicit

Scalaは

見えなかったものを

見えるようにする言語である。

Option:

存在可能性。

型:

値の性質。

Pattern Matching:

構造。

---

# /lessons/scala-is-structural-thinking

Scalaは

手続きだけではなく

構造を重視する。

---

# /assets/scala-support-system

構成要素:

- Scala Compiler
- Scaladoc
- IntelliJ IDEA
- sbt

---

# /traces/scaladoc-discovery-001

- status: derived

- observation:

  実務では
  Scala仕様より

  Scaladoc

  の参照頻度が高い。

---

# /traces/intellij-discovery-001

- status: derived

- observation:

  IntelliJ は

  型表示
  補完
  定義ジャンプ

  を提供する。

- lesson:

  現代プログラミングは
  IDE支援込みで行われる。

---

# /acceptance-tests/option-purpose

- query: (未記録。作成時に記録されていない)
- executor: 不明(未記録)

- result:
  pass

---

# /acceptance-tests/option-vs-null

- query: (未記録。作成時に記録されていない)
- executor: 不明(未記録)

- result:
  pass

---

# /acceptance-tests/option-map

- query: (未記録。作成時に記録されていない)
- executor: 不明(未記録)

- result:
  pass

---

# /acceptance-tests/option-pattern-match

- query: (未記録。作成時に記録されていない)
- executor: 不明(未記録)

- result:
  pass

---

# /acceptance-tests/option-philosophy

- query: (未記録。作成時に記録されていない)
- executor: 不明(未記録)

- result:
  pass

---

# /acceptance-tests/pattern-matching-purpose

- query: (未記録。作成時に記録されていない)
- executor: 不明(未記録)

- result:
  pass

---

# /acceptance-tests/match-as-expression

- query: (未記録。作成時に記録されていない)
- executor: 不明(未記録)

- result:
  pass

---

# /acceptance-tests/decomposition

- query: (未記録。作成時に記録されていない)
- executor: 不明(未記録)

- result:
  partial

- missing:

  case class の取り扱い

---

# /acceptance-tests/documentation-navigation

- query: (未記録。作成時に記録されていない)
- executor: 不明(未記録)

- result:
  fail

- missing:

  Scaladoc利用知識

---

# /acceptance-tests/ide-literacy

- query: (未記録。作成時に記録されていない)
- executor: 不明(未記録)

- result:
  fail

- missing:

  IntelliJ利用知識

---

# /inventory/backlog

優先度A:

- case class
- Pattern Matching深化
- Collection体系

優先度B:

- Scaladoc利用法
- IntelliJ利用法
- sbt

優先度C:

- Either
- for-comprehension
- 型クラス

---

# /open-questions/specification-ingestion-strategy

Scala仕様を

章単位で取り込むのか

概念単位で取り込むのか。

現在の仮説:

概念単位。

---

# /open-questions/how-much-history

背景思想を

どこまで取り込むべきか。

---

# /open-questions/rubric-design

評価ルーブリックを

どのように設計するべきか。

---

# /sources/current-conversation

取り込み状況: 取り込み済み。

取得: 日付は未記録。

