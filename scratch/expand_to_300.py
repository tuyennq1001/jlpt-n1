# -*- coding: utf-8 -*-
import os
import sys

# Đảm bảo import được generate_goi
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from generate_goi import words_data

# Danh sách 19 cặp trùng lặp trực tiếp cần loại bỏ dạng động từ
redundant_words = {
    "ぐずぐずする", "うとうとする", "もじもじする", "すーすーする", "つるつるする",
    "がたがたする", "ごつごつする", "ねばねばする", "べたべたする", "さっさとやる",
    "すっきりする", "ひりひりする", "ちくちくする", "ぬるぬるする", "そわそわする",
    "さっぱりする", "てきぱきやる", "にやにやする", "じわーっとする",
    "からりとする", "カラリとする"
}

# 1. Nhóm 1: Trạng Thái Tinh Thần & Cảm Xúc (Cần bổ sung 14 từ)
g1_new = [
    (
        "しぶしぶ",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Miễn cưỡng / Uể oải làm vì bắt buộc",
        "気が進まないながらも, 仕方なく行動する様子。",
        "Làm việc gì đó một cách miễn cưỡng, không tự nguyện nhưng vẫn phải làm vì nghĩa vụ hoặc bị ép buộc.",
        "彼はしぶしぶ部屋の掃除を始めた。",
        "Anh ta miễn cưỡng bắt đầu dọn dẹp phòng ngủ.",
        "いやいや, 不承不承",
        "喜んで, 進んで"
    ),
    (
        "いやいや",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Miễn cưỡng / Không tình nguyện",
        "嫌がりながらも、仕方なく物事を行う様子。",
        "Thái độ không thích, không muốn làm rõ rệt nhưng vẫn phải thực hiện.",
        "子供はいやいや宿題を片付けた。",
        "Đứa trẻ miễn cưỡng làm cho xong bài tập về nhà.",
        "しぶしぶ, 嫌々ながら",
        "快く, 進んで"
    ),
    (
        "もんもん",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Muộn phiền / Trăn trở khôn nguôi / Khổ tâm",
        "悩み苦しんで、心が晴れない様子。",
        "Trạng thái tâm lý bế tắc, lo lắng, suy nghĩ quẩn quanh không tìm ra lối thoát hoặc lời giải đáp.",
        "どうすべきか一人で悶悶と悩んでいた。",
        "Tôi cứ một mình trăn trở muộn phiền khôn nguôi không biết nên làm thế nào.",
        "くよくよ, 悩み苦しむ",
        "すっきり, 晴れやか"
    ),
    (
        "くよくよ",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Lo nghĩ vớ vẩn / Suy nghĩ tiêu cực / U sầu vì chuyện đã qua",
        "済んだことをいつまでも気にして悩む様子。",
        "Cứ mãi để tâm và buồn bã vì những chuyện nhỏ nhặt đã xảy ra trong quá khứ mà không thể thay đổi.",
        "失敗したことをいつまでもくよくよするな。",
        "Đừng có mãi lo nghĩ buồn bã về chuyện đã thất bại nữa.",
        "くよくよする, 悔やむ",
        "あっさり, 気にしない"
    ),
    (
        "るんるん",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Phơi phới / Hớn hở vui tươi / Tâm trạng bay bổng",
        "気分が軽やかで、楽しそうにしている様子。",
        "Tâm trạng vui vẻ, nhẹ nhàng đến mức muốn ngân nga hát thầm (thường dùng cho các bạn trẻ hoặc khi có tin vui).",
        "彼女はデートの前でルンルン気分だ。",
        "Cô ấy đang ở trong tâm trạng phơi phới hớn hở trước buổi hẹn hò.",
        "うきうき, わくわく",
        "しょんぼり, げんなり"
    ),
    (
        "きょとん",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Ngơ ngác / Nghệt mặt ra (không hiểu chuyện gì)",
        "何が起こったか分からず、ぼんやりしている様子。",
        "Dáng vẻ ngơ ngác, thất thần một lúc khi đột ngột nghe một tin tức bất ngờ hoặc không hiểu lời người khác nói.",
        "注意されて、彼はきょとんとしていた。",
        "Bị nhắc nhở mà cậu ta cứ nghệt mặt ra ngơ ngác không hiểu gì.",
        "ぽかん, 呆然",
        "しゃきっと, はっきり"
    ),
    (
        "ぽかん",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Hốc mồm ngơ ngác / Đờ đẫn / Há hốc mồm",
        "口を開けてぼんやりしている様子。",
        "Trạng thái ngạc nhiên đến mức há hốc mồm ra đờ đẫn, hoặc đầu óc trống rỗng không suy nghĩ gì.",
        "美しい景色にぽかんと口を開けて見とれていた。",
        "Tôi há hốc mồm ngơ ngác ngắm nhìn cảnh sắc tuyệt đẹp.",
        "きょとん, 呆然",
        "しっかり, はっきり"
    ),
    (
        "うはうは",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Cười toe toét (trúng đậm, kiếm bộn tiền)",
        "思いがけない利益を得て、喜びが隠せない様子。",
        "Cảm giác vui sướng tột độ, không giấu được nụ cười hỉ hả khi kiếm được khoản tiền lớn hoặc trúng số bất ngờ.",
        "ボーナスがたくさん出て、今月はウハウハだ。",
        "Thưởng nhiều quá nên tháng này tôi cứ cười toe toét sung sướng.",
        "ほくほく, 悦に入る",
        "げんなり, がっくり"
    ),
    (
        "ぷんすか",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Hầm hầm tức giận / Dỗi (phồng má tức tối)",
        "不機嫌そうに怒っている様子。",
        "Dáng vẻ tức giận giận dỗi, hầm hầm phồng má (thường mang sắc thái hơi đáng yêu của trẻ con hoặc người yêu).",
        "妹は怒ってプンスカしながら部屋に戻った。",
        "Em gái tức giận hầm hầm giận dỗi đi thẳng về phòng.",
        "ぷんぷん, むっと",
        "にこにこ, 穏やか"
    ),
    (
        "むっつり",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Lầm lì / Cau có khó đăm đăm",
        "口数が少なく、愛想がない様子。",
        "Thái độ im lìm, không thèm mở miệng nói chuyện, mặt mày cau có khó gần khiến người khác e ngại.",
        "彼は朝からむっつりした顔で座っている。",
        "Từ sáng tới giờ anh ta cứ ngồi lầm lì cau có khó đăm đăm.",
        "不機嫌, むっつりする",
        "にこやか, 愛想がいい"
    ),
    (
        "のりのり",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Phấn khích tột độ / Hăng hái cuồng nhiệt",
        "気分が最高潮に達し, 進んで行動する様子。",
        "Tâm trạng cực kỳ hăng hái, bắt đúng nhịp vui vẻ và hòa mình vào đám đông một cách phấn khích.",
        "パーティーで彼はノリノリで踊っていた。",
        "Tại bữa tiệc, anh ấy đã phấn khích nhảy múa cực kỳ nhiệt tình.",
        "うきうき, ノリが良い",
        "しらける, 無関心"
    ),
    (
        "てれてれ",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Ngượng ngùng / Bẽn lẽn / Gãi đầu gãi tai",
        "照れて、落ち着かない様子。",
        "Trạng thái ngượng ngùng đỏ mặt khi được khen ngợi hoặc khi đứng trước người mình thích.",
        "褒められて、彼はてれてれと照れていた。",
        "Được khen ngợi, cậu ấy ngượng ngùng gãi đầu bẽn lẽn.",
        "照れる, もじもじ",
        "堂々とする, 平気"
    ),
    (
        "おめおめ",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Trơ trẽn / Muối mặt / Mặt dày chịu nhục",
        "恥ずべき状況にありながら, 平気でいる様子。",
        "Mặt dày chịu đựng sự nhục nhã mà đáng lẽ ra phải cảm thấy vô cùng xấu hổ (thường dùng trong văn chương cổ hoặc phê phán).",
        "ライバルに敗北し、おめおめと戻ってくるわけにはいかない。",
        "Bị thua cuộc trước đối thủ thì tôi không thể muối mặt trơ trẽn quay về được.",
        "恥知らず, 厚かましい",
        "潔い, 潔白な"
    ),
    (
        "つれづれ",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Buồn chán / Vô công rỗi nghề",
        "することもなく、退屈で寂しい様子。",
        "Cảm giác cô đơn rảnh rỗi không có việc gì làm, thời gian trôi qua tẻ nhạt vô vị (từ cổ, nổi tiếng trong tác phẩm Tsurezuregusa).",
        "徒然なるままに日記を書き綴った。",
        "Trong những lúc buồn chán tẻ nhạt, tôi lại viết nguệch ngoạc vào nhật ký.",
        "退屈, 寂しい",
        "にぎやか, 忙しい"
    )
]

# 2. Nhóm 2: Cảm Giác Cơ Thể & Thể Chất (Cần bổ sung 27 từ)
g2_new = [
    (
        "びしょびしょ",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Ướt sũng / Ướt nhẹp / Ướt như chuột lột",
        "水でひどく濡れている様子。",
        "Trạng thái quần áo, cơ thể bị ướt sũng hoàn toàn do dầm mưa hoặc ngã xuống nước.",
        "夕立にあって、服がびしょびしょになった。",
        "Gặp cơn mưa rào ban chiều làm quần áo tôi ướt sũng.",
        "ぐしょぐしょ, ずぶ濡れ",
        "からから, 乾いた"
    ),
    (
        "ぐしょぐしょ",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Ướt nhão nhoét / Ướt nhẹp nhầy nhụa",
        "水気を含んで、ぐずぐずになっている様子。",
        "Nhấn mạnh trạng thái ướt sũng đến mức sũng nước, nhão nhoét (như giày lội bùn, khăn lau sũng nước).",
        "雨の中を歩いたので、靴がぐしょぐしょだ。",
        "Vì đi bộ dưới trời mưa nên đôi giày của tôi ướt nhão nhoét nước.",
        "びしょびしょ, びしょ濡れ",
        "からっと, 乾燥する"
    ),
    (
        "びりびり",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Tê rần (điện giật) / Rách xoành xoạch",
        "電気的・感覚的な刺激を感じる様子。物が破れる音。",
        "Cảm giác tê rần ở đầu ngón tay do điện giật nhẹ; Hoặc âm thanh rách xoành xoạch của giấy, rung động mạnh của loa.",
        "静電気で指先がびりびりとしびれた。",
        "Do tĩnh điện nên đầu ngón tay tôi bị tê rần rần.",
        "じんじん, ちくちく",
        "なめらか"
    ),
    (
        "てらてら",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Bóng nhẫy mỡ / Bóng loáng",
        "脂などで光っている様子。",
        "Lớp bóng loáng, nhẫy dầu mỡ trên bề mặt (như da mặt dầu, hoặc trán hói bóng loáng).",
        "汗と脂で顔がてらてらと光っている。",
        "Khuôn mặt bóng nhẫy vì mồ hôi và dầu.",
        "ぎらぎら, てかてか",
        "かさかさ, さらさら"
    ),
    (
        "すやすや",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Ngủ ngon lành / Ngủ say sưa (cho em bé)",
        "気持ちよさそうに静かに眠っている様子。",
        "Trạng thái ngủ say sưa, êm đềm và thở nhẹ nhàng của trẻ nhỏ hoặc người có giấc ngủ ngon.",
        "赤ちゃんがベッドですやすや眠っている。",
        "Em bé đang ngủ ngon lành trong nôi.",
        "ぐっすり, とろとろ",
        "ぱっちり, 目が冴える"
    ),
    (
        "はあはあ",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Thở phì phò / Thở hổn hển / Thở dốc",
        "息が荒くなって、激しく呼吸する様子。",
        "Tiếng thở dốc hổn hển dồn dập sau khi vận động mạnh hoặc khi bị kiệt sức.",
        "階段を駆け上がって、はあはあと息を切らした。",
        "Chạy vội lên cầu thang khiến tôi thở dốc hổn hển.",
        "ぜーぜー, ふうふう",
        "静かに"
    ),
    (
        "ふうふう",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Phù phù (thổi canh nóng) / Thở hồng hộc",
        "熱いものを冷ますために息を吹きかける様子。苦しそうに呼吸する様子。",
        "Có hai nghĩa: Hành động chu môi thổi phù phù cho nguội thức ăn nóng; Hoặc tiếng thở than mệt mỏi khi đối mặt với công việc quá sức.",
        "スープが熱いので、ふうふうと吹いて冷ました。",
        "Súp nóng quá nên tôi thổi phù phù cho nguội bớt.",
        "はあはあ, ぜーぜー",
        "静かに"
    ),
    (
        "どろどろ",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Nhão nhẹt / Bùn đất dơ bẩn / Tan chảy sền sệt",
        "固形物が溶けて、粘り気のある液体になる様子。泥だらけの様子。",
        "Chất lỏng sệt dính dơ bẩn như bùn lầy, hoặc kẹo nung chảy nhầy nhụa sền sệt.",
        "雨で道路が泥泥になって歩きにくい。",
        "Trời mưa khiến con đường nhão nhẹt bùn đất rất khó đi.",
        "べたべた, ぬるぬる",
        "さらさら, からっと"
    ),
    (
        "べとべと",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Dính nhớp nháp (mồ hôi, keo, dầu mỡ)",
        "粘り気のあるものが付着して、気持ちが悪い様子。",
        "Cảm giác dính nhớp nháp khó chịu trên da do mồ hôi nhễ nhại hoặc khi tay dính nhựa đường, kẹo mạch nha.",
        "汗をかいて、体がべとべとする。",
        "Đổ mồ hôi làm cơ thể tôi dính nhớp nháp rất khó chịu.",
        "べたべた, ぬるぬる",
        "さらさら, さらっと"
    ),
    (
        "とろとろ",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Ninh nhừ sền sệt / Chảy mềm (phô mai) / Lim dim",
        "弱火で煮込まれて柔らかい様子。チーズなどが溶けている様子。眠気で目が閉じる様子。",
        "Đồ ăn được ninh nhừ sền sệt cực mềm (như trứng ốp lết, phô mai chảy); Hoặc mi mắt lim dim do buồn ngủ.",
        "このお肉は口の中でとろとろに溶ける。",
        "Miếng thịt này được ninh mềm sền sệt, tan ngay trong miệng.",
        "とろ火, ふにゃふにゃ",
        "かちかち, ぱさぱさ"
    ),
    (
        "ぐにゃり",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Mềm oặt xuống / Cong vẹo đi / Nhũn ra",
        "弾力がなくなり、形が崩れる様子。",
        "Đồ vật bỗng mất đi độ cứng vốn có và bẻ cong dễ dàng, hoặc cơ thể mệt lử mềm oặt đi.",
        "暑さでプラスチックの定規がぐにゃりと曲がった。",
        "Cây thước nhựa bị uốn cong mềm oặt do sức nóng.",
        "ぐゃぐにゃ, へなへな",
        "かちかち, まっすぐ"
    ),
    (
        "かちかち",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Cứng ngắc / Đông cứng / Cứng như đá",
        "非常に硬くて、弾力がない様子。",
        "Trạng thái đồ vật bị đông đá đông cứng ngắc, hoặc bánh mì cũ để lâu bị khô cứng trơ trơ.",
        "冷凍庫に入れておいた肉がかちかちに凍っている。",
        "Miếng thịt để trong ngăn đá đông cứng ngắc rồi.",
        "こちこち, カチカチ",
        "ふにゃふにゃ, 柔らかい"
    ),
    (
        "こちこち",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Cứng đờ (vì sợ) / Cứng ngắc (vai gáy)",
        "緊張などで体が強張っている様子。肩などが凝っている様子。",
        "Cơ thể căng cứng đờ không thể cử động linh hoạt do quá sợ hãi, lo lắng trước đám đông; Hoặc cơ vai gáy bị bó cứng.",
        "緊張のあまり、面接で体がこちこちになってしまった。",
        "Vì quá căng thẳng nên khi phỏng vấn cơ thể tôi cứ cứng đờ ra.",
        "がちがち, 緊張する",
        "のびのび, ほぐれる"
    ),
    (
        "がちがち",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Răng va vào nhau lập cập / Bó cứng cơ",
        "寒さで歯が鳴る様子。体が非常に硬くなっている様子。",
        "Tiếng răng va vào nhau lập cập cành cạch do lạnh buốt; Hoặc cơ bắp căng thẳng tột độ.",
        "寒さで歯ががちがちと鳴った。",
        "Vì lạnh quá nên răng tôi cứ va vào nhau lập cập.",
        "がたがた, こちこち",
        "ゆるい, 柔らかい"
    ),
    (
        "ぱさぱさ",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Khô xơ xác (tóc) / Khô khốc (bánh mì để lâu)",
        "水分がなくなって、つやがない様子。ぱさつく様子。",
        "Trạng thái thiếu độ ẩm, khô xơ của tóc hư tổn hoặc món ăn khô khốc khó nuốt vì mất hết nước.",
        "このパンは古くてぱさぱさしている。",
        "Ổ bánh mì này cũ rồi nên ăn khô khốc.",
        "かさかさ, ばさばさ",
        "しっとり, 潤う"
    ),
    (
        "ばさばさ",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Khô xơ bù xù (mái tóc) / Phành phạch (tiếng đập cánh)",
        "髪の毛が乾燥してまとまらない様子。鳥が羽ばたく音。",
        "Mái tóc khô xơ không vào nếp, dựng bù xù lộn xộn; Hoặc tiếng đập cánh phành phạch của chim lớn.",
        "髪の毛が痛んでばさばさになっている。",
        "Mái tóc bị xơ tổn nên trông cứ bù xù xơ xác.",
        "ぱさぱさ, ボサボサ",
        "しっとり, さらさら"
    ),
    (
        "かりかり",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Giòn rụm (khoai tây chiên, ba chỉ chiên)",
        "硬い物をかむ時の音。軽く引っかく音。",
        "Độ giòn tan của các món ăn khô cứng mỏng nhẹ (như bim bim, thịt ba rọi rán giòn); Hoặc âm thanh cào kèn kẹt nhẹ.",
        "かりかりのポテトチップスを食べる。",
        "Tôi ăn những miếng khoai tây chiên giòn rụm.",
        "さくさく, パリパリ",
        "しんなり"
    ),
    (
        "さくさく",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Giòn tan (bánh quy, tempura)",
        "クッキーなどをかむ音。雪や砂を踏みしめる音。",
        "Món bánh có nhiều lớp bột giòn xốp dễ vỡ; Hoặc tiếng bước chân giẫm sột soạt trên nền tuyết xốp.",
        "このクッキーはさくさくしていて美味しい。",
        "Món bánh quy này giòn tan ăn ngon ghê.",
        "かりかり, パリパリ",
        "湿気る"
    ),
    (
        "しゃりしゃり",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Sần sật (lê, táo) / Xào xạc (đá bào, tuyết cứng)",
        "梨や氷などをかみ砕く時の音。",
        "Âm thanh giòn ngọt, sần sật của các loại hoa quả nhiều nước như lê, táo, dưa hấu hoặc tiếng đá bào tan trong miệng.",
        "冷たいかき氷をしゃりしゃりと食べる。",
        "Ăn món đá bào mát lạnh sột soạt vui tai.",
        "サクサク",
        "ぐねぐね"
    ),
    (
        "こりこり",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Giòn sần sật (sụn tai heo, sứa, ốc)",
        "貝や軟骨などの歯ごたえがある様子。",
        "Cảm giác nhai các món có độ dai giòn, sần sật cứng nhẹ ở răng (như sụn heo, sứa, hải sâm).",
        "軟骨のこりこりとした食感が好きだ。",
        "Tôi thích cái cảm giác nhai sụn heo giòn sần sật.",
        "こりこりする",
        "柔らかい"
    ),
    (
        "ぷりぷり",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Giòn đanh căng mọng (tôm tươi) / Dỗi hờn",
        "海老などが弾力がある様子。また、怒っている様子。",
        "Độ dai giòn, săn chắc bập bùng của hải sản tươi (tôm, mực); Hoặc mông bé căng tròn; Hoặc sắc thái nổi giận giận dỗi.",
        "ぷりぷりとした新鮮なエビをユーでる。",
        "Luộc những con tôm tươi roi rói giòn sần sật.",
        "もちもち, ぷんぷん",
        "へなへな, のろのろ"
    ),
    (
        "もちもち",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Dẻo quánh / Bánh giầy dẻo mịn / Da dẻ căng bóng",
        "餅のように粘り気と弾力がある様子。",
        "Cảm giác dai dẻo đàn hồi cực tốt của bánh mì nướng ngon, bánh mochi, hay làn da mịn màng khỏe mạnh của em bé.",
        "もちもちとした食感のうどんが特徴だ。",
        "Đặc trưng của món mì udon này là sợi mì dẻo dai đàn hồi.",
        "ふっくら, ぷniぷに",
        "かちかち, ぱさぱさ"
    ),
    (
        "ぷにぷに",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Mềm dẻo đàn hồi / Bồng bềnh mềm mại",
        "柔らかくて弾力があり、触ると気持ちが良い様子。",
        "Cảm giác sờ vào những vật mềm mại, dẻo và nảy nhẹ (như má em bé, đệm chân mèo cưng, thạch jelly).",
        "猫の肉球はぷにぷにしていて可愛い。",
        "Cái đệm chân của chú mèo mềm dẻo sờ thích tay dễ thương ghê.",
        "もちもち, ぷにぷにする",
        "かちかち"
    ),
    (
        "ふわふわ",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Bồng bềnh / Mềm mại như bông / Xốp nhẹ",
        "柔らかく膨らんで、空気を含んでいる様子。",
        "Cảm giác bồng bềnh, siêu nhẹ và êm ái (như mây, bông gòn, bánh bông lan xốp, lông cừu).",
        "焼きたてのパンがふわふわしている。",
        "Mẻ bánh mì mới ra lò mềm xốp bồng bềnh.",
        "ふんわり, ふっくら",
        "かちかち, ずっしり"
    ),
    (
        "ほくほく",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Bở tơi nóng hổi (khoai lang nướng) / Hớn hở",
        "温かくてホクホクした食べ物の様子。嬉しくてたまらない様子。",
        "Trạng thái khoai lang nướng bở tơi, ấm áp và bốc hơi nghi ngút khi cắn; Hoặc nét mặt hỉ hả vì vừa gặp may mắn lớn.",
        "焼きたての焼き芋はほくほくしていて美味しい。",
        "Khoai lang nướng nóng hổi bở tơi ăn ngon tuyệt cú mèo.",
        "ほかほか, うはうは",
        "冷たい, がっくり"
    ),
    (
        "あつあつ",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Nóng hôi hổi (đồ ăn mới nấu) / Nồng nàn thắm thiết",
        "料理がとても熱い様子。また、熱愛中の様子。",
        "Đồ ăn bốc khói nghi ngút nóng hổi vừa ra lò; Hoặc quan hệ tình cảm của các cặp đôi đang nồng nàn thắm thiết đến phát ghen.",
        "あつあつの鍋料理をみんなで囲む。",
        "Mọi người cùng quây luận bên nồi lẩu nóng hôi hổi.",
        "ほかほか, アツアツ",
        "ひえひえ, 冷めきった"
    ),
    (
        "ひえひえ",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Lạnh buốt / Lạnh ngắt / Chilled mát lạnh",
        "非常に冷たくなっている様子。",
        "Cơ thể bị lạnh buốt do nhiệt độ giảm sâu, hoặc lon bia nước ngọt được ướp lạnh ngắt sảng khoái.",
        "冷蔵庫でひえひえになったビールを飲む。",
        "Uống lon bia đã được ướp lạnh buốt sảng khoái trong tủ lạnh.",
        "ひんやり, 冷たい",
        "あつあつ, ほかほか"
    )
]

# 3. Nhóm 3: Hành Vi & Thái Độ (Cần bổ sung 19 từ)
g3_new = [
    (
        "やんわり",
        "Hành Vi & Thái Độ",
        "Nhẹ nhàng / Khéo léo / Từ chối khéo",
        "相手を刺激しないように、柔らかく対応する様子。",
        "Thái độ hoặc hành vi nhẹ nhàng nhã nhặn để tránh gây xích mích hoặc làm đau lòng người khác (thường dùng khi từ chối, khuyên răn).",
        "彼の誘いをやんわりと断った。",
        "Tôi đã khéo léo nhẹ nhàng từ chối lời mời của anh ấy.",
        "穏やかに, 遠回しに",
        "きっぱり, 強く"
    ),
    (
        "のそのそ",
        "Hành Vi & Thái Độ",
        "Chầm chậm lờ đờ / Lề mề / Dáng đi nặng nề",
        "動作が遅く、のろのろと動く様子。",
        "Diễn tả hành động di chuyển chậm chạp, lờ đờ, lề mề không có chút vội vã nào (như dáng gấu đi, người lười ngủ dậy).",
        "クマが森の中からのそのそと現れた。",
        "Một con gấu chầm chậm lờ đờ xuất hiện từ trong rừng.",
        "のろのろ, とぼとぼ",
        "さっさと, てきぱき"
    ),
    (
        "うかうか",
        "Hành Vi & Thái Độ",
        "Lơ đãng nhởn nhơ / Bất cẩn / Đãng trí",
        "注意を怠って、ぼんやりと時間を過ごす様子。",
        "Trạng thái nhởn nhơ lơ là phòng bị, làm việc bất cẩn thiếu tập trung dẫn đến việc bỏ lỡ cơ hội hoặc bị người khác vượt qua.",
        "うかうかしていると、ライバルに追い抜かれるぞ。",
        "Nếu cứ nhởn nhơ lơ đãng như thế, cậu sẽ bị đối thủ vượt mặt đấy.",
        "うっかり, ぼんやり",
        "しっかり, 注意深く"
    ),
    (
        "もたもた",
        "Hành Vi & Thái Độ",
        "Lóng ngóng lề mề / Chậm chạp / Vướng tay chân",
        "動作が遅くてはかどらない様子。",
        "Sự vụng về lề mề trong thao tác làm tiến độ công việc bị trì trệ chậm chạp (như lóng ngóng mãi không buộc được dây giày).",
        "もたもたしているとバスに遅れるよ。",
        "Cứ lề mề lóng ngóng thế là trễ xe buýt bây giờ.",
        "のろのろ, ぐずぐず",
        "さっさと, てきぱき"
    ),
    (
        "ちゃくちゃくと",
        "Hành Vi & Thái Độ",
        "Một cách vững chắc / Từng bước đều đặn",
        "順調に仕事や予定が進んでいく様子。",
        "Tiến trình công việc diễn ra rất thuận lợi, theo sát kế hoạch ban đầu một cách vững chắc không ngừng nghỉ.",
        "工事は着々と進んでいる。",
        "Công trình đang được tiến hành từng bước vô cùng thuận lợi.",
        "着実に, 着々",
        "もたもた, 遅れる"
    ),
    (
        "ゆうゆうと",
        "Hành Vi & Thái Độ",
        "Ung dung tự tại / Thong thả / Vượt qua dễ dàng",
        "余裕があって、落ち着いている様子。簡単に成し遂げる様子。",
        "Hành vi thong dong ung dung đầy tự tin, không vội vã; Hoặc vượt qua kỳ thi/đạt mục tiêu cực kỳ dễ dàng dư dả thời gian.",
        "鳥が大空をゆうゆうと飛んでいる。",
        "Cánh chim đang ung dung tự tại sải cánh bay lượn trên bầu trời rộng lớn.",
        "悠々と, のんびり",
        "あわたただしく, 焦って"
    ),
    (
        "のうのうと",
        "Hành Vi & Thái Độ",
        "Nhởn nhơ đắc ý / Thảnh thơi nhàn hạ",
        "悩みや心配事がなく、気楽に過ごす様子。",
        "Trạng thái nhởn nhơ thảnh thơi quá mức, trốn tránh trách nhiệm hoặc sống sung sướng bất chấp hoàn cảnh khó khăn xung quanh.",
        "親のお金で毎日能能と暮らしている。",
        "Anh ta cứ nhởn nhơ thảnh thơi tiêu tiền của bố mẹ sống qua ngày.",
        "呑気, のんき",
        "せかせか, 苦労する"
    ),
    (
        "よちよち",
        "Hành Vi & Thái Độ",
        "Chập chững bước đi / Dáng đi lẫm chẫm",
        "幼児などが、足元が不安定に歩く様子。",
        "Dáng đi chưa vững, nghiêng ngả lẫm chẫm đầy đáng yêu của em bé tập đi hoặc chim cánh cụt.",
        "ペンギンがよちよちと歩く姿が可愛い。",
        "Dáng đi chập chững lẫm chẫm của chú chim cánh cụt trông thật dễ thương.",
        "よちよち歩く, よたよた",
        "すたすた"
    ),
    (
        "しゃきしゃき",
        "Hành Vi & Thái Độ",
        "Hoạt bát dứt khoát / Sần sật (rau củ tươi)",
        "動作が元気で引き締まっている様子。野菜などが新鮮で歯ごたえがある様子。",
        "Tác phong nhanh nhẹn, năng nổ dứt khoát làm việc hiệu quả; Hoặc cảm giác nhai sần sật của xà lách, giá đỗ tươi.",
        "彼女はいつもシャキシャキ働いている。",
        "Cô ấy lúc nào cũng làm việc vô cùng hoạt bát dứt khoát.",
        "きびきび, てきぱき",
        "もたもた, だらだら"
    ),
    (
        "しれっと",
        "Hành Vi & Thái Độ",
        "Tỉnh bơ / Thản nhiên / Như không có chuyện gì",
        "素知らぬ顔をして、平気そうにしている様子。",
        "Hành động thản nhiên, tỉnh bơ như không hay biết gì ngay cả sau khi làm việc sai hoặc mắc lỗi nghiêm trọng.",
        "彼は遅刻したのに、しれっとした顔で教室に入ってきた。",
        "Dù đi trễ nhưng cậu ta vẫn bước vào lớp với vẻ mặt thản nhiên tỉnh bơ như không.",
        "けろっと, 素知らぬ顔で",
        "おどおdo, 恐縮する"
    ),
    (
        "しゃあしゃあと",
        "Hành Vi & Thái Độ",
        "Trơ tráo / Mặt dày mày dạn / Nói dối không chớp mắt",
        "恥ずかしいことをしても、平気でいる様子。",
        "Thái độ trơ tráo trơ trơ không chút xấu hổ hay hối lỗi dù vừa bị bắt quả tang làm chuyện sai trái hoặc nói dối.",
        "彼は嘘がバレても、しゃあしゃあと嘘を重ねた。",
        "Dù lời nói dối bị bại lộ, anh ta vẫn trơ tráo tiếp tục bịa đặt thêm.",
        "ぬけぬけと, 厚かましい",
        "恥ずかしがる, 恐縮する"
    ),
    (
        "ぬけぬけと",
        "Hành Vi & Thái Độ",
        "Trâng tráo / Trơ trẽn khôn lỏi / Mặt dày",
        "厚かましく、恥じる様子がない様子。",
        "Tương tự `しゃあしゃあと` nhưng nhấn mạnh vào sự láu cá, trâng tráo thái quá đến mức khó tin trước mặt người bị hại.",
        "よくもぬけぬけとそんなことが言えたものだ。",
        "Sao anh có thể trâng tráo mặt dày nói ra những lời như thế được chứ.",
        "しゃあしゃあと, 厚かましい",
        "遠慮する, 身を縮める"
    ),
    (
        "堂々と",
        "Hành Vi & Thái Độ",
        "Đường đường chính chính / Tự tin uy nghi",
        "自信に満ちて、誇らしげな様子。",
        "Thái độ tự tin đầy kiêu hãnh, quang minh chính đại không lén lút che giấu gì cả.",
        "ステージの上で堂々とスピーチをした。",
        "Cậu ấy đã đứng thuyết trình vô cùng tự tin đường đường chính chính trên sân khấu.",
        "堂々, 堂々とすること",
        "おどおど, こそこそ"
    ),
    (
        "せかせか",
        "Hành Vi & Thái Độ",
        "Lật đật tất bật / Nháo nhào vội vã",
        "動作が忙しく、落ち着きがない様子。",
        "Dáng vẻ tất bật vội vã, đi đứng nói năng liến thoắng nháo nhào do thiếu bình tĩnh hoặc quá bận rộn.",
        "彼はいつもせかせか歩いている。",
        "Anh ta lúc nào cũng bước đi lật đật tất bật vội vã.",
        "そわそわ, 忙しない",
        "のんびり, ゆったり"
    ),
    (
        "まごまご",
        "Hành Vi & Thái Độ",
        "Lúng túng hoang mang / Bối rối loay hoay",
        "どうしていいか分からず、困惑している様子。",
        "Trạng thái bối rối, loay hoay lúng túng khi đứng trước tình huống xa lạ hoặc không tìm thấy đường đi.",
        "機械の使い方を間違えて、まごまごしてしまった。",
        "Không biết dùng máy nên tôi cứ loay hoay lúng ta lúng túng.",
        "おろおろ, うろうろ",
        "てきぱき, スムーズに"
    ),
    (
        "わいわい",
        "Hành Vi & Thái Độ",
        "Ồn ào náo nhiệt / Bàn tán rôm rả",
        "大勢が集まって賑やかに騒ぐ様子。",
        "Không khí ồn ào náo nhiệt, cười nói reo hò rôm rả của một đám đông tụ tập cùng vui chơi.",
        "みんなでわいわい話しながら食事をした。",
        "Mọi người vừa ăn vừa nói chuyện rôm rả náo nhiệt.",
        "がやがや, にぎやか",
        "しんと, 静かに"
    ),
    (
        "がやがや",
        "Hành Vi & Thái Độ",
        "Ồn ào náo loạn / Tiếng xì xào nhốn nháo",
        "多くの人が一斉に騒がしく話す様子。",
        "Tiếng xì xào nhốn nháo hỗn tạp của nhiều người cùng nói chuyện một lúc trong phòng họp hoặc nhà ga khiến không gian hơi lộn xộn.",
        "授業が始まる前、教室内はがやがやしていた。",
        "Trước giờ học, trong phòng học cứ xì xào ồn ào nhốn nháo.",
        "わいわい, 騒がしい",
        "静まり返る, しんと"
    ),
    (
        "にっこり",
        "Hành Vi & Thái Độ",
        "Mỉm cười rạng rỡ / Nở nụ cười tươi",
        "嬉しそうに微笑む様子。",
        "Hành động mỉm cười nhẹ nhàng rạng rỡ đầy thân thiện hướng về người khác.",
        "彼女はカメラに向かってにっこり笑った。",
        "Cô ấy mỉm cười rạng rỡ trước ống kính máy ảnh.",
        "にこにこ, にっこりする",
        "しかめっ面, つんつん"
    ),
    (
        "にやりと",
        "Hành Vi & Thái Độ",
        "Cười toe toét ẩn ý / Cười khẩy nham hiểm",
        "意味ありげに、また満足そうに笑う様子。",
        "Nụ cười thoáng qua đầy ẩn ý, tự mãn hoặc nham hiểm khi nghĩ ra một mưu mẹo gì đó.",
        "彼は何か悪だくみを思いついたのか、にやりと笑った。",
        "Anh ta bỗng cười khẩy một cái đầy ẩn ý, có vẻ vừa nghĩ ra âm mưu gì đó.",
        "にやにや, にやりとする",
        "真面目な顔"
    )
]

# 4. Nhóm 4: Mức Độ & Biến Đổi (Cần bổ sung 14 từ)
g4_new = [
    (
        "ふっくら",
        "Mức Độ & Biến Đổi",
        "Căng tròn phúng phính / Nở phồng xốp mịn",
        "柔らかく膨らんでいる様子。",
        "Sự phồng lên đầy đặn, mềm xốp (như bánh mì mới nướng nở phồng, hoặc đôi má hồng hào phúng phính của em bé).",
        "このパンはふっくらと焼き上がっている。",
        "Bánh mì này được nướng nở phồng xốp mịn trông ngon quá.",
        "ふわふわ, ふんわり",
        "ぺしゃんこ, かたい"
    ),
    (
        "こんもり",
        "Mức Độ & Biến Đổi",
        "Rậm rạp um tùm / Xum xuê đắp cao",
        "草木が群がって茂り, 盛り上がっている様子。",
        "Mô tả đồi cây xanh um tùm đắp cao lên tròn trịa, hoặc đĩa thức ăn được đắp cao đầy đặn.",
        "山の上に緑の森がこんもりと茂っている。",
        "Trên đỉnh núi, cánh rừng xanh um tùm rậm rạp.",
        "もりもり, 茂る",
        "まばら, はげた"
    ),
    (
        "じっくり",
        "Mức Độ & Biến Đổi",
        "Kỹ càng thấu đáo / Từ tốn nghiền ngẫm",
        "落ち着いて時間をかけ、十分に物事を行う様子。",
        "Hành động từ tốn dành nhiều thời gian để suy nghĩ thấu đáo hoặc chuẩn bị một cách cực kỳ cẩn thận không vội vã.",
        "将来設計についてじっくり考えよう。",
        "Hãy cùng từ tốn suy nghĩ thật kỹ càng thấu đáo về kế hoạch tương lai.",
        "じっくりと, つくづく",
        "さっさと, 急いで"
    ),
    (
        "ばっちり",
        "Mức Độ & Biến Đổi",
        "Hoàn hảo chu đáo / Trúng phóc / Tuyệt hảo",
        "準備などが完璧で、結果が良い様子。",
        "Công tác chuẩn bị hoàn hảo 100%, hoặc việc trang điểm ăn mặc cực kỳ chỉn chu bắt mắt.",
        "テストの対策はばっちりだ。",
        "Việc chuẩn bị ôn thi đã hoàn hảo chu đáo lắm rồi.",
        "ぴったり, 完璧に",
        "ぼろぼろ, 不十分"
    ),
    (
        "がっちり",
        "Mức Độ & Biến Đổi",
        "Vạm vỡ săn chắc / Chắc chắn / Khôn ngoan tiết kiệm",
        "骨組みが頑丈な様子。また、金銭に細かい様子。",
        "Cơ thể vạm vỡ cơ bắp săn chắc; Hoặc kết cấu nhà cửa vô cùng kiên cố; Hoặc tính toán tiền bạc cực kỳ chặt chẽ khôn ngoan.",
        "彼はがっちりした体格をしている。",
        "Cậu ấy sở hữu vóc dáng vạm vỡ săn chắc.",
        "しっかり, がっしり",
        "へなへな, ゆるい"
    ),
    (
        "むっちり",
        "Mức Độ & Biến Đổi",
        "Đầy đặn mỡ màng / Tròn trịa đầy sức sống",
        "肉付きがよく、柔らかそうな様子。",
        "Da thịt đầy đặn, tròn trịa mỡ màng một cách khỏe mạnh, quyến rũ (như bắp đùi săn chắc).",
        "赤ちゃんのむっちりした太ももが可愛い。",
        "Cặp đùi đầy đặn phúng phính của em bé trông dễ thương quá.",
        "ふっくら, ぽっちゃり",
        "げっそり, 痩せた"
    ),
    (
        "すんなり",
        "Mức Độ & Biến Đổi",
        "Thon thả thanh mảnh / Trơn tru suôn sẻ",
        "細いてしなやかな様子。物事が滞りなく進む様子。",
        "Cơ thể thon thả thanh mảnh cực đẹp; Hoặc sự việc, cuộc thảo luận diễn ra trơn tru suôn sẻ mà không gặp bất kỳ cản trở nào.",
        "彼女はすんなりとした手足をしている。",
        "Cô ấy sở hữu tay chân thon thả thanh mảnh thật đẹp.",
        "するする, スムーズに",
        "ごつごつ, 難航する"
    ),
    (
        "うっすら",
        "Mức Độ & Biến Đổi",
        "Mờ ảo / Man mác se se / Mỏng nhẹ",
        "色が薄く、かすかに感じられる様子。",
        "Lớp phủ mỏng nhẹ (như sương mù mờ ảo, lớp tuyết mỏng mới rơi, hoặc màu son nhạt nhòa).",
        "山頂には雪がうっすらと積もっている。",
        "Trên đỉnh núi tuyết đã phủ một lớp mỏng nhẹ.",
        "かすかに, 薄く",
        "ぎっしり, 濃く"
    ),
    (
        "まるごと",
        "Mức Độ & Biến Đổi",
        "Toàn bộ / Nguyên vẹn cả quả",
        "全体をそのまま残さず扱う様子。",
        "Ăn hoặc dùng toàn bộ đồ vật mà không cắt nhỏ ra, giữ nguyên trạng ban đầu.",
        "リンゴを丸ごと食べる。",
        "Tôi ăn nguyên cả quả táo.",
        "すべて, まるまる",
        "ばらばら, 部分的に"
    ),
    (
        "そっくり",
        "Mức Độ & Biến Đổi",
        "Giống hệt như đúc / Toàn bộ không sót gì",
        "すべて残らず。また、非常によく似ている様子。",
        "Hai người hoặc hai vật giống hệt nhau như hai giọt nước; Hoặc đưa toàn bộ tiền bạc không bớt lại đồng nào.",
        "彼は父親に顔がそっくりだ。",
        "Gương mặt của anh ta giống hệt như đúc bố mình.",
        "瓜二つ, 全部",
        "全く違う"
    ),
    (
        "ぐんと",
        "Mức Độ & Biến Đổi",
        "Đáng kể / Vượt bậc / Nâng cấp rõ rệt",
        "差が大きく、一段と引き立つ様子。",
        "Sự thay đổi vượt bậc về mức độ, khoảng cách tăng vọt đáng kể (như thành tích học tập tiến bộ vượt bậc).",
        "気温が下がって、ぐんと寒くなった。",
        "Nhiệt độ hạ thấp làm thời tiết lạnh hơn hẳn đáng kể.",
        "ぐっと, 一段と",
        "わずかに"
    ),
    (
        "うんと",
        "Mức Độ & Biến Đổi",
        "Rất nhiều / Cực kỳ / Hết sức mình",
        "数量が非常に多い様子。力を強く込める様子。",
        "Số lượng nhiều vượt trội, hoặc hành động dồn hết sức lực lực lưỡng làm việc gì đó.",
        "休日はうんと楽しみたい。",
        "Tôi muốn tận hưởng ngày nghỉ thật nhiều.",
        "たくさん, がんばって",
        "少し, わずかに"
    ),
    (
        "ごてごて",
        "Mức Độ & Biến Đổi",
        "Trang trí rườm rà / Loè loẹt nhức mắt / Lộn xộn",
        "余計な装飾が多く、すっきりしない様子。",
        "Trang trí quá nhiều chi tiết thừa thãi tạo cảm giác loè loẹt rườm rà nhức mắt.",
        "この部屋は飾りが多くてごてごてしている。",
        "Căn phòng này trang trí nhiều đồ rườm rà lộn xộn quá.",
        "ごちゃごちゃ, 派手な",
        "すっきり, シンプル"
    ),
    (
        "ぼちぼち",
        "Mức Độ & Biến Đổi",
        "Rục rịch bắt đầu / Thong thả từng chút một",
        "少しずつ物事を始める様子。まあまあの状態。",
        "Thong thả bắt đầu rục rịch chuẩn bị hành động, hoặc trạng thái công việc ở mức tàm tạm, bình ổn.",
        "時間が遅いので、ぼちぼち出かけましょう。",
        "Muộn rồi, chúng ta rục rịch thong thả lên đường thôi.",
        "そろそろ, ぼつぼつ",
        "急いで, さっさと"
    )
]

def main():
    # 1. Lọc bỏ các từ trùng lặp trong words_data
    filtered_data = [w for w in words_data if w[0] not in redundant_words]
    print(f"Số lượng sau khi lọc bỏ từ trùng lặp: {len(filtered_data)}")
    
    # 2. Gom nhóm để đếm
    groups = {
        "Trạng Thái Tinh Thần & Cảm Xúc": [],
        "Cảm Giác Cơ Thể & Thể Chất": [],
        "Hành Vi & Thái Độ": [],
        "Mức Độ & Biến Đổi": []
    }
    
    for item in filtered_data:
        g = item[1]
        if g in groups:
            groups[g].append(item)
            
    print("Số lượng hiện tại trong từng nhóm:")
    for name, lst in groups.items():
        print(f"  - {name}: {len(lst)}")
        
    # 3. Trộn thêm từ mới
    groups["Trạng Thái Tinh Thần & Cảm Xúc"].extend(g1_new)
    groups["Cảm Giác Cơ Thể & Thể Chất"].extend(g2_new)
    groups["Hành Vi & Thái Độ"].extend(g3_new)
    groups["Mức Độ & Biến Đổi"].extend(g4_new)
    
    print("\nSố lượng sau khi thêm từ mới:")
    total_count = 0
    final_list = []
    for name, lst in groups.items():
        print(f"  - {name}: {len(lst)}")
        total_count += len(lst)
        final_list.extend(lst)
        
    print(f"Tổng số từ vựng: {total_count}")
    if total_count != 300:
        print("Lỗi: Tổng số từ không khớp 300!")
        return
        
    # 4. Tạo chuỗi words_data mới
    array_lines = []
    for item in final_list:
        # Format tuple đẹp mắt
        t_str = f"""    (
        "{item[0]}",
        "{item[1]}",
        "{item[2]}",
        "{item[3]}",
        "{item[4]}",
        "{item[5]}",
        "{item[6]}",
        "{item[7]}",
        "{item[8]}"
    )"""
        array_lines.append(t_str)
        
    words_data_string = "words_data = [\n" + ",\n".join(array_lines) + "\n]"
    
    # 5. Ghi đè vào generate_goi.py
    script_path = "/Users/tuyennq1001/htdocs/jlpt-n1/scratch/generate_goi.py"
    with open(script_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Tìm đoạn định nghĩa words_data = [ ... ]
    # Tìm index của words_data = [
    start_token = "words_data = ["
    start_idx = content.find(start_token)
    
    # Tìm index của dấu đóng ] ngay sau đó kết thúc words_data
    # Để an toàn, chúng ta tìm dấu đóng ] trước khi sang ILLUSTRATED_WORDS
    end_token = "\n# Các từ vựng đã được tạo hình ảnh AI minh họa thực tế"
    if end_token not in content:
        end_token = "\n# Các từ vựng đã được tạo hình ảnh"
    end_idx = content.find(end_token)
    
    # Tìm dấu đóng ngoặc vuông ] trước end_token
    # Lùi lại từ end_idx để tìm dấu đóng ngoặc vuông ]
    array_end_idx = content.rfind("]", start_idx, end_idx)
    
    if start_idx != -1 and array_end_idx != -1:
        new_content = content[:start_idx] + words_data_string + content[array_end_idx + 1:]
        with open(script_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Đã mở rộng thành công database lên 300 từ vựng sạch, không trùng lặp!")
    else:
        print("Lỗi: Không tìm thấy vị trí chèn trong generate_goi.py")

if __name__ == "__main__":
    main()
