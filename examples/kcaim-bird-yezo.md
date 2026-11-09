# /system-record/instance
- name: kcaim-bird-yezo
- 種別: 例(example)。KCAIM の形式を、**紀行・踏み跡の性質の出典**で試すための小さな試行。孫子のインスタンス(`kcaim-sonshi.md`)と対をなす。
- 作成日: 2026-10-27
- 作成: AI が下書きした。**人による内容確認は未了。**日本語の言い換えと整理は AI の下書きで、`derived` として読むこと。
- 対象(試行の範囲): イザベラ・バード『日本奥地紀行』(*Unbeaten Tracks in Japan*)のうち、**第35信(函館から沙流太=Sarufuto まで、1878年8月)**。取り込んだ本文の範囲は `/sources/gutenberg-2184` を参照。
- 別名: 日本奥地紀行、Unbeaten Tracks in Japan、Isabella L. Bird。
- 境界つきエージェントの責任範囲: この範囲の本文が**述べていること**、およびそこから明示して導ける整理。
- 範囲外(このインスタンスだけでは答えを根拠づけられない): ①現在の北海道の地理・地名・行政・人口。②バードの記述が当時の実態をどこまで正確に反映するかの最終判断。③アイヌ民族に関する現在の理解、権利、文化の評価。④本試行で取り込んでいない章の内容。
- 視点についての注意: 本文は、19世紀の英国人旅行者の一人称の記録である。当時の語(例: "savage"、"Aino")や偏見を含む。**これらは当時の語と視点であり、現在の語や事実ではない。**本インスタンスは、アイヌの習俗を詳述する第36信後半〜第37信を、この試行では取り込まない(→ `/open-questions/ainu-material-handling`)。
- 状態の語(このインスタンスで使う):
  - `stated`: 本文がそう述べている(引用が固定した本文と一致する)。**事実として正しいことを意味しない。**
  - `observed` / `reported` / `viewpoint`: 本文の中で、バードが見たと述べること / 他人から聞いたと述べること / 彼女の判断や感想。
  - `derived`: AI が導いた整理。`recalled`: AI の記憶による(出典未確認)。
  - 結果の語(受け入れテスト): `pass` / `partial` / `fail` / `volatile`。出典の**取り込み状況**は別に、「取り込み済み」「一部取り込み」「未取り込み」と書く(`partial` を取り込み状況に使わない)。
- 機微情報: 含まない。
- concept-version: miso コンセプト(CONCEPT.md)2026-11-07 版に準拠(旧称 KCAIM 期に作成し、新陳代謝の方針により、ファイル名と一部の語は旧称のまま)。
- 観察者の位置: 外部観察。本文は19世紀の英国人旅行者の一人称であり、このインスタンスは、現代の日本語話者の AI と人がそれを読む立場である。現地(北海道)の当事者の立場ではない。
- 単位と責任者: 単位は、第35信の本文(一つの紀行の一部)。内容の責任者(オーナー)は hfu。
- 正本: この `.md` ファイル。

# /sources/gutenberg-2184
- 取り込み状況: 一部取り込み(第35信のみ)
- 名称: Project Gutenberg eBook #2184 *Unbeaten Tracks in Japan*(Isabella L. Bird)
- URL: https://www.gutenberg.org/cache/epub/2184/pg2184.txt
- 取得: 2026-10-27。サイズ 735672 バイト。sha256 = 8b6f02e3e20410afe52a49bcb4fd2c88fc2df41ee619c02afaab42cf2b3ff9c6
- 版の記録(ファイル冒頭より): 公開 2000-05-01、最終更新 2019-09-12、英語。転写の底本は **1911年ジョン・マレー版**(ボランティア David Price による転写、Kate Ruffell による第2校正)。1911年版の表紙には、初版 1905年1月、再版 1907年6月、第2版 1911年10月と書かれている。
- 取り込んだ範囲: 第35信とその続き(固定した本文の、第35信の見出しから第36信の見出しの直前まで)。
- 利用条件: Gutenberg は「アメリカ合衆国ではパブリックドメイン」と表示している。著者の生没年は 1831〜1904 年とされ、日本の基準(没後70年)でも保護期間は過ぎていると考えられる。転写はボランティアによる。**Gutenberg の利用条件(商標の扱いを含む)は、再配布時に確認する。**このインスタンスは短い句の引用にとどめ、全文を転載しない。
- 版の関係: この1911年版と、1880年の原著の関係は不明。→ `/open-questions/edition-relation`
- 日本語訳: 現代の邦訳は訳者の著作物であり、使わない。

# /authorities/precedence
- status: normative(このインスタンス内の取り決め)
- 規則1: 1878年の経路と出来事について、固定した本文を最優先の根拠とする。AI の言い換えは `derived` と明示する。
- 規則2: 本文の記述は `stated` であり、事実の保証ではない。バードの観察(`observed`)、伝聞(`reported`)、判断(`viewpoint`)を区別して書く。
- 規則3: 現在の地名・地理は、国土地理院の地名情報など、現在の権威ある出典に照らして確かめるべきだが、この試行では取り込んでいない。AI の記憶による対応は `recalled` とし、根拠にしない。
- 規則4: 引用は、固定した本文に照らして機械的に確かめてから載せる。(孫子のインスタンスの教訓を引き継ぐ)

# /assets/transport-and-lodging
- status: stated
- 許可証(*shomon*): 本文は、領事の働きかけで総督が *shomon*(公式の書状・証明書)を発給したと述べる。内容は "giving me a right to obtain horses and coolies everywhere at the Government rate of 6 sen a ri"、および "with a prior claim to accommodation at the houses kept up for officials on their circuits"。(第35信)
- 宿泊: "there is a uniform charge at the yadoyas of 30 sen a day, which includes three meals, whether you eat them or not"。(第35信)
- 馬: "They are entirely unshod"。先導役の馬("front horse")が先に立たないと、他の馬は進まない、と述べる。(第35信)
- 道: 函館から森の方向の道について、"the road is only passable for pack-horses, owing to the number of broken bridges"。(第35信)
- 船(森から室蘭の対岸へ): 蒸気船は "it took us six weary hours to steam twenty-five miles"、到着は "it was eight at night before we reached the beautiful and almost land-locked bay of Mororan"。この船は、バードのために "kept waiting for me on the other side for two days" と述べる。(第35信)
- 電信: 幌別から白老の道について "grey telegraph-poles along it"。苫小牧では "the road and telegraph wires turn inland to Satsuporo"。(第35信)
- 運送所: "I think that the Transport Offices in Yezo are in Government hands"。(推測を含む伝聞として書かれている。`viewpoint`)
- 解釈(derived): 1878年の蝦夷の旅は、**官の許可証、官の運送所、官の宿**に強く依存していた、と読める。ただし、1人の旅行者の経験であり、一般化できない。

# /assets/places
- status: stated(綴りと本文中の描写)/ 現在の地名との対応は `recalled`(確度つき。**未確認。国土地理院の地名情報などで確かめる**)
- 本文の綴りと、現在の地名との対応(AI の記憶):
  - Hakodaté → 函館(確度: 高)
  - Nanai → 七飯(確度: 中)
  - Komono-taki(本文の綴り)→ 駒ヶ岳(確度: 中)
  - Ginsainoma → 不明(確度: 低。確かめる)
  - Mori → 森(確度: 高)。"Volcano Bay" → 噴火湾(確度: 高)
  - Mororan → 室蘭(確度: 高)
  - Horobets → 幌別(確度: 中)
  - Shiraôi → 白老(確度: 高)
  - Tomakomai → 苫小牧(確度: 高)。Tarumai → 樽前山(確度: 高)
  - Yubets → 勇払(確度: 中)
  - Sarufuto → 沙流川の河口近くの集落(確度: 低。現在の地名は確かめる)
  - Satsuporo → 札幌(確度: 高)
  - Biratori → 平取(確度: 高)
- 本文がアイヌ語の地名について述べていること(`stated`): "several names compounded with bets or pets, the Aino for a river, such as Horobets, Yubets, Mombets"。(第35信)
- 注: 上の対応は、受け入れテストの `t03` で、検証の対象にする。

# /traces/leg-01-hakodate-to-ginsainoma
- status: stated
- 日付の記載: "GINSAINOMA, YEZO, August 17"(第35信の見出し部)。
- 出来事(バードの記述): 函館から Ginsainoma まで、"ridden the eighteen miles from Hakodaté without Ito or an attendant of any kind"。馬は、"it belongs to the Kaitakushi" と述べる(開拓使の馬)。夕食は米、卵、黒豆。
- 途中の記述: Nanai を "a trim Europeanised village in the midst of fine crops" と述べ、そこで政府が "making acclimatisation and other agricultural experiments" と述べる。
- 注: 日付と曜日の関係に疑問がある。→ `/open-questions/dateline-weekday`

# /traces/leg-02-ginsainoma-to-mori
- status: stated
- 日付の記載: "MORI, VOLCANO BAY, Monday"。
- 出来事: "Saturday was grey and lifeless"、"the ride of seven miles here along a sandy road"(Ginsainoma から森まで)。
- 森についての記述: "Mori is a large, ramshackle village, near the southern point of Volcano Bay"。"Mori has no anchorage, though it has an unfinished pier 345 feet long"。蒸気の渡しが "here" にあり、"a very difficult bridle-track running for nearly 100 miles round the bay"(湾を回る道)があるとも述べる。

# /traces/leg-03-mori-to-mororan
- status: stated
- 日付の記載: "YUBETS. YEZO."(この部分が書かれた場所。**見出しの場所は、書いた時点の場所で、記述している出来事の場所ではない**と読める。→ `/lessons/dateline-is-writing-place`)
- 出来事: 蒸気船("not bigger than a large decked steam launch")で、森から対岸の室蘭へ。"six weary hours to steam twenty-five miles"、到着は "eight at night"。バードは、この船が "the only means of reaching the new capital without taking a most difficult and circuitous route" だと述べる。

# /traces/leg-04-mororan-to-horobets
- status: stated
- 出来事: 室蘭で "the three coolies who had been impressed for the occasion had all absconded"(人力車の曳き手が逃げた)。バードは、その車が "kept by the Government for the conveyance of hospital patients" だと述べる。
- 測量技師: バードは室蘭の坂で "Mr. Akboshi, a pleasant young Japanese surveyor who spoke English" に会った、と述べる。この人物は、室蘭を "the worst place in Yezo" と評した、とも述べる。(`reported`。この人物について、本文はこれ以上述べない)
- 幌別: 混住の村で、"forty-seven Aino and only eighteen Japanese houses"。

# /traces/leg-05-horobets-to-shiraoi
- status: stated
- 出来事: 幌別から白老まで "my journey of sixteen miles"。許可証(*shomon*)を示して、運送所の拒否が解けた、と述べる。曳き手はアイヌの人々で、その区間を休まず進んだ、と述べる。川を渡る場面がある。
- 白老: 日没後に到着。"a village of eleven Japanese houses, with a village of fifty-one Aino houses, near the sea"。宿は新しい宿で、焼いた鮭の食事、油の灯り。

# /traces/leg-06-shiraoi-to-tomakomai
- status: stated
- 出来事: 白老から苫小牧へ。"The road is perfectly level for thirteen miles"、苫小牧に "at noon"。
- 苫小牧の記述: 近くに "the volcano of Tarumai"。バードは、この火山が最近 "blew off its cap" し、灰が "as far as Cape Erimo, fifty miles off" まで届いたと述べる(`reported`)。
- 道: "At this place the road and telegraph wires turn inland to Satsuporo"、馬だけの道は "turns to the north-east, and straggles round the island for about seven hundred miles"。
- 地質の記述: "From Mororan to Sarufuto there are everywhere traces of new and old volcanic action"(`observed`/`viewpoint`)。

# /traces/leg-07-tomakomai-to-yubets
- status: stated
- 出来事: 苫小牧で馬に乗り換え。"After riding eight miles along this breezy belt" で、Yubets に着く。
- Yubets: "four or five Japanese houses, four Aino huts" と、漁期に "from 200 to 300 men" を収容する大きな建物(バードは "barrack" と呼ぶ)を述べる。バードは、この場所に強い印象を受けた、と述べる(`viewpoint`)。

# /traces/leg-08-yubets-to-sarufuto
- status: stated
- 出来事: Yubets から沙流太(Sarufuto)まで "the seventeen miles"。"A mounted policeman started with us from Yubets" と述べる。川を、浅瀬と舟で渡る。
- 沙流太: "a colonisation settlement, mainly of samurai from the province of Sendai"、"this Japanese village of sixty-three houses"。
- 同じ頃の旅行者: 平取から戻った "Mr. Von Siebold and Count Diesbach" が訪ねてきた、と述べる。
- 次の行程の準備: "We have to take not only food for both Ito and myself, but cooking utensils"。

# /decision-support/reading-bird-as-source
- status: derived(AI下書き)
- この出典の読み方:
  1. **一人称・同時代の記録**である。当時の蝦夷の交通、制度、価格、風景を知る手がかりとして価値がある。
  2. 同時に、**1人の外国人旅行者の視点**である。観察(`observed`)、伝聞(`reported`)、判断(`viewpoint`)を、本文の書き方から区別する。
  3. 数字(距離、戸数、価格、時間)は、`stated` として扱い、他の出典で確かめる前に、一般化しない。
  4. 先住民族に関する記述は、当時の語と偏見を含む。現在の理解と、そのまま混ぜない。
- 限界: 上の読み方は AI の案である。専門家による史料批判ではない。

# /lessons/dateline-is-writing-place
- status: derived
- 内容: 手紙の見出し("MORI"、"YUBETS"、"SARUFUTO")は、**書いた場所と時点**を指す。その節が記述する出来事は、それ以前の日々にわたることがある。見出しだけで、出来事の場所と日付を決めない。
- 来歴: `/traces/leg-03-mori-to-mororan`(見出しは Yubets だが、内容は森から室蘭への船)。
- 次に確かめること: 他の章でも同じ傾向があるか。

# /open-questions/edition-relation
- status: open
- 問い: 1911年ジョン・マレー版(初版1905年)は、1880年の原著と同じ内容か、短縮版か。第35信の記述は、原著と同じか。
- 影響: 「バードが1878年に書いたこと」と「1905年以降の版が伝えること」を区別できない。
- 次の行動: 原著(1880年版)の目録や、版の比較を調べる。

# /open-questions/dateline-weekday
- status: open
- 問い: 第35信の見出し "GINSAINOMA, YEZO, August 17" と、本文の "Saturday was grey and lifeless and the ride of seven miles here" の関係。1878年8月17日は土曜日(計算)で、見出しの日付と、"Saturday" に Ginsainoma を出発したという記述が整合しない可能性がある。
- 考えられる理由: 見出しの日付の誤り、書いた日と到着日の差、版による差、AI の計算の誤り(曜日は計算で確認したが、暦の種類は確認していない)。
- 次の行動: 他の版や、他の出典の日付と照合する。

# /open-questions/place-identification
- status: open
- 問い: `/assets/places` の `recalled` の対応を、国土地理院の地名情報などで確かめる。特に Ginsainoma と Sarufuto。
- 次の行動: 地理空間の専門家(あなた)による確認、または公開されている地名情報の取り込み。

# /open-questions/ainu-material-handling
- status: open(人の判断が必要)
- 問い: アイヌの習俗を詳述する章(第36信後半〜第37信、第38信ほか)を、取り込むか、どう取り込むか。
- 論点: ①当時の語と偏見を含む。②先住民族に関する情報で、取り込むなら視点の明記と、現在の理解との区別が要る。③当事者や専門家の関与が望ましい可能性がある。
- 現在の扱い: 取り込まない。

# /acceptance-tests/t01-route
- 提案者: AI(あなたの問いに置き換えてよい)
- query: バードは函館から沙流太(Sarufuto)まで、どの経路で、どの交通手段で移動したか
- expected: 8つの区間と、それぞれの手段(馬、蒸気船、人力車、馬)を、本文の記述として示す。日付は、見出しと曜日の疑問(`dateline-weekday`)を断る。
- requires: /traces/leg-01-hakodate-to-ginsainoma 〜 /traces/leg-08-yubets-to-sarufuto
- result: 未実行

# /acceptance-tests/t02-transport-system
- query: 1878年の蝦夷で、バードは交通と宿泊の制度・費用について何を述べているか
- expected: *shomon* の内容、1里6銭、宿1日30銭(3食込み)、運送所、蒸気船の条件を `stated` として示す。1人の旅行者の経験で、一般化できないと断る。
- requires: /assets/transport-and-lodging
- result: 未実行

# /acceptance-tests/t03-checkable-against-modern-geography
- kind: boundary(当てはめ)
- query: バードの記述のうち、現在の地理と照合できるものは何か。照合に何が必要か
- expected: 地名、距離、戸数、火山などを挙げ、現在の地名との対応は `recalled` で未確認と断る。照合に必要な出典(国土地理院の地名情報など)を示す。現在の事実そのものは範囲外と断る。
- requires: /assets/places, /open-questions/place-identification
- result: 未実行

# /acceptance-tests/t04-bets-pets
- query: バードが述べた「ベツ/ペツ」の付く地名について、何が分かるか
- expected: 本文は、アイヌ語で川を指す語から成る名前の例(Horobets、Yubets、Mombets)を挙げる、と述べる。現在の地名学での確かな語源は、この出典では確かめられず、範囲外と断る。
- requires: /assets/places
- result: 未実行

# /acceptance-tests/t05-population-today
- kind: boundary
- query: 現在の苫小牧市の人口は
- expected: 範囲外で、変わりやすい(volatile)ため、このインスタンスでは答えられないと断る。
- requires: /system-record/instance
- result: 未実行

# /acceptance-tests/t06-how-far-reliable
- kind: boundary(当てはめ)
- query: この記述は、1878年当時の蝦夷の実態を、どこまで反映していると言えるか
- expected: 一人称・同時代の記録としての価値と、1人の外国人の視点であること、観察・伝聞・判断の区別、版の関係の未解決を示す。最終判断は人のものと断る。
- requires: /decision-support/reading-bird-as-source, /open-questions/edition-relation
- result: 未実行

# /acceptance-tests/t07-surveyor
- query: バードが室蘭で会った測量技師について、何が分かるか
- expected: 本文は、"Mr. Akboshi, a pleasant young Japanese surveyor who spoke English" と述べ、この人物が室蘭を悪く評したと述べる(`reported`)。それ以上は、この出典では分からないと断る(出典の限界)。
- requires: /traces/leg-04-mororan-to-horobets
- result: 未実行

# /acceptance-tests/t08-dates-consistent
- query: バードの旅程の日付は、一貫しているか
- expected: 見出しの日付は一部しか記載がなく、曜日との整合に疑問が残ることを示す(`dateline-weekday`)。断定しない。
- requires: /open-questions/dateline-weekday, /lessons/dateline-is-writing-place
- result: 未実行

# /inventory/sources
- 取り込み済み: 第35信(固定した本文の該当範囲)
- 未取り込み: 第32〜34信(函館到着前後)、第36信以降(アイヌの習俗を含む。取り込みは人の判断を待つ)、第39〜42信(噴火湾の周辺と帰路)、第43〜44信
- 現在の地名の出典: 未取り込み(国土地理院の地名情報など)

# /inventory/backlog
- 受け入れテスト: t01〜t08(AI の提案。あなたの問いで置き換えてよい。すべて未実行)
- 自律的に進められる次の行動: (1) 引用を固定した本文に機械照合する(済み。→ 検査スクリプト)、(2) t01〜t08 を盲検で実行する、(3) 第39〜41信(噴火湾、有珠岳、長万部)を取り込み、第35信と同じ形式で踏み跡にする
- 人の判断を要する項目: アイヌ関係の章の扱い(→ `/open-questions/ainu-material-handling`)、現在の地名との対応の確認(→ `/open-questions/place-identification`)、版の関係の確認
- 孫子のインスタンスから引き継いだ教訓: 状態語の衝突を避ける(結果の語と取り込み状況の語を分ける)、実行者を記録する、欠けを「取り込み不足」と「出典の限界」に分ける
