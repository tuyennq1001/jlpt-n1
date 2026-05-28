# -*- coding: utf-8 -*-
import os

new_words_tuples = """    (
        "めきめき",
        "Mức Độ & Biến Đổi",
        "Tiến bộ rõ rệt / Lớn nhanh như thổi",
        "目立って成長したり、上達したりする様子。",
        "Diễn tả sự tiến bộ vượt bậc, phát triển nhanh chóng thấy rõ (về năng lực, kỹ năng, sức khỏe hoặc sự lớn lên của thực vật).",
        "日本語の勉強を始めてから、彼女はめきめき実力をつけた。",
        "Kể từ khi bắt đầu học tiếng Nhật, cô ấy đã tiến bộ rõ rệt.",
        "ぐんぐん, 急速に",
        "のろのろ, 衰退する"
    ),
    (
        "ちゃっかり",
        "Hành Vi & Thái Độ",
        "Láu cá / Khôn ngoan / Tận dụng cơ hội (trục lợi cho mình)",
        "抜け目なく、自分に都合のよいように行動する様子。",
        "Thái độ khôn lỏi, biết tận dụng cơ hội để thu lợi ích cho bản thân mà không làm hại ai lộ liễu nhưng khiến người khác bất ngờ.",
        "彼はちゃっかり一番いい席を確保していた。",
        "Anh ta đã láu cá xí trước chỗ ngồi tốt nhất rồi.",
        "抜け目ない, 要領よく",
        "お人よし, 不器用"
    ),
    (
        "ばっぱり",
        "Hành Vi & Thái Độ",
        "Đột ngột chạm trán / Đổ sầm / Đột ngột dừng lại",
        "偶然出会う様子。また、急に倒れる様子。",
        "Có hai nghĩa chính: Tình cờ chạm trán người quen trên phố; Hoặc tiếng đổ sầm của đồ vật hay người ngã gục.",
        "駅で偶然友人にばったり会った。",
        "Tôi tình cờ chạm mặt một người bạn cũ ở nhà ga.",
        "ひょっこり, 偶然に",
        "予定通り"
    ),
    (
        "げんなり",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Chán nản / Mệt mỏi / Phát ngấy",
        "すっかり嫌になる様子。また、ひどく疲れる様子。",
        "Trạng thái chán ngán, kiệt sức và mất sạch tinh thần do phải nghe đi nghe lại một câu chuyện hoặc làm việc quá tải.",
        "毎日残業ばかりで、げんなりする。",
        "Ngày nào cũng làm thêm giờ khiến tôi chán nản mệt mỏi.",
        "うんざり, がっかり",
        "すっきり, 張り切る"
    ),
    (
        "うんざり",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Chán ngấy / Phát ngán / Ngán ngẩm",
        "物物が度重なって嫌になる様子。",
        "Cảm giác chán ngấy đến mức không muốn nhìn thấy hay nghe thấy nữa do một sự việc lặp đi lặp lại quá nhiều lần.",
        "彼の長い自慢話には、もううんざりだ。",
        "Tôi phát ngán với những câu chuyện tự cao dài dòng của anh ta rồi.",
        "げんなり, 飽き飽き",
        "すっきり, 満足する"
    ),
    (
        "へろへろ",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Mệt lử / Bủn rủn / Mệt rã rời không còn lực",
        "ひどく疲れて、体に力が入らない様子。",
        "Trạng thái cơ thể mệt mỏi rã rời, chân tay bủn rủn không còn chút lực nào sau khi tập thể thao quá sức.",
        "マラソンの後で、体がへろへろだ。",
        "Sau khi chạy marathon, cơ thể tôi mệt rã rời không còn chút sức lực nào.",
        "くたくた, へとへと",
        "元気いっぱい, シャキッとする"
    ),
    (
        "へなへな",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Yếu ớt / Mềm nhũn / Ngã quỵ",
        "力が入らず、折れ曲がったり倒れたりする様子。",
        "Trạng thái ngã quỵ xuống đất do chân tay mềm nhũn không còn sức lực vì kiệt sức hoặc cú sốc tinh thần.",
        "叱られて、その場にへなへなと座り込んでしまった。",
        "Bị mắng xong, cậu ấy ngã quỵ xuống ngồi bệt ngay tại chỗ.",
        "くたくた, ふにゃふにゃ",
        "しゃきっと, シャンとする"
    ),
    (
        "ふにゃふにゃ",
        "Mức Độ & Biến Đổi",
        "Mềm nhũn / Nhão nhoét / Không có lập trường",
        "柔らかくて弾力がない様子。態度がはっきりしない様子。",
        "Đồ vật mềm không có độ cứng (như đồ nhựa gặp nóng); Hoặc thái độ của con người ba phải, mềm yếu.",
        "このプラスチックは熱でふにゃふにゃになった。",
        "Miếng nhựa này đã bị mềm nhũn ra do sức nóng.",
        "柔らかい, ぐにゃぐにゃ",
        "かたい, シャキッとする"
    ),
    (
        "ぐにゃぐにゃ",
        "Mức Độ & Biến Đổi",
        "Mềm oặt / Cong vẹo / Lằng ngoằng",
        "柔らかくて、簡単に形が変わる様子。",
        "Diễn tả đồ vật quá mềm, dễ dàng bị uốn cong, biến dạng (như thanh sắt bị nung nóng hoặc cơ thể dẻo kẹo).",
        "暑さでキャンディーがぐにゃぐにゃに溶けてしまった。",
        "Do trời nóng nên kẹo mút đã bị chảy ra mềm oặt.",
        "ふにゃふにゃ, 曲がりくねる",
        "まっすぐ, カチカチ"
    ),
    (
        "くねくね",
        "Hành Vi & Thái Độ",
        "Uốn éo / Ngoằn ngoèo / Khúc khuỷu",
        "体や道などが何度も曲がりくねっている様子。",
        "Dáng đi uốn éo cơ thể; Hoặc con đường đèo uốn lượn ngoằn ngoèo.",
        "山道がくねくねと続いている。",
        "Con đường núi cứ kéo dài ngoằn ngoèo khúc khuỷu.",
        "曲がりくねる, うねうね",
        "まっすぐ, 直線的"
    ),
    (
        "ころころ",
        "Hành Vi & Thái Độ",
        "Lăn lông lốc / Thay đổi xoành xoạch",
        "小さな丸い物が転がる様子。また、状況や意見が頻繁に変わる様子。",
        "Có hai nghĩa: Đồ vật tròn nhỏ lăn lông lốc; Hoặc ý kiến, kế hoạch thay đổi liên tục xoành xoạch.",
        "意見をころころ変える人は信用されない。",
        "Người thay đổi ý kiến xoành xoạch thì không được tin tưởng.",
        "変わる, 転がる",
        "一定の, 固定する"
    ),
    (
        "ごろごろ",
        "Hành Vi & Thái Độ",
        "Lăn sầm sập / Nằm ườn ăn không ngồi rồi / Tiếng sấm rền",
        "大きな物が転がる様子。家で怠けて過ごす様子。雷の音。",
        "Nghĩa chính: Nằm ườn ở nhà ăn không ngồi rồi; Tiếng đá tảng lăn; Hoặc tiếng sấm chớp đùng đoàng.",
        "休日はどこにも出かけず、家でごろごろしていた。",
        "Ngày nghỉ tôi chẳng đi đâu cả, chỉ nằm ườn ở nhà.",
        "だらだら, 怠ける",
        "てきぱき, 忙しい"
    ),
    (
        "ゆらゆら",
        "Mức Độ & Biến Đổi",
        "Lao xao / Rung rinh / Chao đảo nhẹ",
        "ゆっくりと揺れ動く様子。",
        "Diễn tả chuyển động đung đưa chậm rãi nhẹ nhàng (như ngọn nến trước gió, rong biển dưới nước).",
        "炎がゆらゆらと揺れている。",
        "Ngọn lửa đang bập bùng rung rinh lao xao.",
        "揺れる, ふらふら",
        "じっとする, 静止する"
    ),
    (
        "ぐらぐら",
        "Mức Độ & Biến Đổi",
        "Rung bần bật / Rung lắc mạnh / Sắp đổ",
        "激しく揺れる様子。また、歯などが不安定な様子。",
        "Sự rung lắc dữ dội do động đất, hoặc răng lung lay sắp rụng.",
        "地震でビルがぐらぐらと揺れた。",
        "Cơn động đất làm tòa nhà rung lắc bần bật.",
        "がたがた, 揺れる",
        "しっかり, 安定する"
    ),
    (
        "がたぴし",
        "Mức Độ & Biến Đổi",
        "Kêu cọc kạch / Rệu rã (cửa, bàn ghế)",
        "建具や家具などが立て付けが悪く、音を立てる様子。",
        "Âm thanh cọc kạch khó chịu của cửa gỗ cũ kỹ, bàn ghế bị rệu rã lỏng khớp.",
        "この古いドアは開閉のたびにがたぴし言う。",
        "Chiếc cửa cũ này cứ mỗi lần đóng mở là lại kêu cọc kạch.",
        "がたがた, きしむ",
        "スムーズな"
    ),
    (
        "がくっと",
        "Mức Độ & Biến Đổi",
        "Giảm đột ngột / Ngã quỵ xuống",
        "急に折れ曲がったり、数量が急激に減ったりする様子。",
        "Sự giảm sút nghiêm trọng về số lượng/doanh số một cách bất ngờ; Hoặc cơ thể ngã quỵ khuỵu gối.",
        "売上が今月に入ってがくっと落ちた。",
        "Doanh thu bắt đầu từ tháng này đã bị giảm sút đột ngột.",
        "がっくり, 急落する",
        "ぐんぐん, 急増する"
    ),
    (
        "ひやっと",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Ớn lạnh (lo sợ đột ngột) / Mát lạnh se se",
        "急に冷たさを感じる様子。また、一瞬恐怖や危機を感じる様子。",
        "Cảm giác giật mình ớn lạnh vì suýt xảy ra tai nạn nguy hiểm, hoặc vị mát lạnh se se.",
        "飛び出してきた車を見て、ひやっとした。",
        "Nhìn thấy chiếc xe đột ngột lao ra, tôi giật mình ớn lạnh cả người.",
        "ひやりとする, どきっと",
        "ほっとする, 安心する"
    ),
    (
        "ひやりと",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Ớn lạnh sống lưng / Rùng mình (lo sợ nguy hiểm)",
        "冷やりとする様子。恐怖で身の毛がよだつ様子。",
        "Tương tự như ひやっと nhưng nhấn mạnh vào cảm giác rùng mình, ớn lạnh chạy dọc sống lưng do lo sợ tai nạn sắp xảy ra.",
        "子供が道路に飛び出し、ひやりとした。",
        "Đứa bé đột ngột lao ra đường khiến tôi ớn lạnh sống lưng.",
        "ひやっとする, はらはらする",
        "安心する"
    ),
    (
        "むかつく",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Cảm thấy bực mình / Nôn nao khó chịu",
        "腹が立つ様子。また、胃が気持ち悪い様子。",
        "Cảm xúc giận dữ, bực tức trước lời nói khó nghe của ai đó; Hoặc cảm giác nôn nao ở dạ dày.",
        "彼の傲慢な態度には、本当にむかつく。",
        "Thái độ ngạo mạn của anh ta thật sự làm tôi bực mình chết đi được.",
        "いらいら, 腹が立つ",
        "すっきり, さっぱりする"
    ),
    (
        "うずうず",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Bứt rứt ngứa ngáy (muốn làm gì đó ngay)",
        "何かしたくて、じっとしていられない様子。",
        "Tâm trạng nóng lòng, bứt rứt muốn hành động ngay lập tức (như muốn đi du lịch, ra sân chơi bóng).",
        "体がなまって、早く運動したくてうずうずしている。",
        "Cơ thể uể oải quá rồi, tôi ngứa ngáy chân tay muốn vận động ngay lập tức.",
        "むずむず, 焦がれる",
        "落ち着く, 平気"
    ),
    (
        "のびのび",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Thong dong / Vui vẻ thoải mái / Vươn mình khỏe mạnh",
        "何の制約もなく、気持ちよく過ごす様子。",
        "Trạng thái tự do tự tại, không bị gò bó áp lực; Hoặc cây cối vươn cành xanh tốt thoải mái.",
        "試験が終わって、のびのびと連休を楽しんだ。",
        "Kỳ thi kết thúc, tôi thong dong tận hưởng kỳ nghỉ dài một cách thoải mái.",
        "のんびり, ゆったり",
        "窮屈な, 緊張する"
    ),
    (
        "まったり",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Thong thả nhàn nhã / Vị tròn trịa đậm đà",
        "のんびりした様子。また、味がまろやかで深い様子。",
        "Trạng thái nghỉ ngơi thong thả nhàn nhã không vội vã; Hoặc hương vị đồ ăn ngậy, béo dịu nhẹ.",
        "休日はカフェでまったり過ごすのが好きだ。",
        "Tôi thích dành những ngày nghỉ để ngồi thong thả nhàn nhã ở quán cà phê.",
        "のんびり, ゆったり",
        "ばたばた, 忙しい"
    ),
    (
        "しつこい",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Dai dẳng đeo bám / Ngấy béo (đồ ăn) / Đậm đặc",
        "しつこくて嫌になる様子。味がしつこい様子。",
        "Độ béo ngấy của món ăn nhiều dầu mỡ khó tiêu; Hoặc tính cách lải nhải dai dẳng làm người khác khó chịu; Cơn ho kéo dài mãi không khỏi.",
        "この料理は油 q 多すぎて、味がしつこい。",
        "Món ăn này nhiều dầu quá nên vị béo ngấy rất khó ăn.",
        "くどい, しつこい",
        "あっさり, さっぱり"
    ),
    (
        "くどくど",
        "Hành Vi & Thái Độ",
        "Lải nhải / Dài dòng văn tự / Nói đi nói lại",
        "同じことをしつこく繰り返して言う様子。",
        "Cách nói chuyện dài dòng, lải nhải lặp đi lặp lại một nội dung khiến người nghe phát ngán.",
        "上司は同じ注意をくどくどと繰り返した。",
        "Sếp cứ lải nhải lặp đi lặp lại một lời nhắc nhở đó mãi.",
        "しつこく, くどい",
        "あっさりと, 簡潔に"
    ),
    (
        "くどい",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Nói dài dòng / Vị quá nồng, ngấy béo",
        "しつこくて嫌味な様子。また、味が濃厚すぎる様子。",
        "Vị thức ăn quá đậm đặc nồng nặc dễ ngấy; Hoặc văn phong, lời nói dài dòng lôi thôi.",
        "彼の言い訳はくどくて、聞くのが嫌になる。",
        "Lời biện bạch của anh ta dài dòng lôi thôi quá, nghe phát ngán.",
        "しつこい, くどくdo",
        "あっさり, さっぱり"
    ),
    (
        "するする",
        "Hành Vi & Thái Độ",
        "Trơn tru / Thoan thoắt / Tuồn tuột",
        "滞りなく滑らかに進む様子。",
        "Chuyển động lướt đi trơn tru không gặp trở ngại (như rắn bò thoăn thoắt, kéo dây thừng tuồn tuột).",
        "ヘビが草の上をするすると這っていった。",
        "Con rắn bò thoăn thoắt trơn tru trên thảm cỏ.",
        "するりと, さらさら",
        "つっかかる, 滞る"
    ),
    (
        "するりと",
        "Hành Vi & Thái Độ",
        "Tuột mất / Trơn tuột / Thoát ra nhẹ nhàng",
        "すべって簡単に抜ける様子。機会を逃す様子。",
        "Cơ thể hoặc đồ vật trơn tuột thoát ra khỏi vòng vây nhẹ nhàng (như lươn tuột khỏi tay, hoặc tuột mất cơ hội quý giá).",
        "容疑者は人混みの中をするりとすり抜けた。",
        "Nghi phạm đã trơn tuột luồn lách qua đám đông trốn thoát.",
        "するする, ぬるりと",
        "引っかかる, つかまる"
    ),
    (
        "こつこつ",
        "Hành Vi & Thái Độ",
        "Cần mẫn / Từng chút một / Cộc cộc (tiếng gõ)",
        "地道に努力を重ねる様子。硬い物が当たる音。",
        "Sự cố gắng kiên trì, tích lũy đều đặn từng chút một để đạt mục tiêu; Hoặc tiếng giày gõ cộc cộc trên hành lang.",
        "彼は毎日こつこつと受験勉強を続けている。",
        "Anh ấy vẫn cần mẫn kiên trì tự học thi mỗi ngày.",
        "地道に, 着々と",
        "怠ける, 一気に"
    ),
    (
        "ちびちび",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Nhấm nháp từng tí / Nhấp từng ngụm / Tí một",
        "少しずつ物を消費したり飲んだりする様子。",
        "Hành động uống rượu nhấm nháp từng ngụm nhỏ, hoặc tiêu xài tiền bạc cực kỳ tiết kiệm tí một.",
        "お気に入りのウイスキーをちびちびと飲む。",
        "Nhấm nháp từng ngụm nhỏ ly rượu Whisky yêu thích.",
        "少しずつ, ちょびちょび",
        "がぶがぶ, 一気に"
    ),
    (
        "ちょくちょく",
        "Hành Vi & Thái Độ",
        "Thường xuyên / Tăm tắp / Hay xảy ra",
        "しばしば。たびたび。頻繁に起こる様子。",
        "Tần suất xảy ra sự việc thường xuyên, lặp lại nhiều lần (như thường xuyên ghé tiệm ăn, thường xuyên gặp lỗi).",
        "あの店には仕事帰りによくちょくちょく寄る。",
        "Tôi thường xuyên ghé vào cửa hàng đó trên đường đi làm về.",
        "たびたび, しばしば",
        "たまに, めったに"
    ),
    (
        "うろちょろ",
        "Hành Vi & Thái Độ",
        "Đi quanh quẩn / Lảng vảng làm phiền",
        "あちこち動き回って邪魔になる様子。",
        "Hành động đi qua đi lại lẩn quẩn lảng vảng xung quanh gây cản trở, vướng chân người khác.",
        "台所で忙しい時に、子供にうろちょろされて困った。",
        "Lúc đang bận rộn trong bếp mà đứa trẻ cứ lảng vảng quanh quẩn vướng chân thật phiền phức.",
        "うろうろ, ちょこまか",
        "じっとしている"
    ),
    (
        "きらきら",
        "Mức Độ & Biến Đổi",
        "Lấp lánh / Lung linh / Long lanh",
        "光り輝く様子。",
        "Ánh sáng lấp lánh phản chiếu của kim cương, ngôi sao trên trời đêm hoặc đôi mắt long lanh hạnh phúc.",
        "夜空に星がきらきらと輝いている。",
        "Những ngôi sao đang tỏa sáng lấp lánh trên bầu trời đêm.",
        "きらびやか, 輝く",
        "どんより, 暗い"
    ),
    (
        "ぎらぎら",
        "Mức Độ & Biến Đổi",
        "Chiếu chói chang / Chói mắt / Nhẫy mỡ",
        "光が強すぎてまぶしい様子。また、脂ぎっている様子。",
        "Ánh nắng mặt trời mùa hè chiếu chói chang gay gắt đến hoa mắt; Hoặc khuôn mặt nhẫy bóng mỡ.",
        "夏の太陽がぎらぎらと照りつける。",
        "Mặt trời mùa hè chiếu sáng chói chang gay gắt.",
        "まぶしい, ギラギラする",
        "曇る, 薄暗い"
    ),
    (
        "うるうる",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Mắt rưng rưng / Căng mọng nước",
        "涙が目にたまっている様子。また、水分を含んで潤っている様子。",
        "Đôi mắt rưng rưng lệ vì cảm động sắp khóc; Hoặc làn da căng mọng đầy nước ẩm mịn.",
        "映画の結末を見て、目がうるうるしてきた。",
        "Xem xong kết cục bộ phim, mắt tôi rưng rưng nước mắt.",
        "涙ぐむ, 潤う",
        "かさかさ, 乾く"
    ),
    (
        "げらげら",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Cười ha hả / Cười toác miệng sằng sặc",
        "大声で品なく笑う様子。",
        "Điệu cười rất to, sằng sặc, cười lớn không giữ kẽ khi nghe chuyện cực kỳ hài hước.",
        "テレビのお笑い番組を見て、げらげら笑った。",
        "Xem chương trình hài trên tivi rồi cười ha hả sằng sặc.",
        "大笑い, げらげら笑う",
        "しくしく, めそめそ"
    ),
    (
        "くすくす",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Cười khúc khích / Cười thầm trộm",
        "声を抑えて笑う様子。",
        "Tiếng cười nhỏ, khúc khích, cố kìm nén âm lượng trong lớp học hoặc cuộc họp khi có chuyện ngộ nghĩnh.",
        "授業中なのに、面白くてくすくす笑ってしまった。",
        "Đang trong giờ học mà vì buồn cười quá nên tôi cứ cười khúc khích.",
        "クスクス, 含み笑い",
        "げらげら, 大声で笑う"
    ),
    (
        "しくしく",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Khọc thút thít nhỏ lệ / Đau âm ỉ (bụng)",
        "静かに泣き続ける様子。また、鈍い痛みが続く様子。",
        "Nghĩa chính: Khóc nhỏ nhẹ, sụt sùi thút thít một mình; Hoặc cảm giác đau bụng âm ỉ dai dẳng.",
        "失恋した彼女は、部屋の隅でしくしく泣いていた。",
        "Cô ấy bị thất tình đang ngồi khóc thút thít ở góc phòng.",
        "めそめそ, 泣く, 痛む",
        "にこにこ, げらげら"
    ),
    (
        "かんかん",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Nổi giận lôi đình / Nắng chang chang",
        "激しく怒っている様子。太陽が強く照りつける様子。",
        "Cơn giận dữ bốc hỏa đùng đùng, nổi lôi đình của bố mẹ; Hoặc thời tiết nắng chang chang gay gắt.",
        "約束の時間を大幅に遅れて、彼はかんかんに怒っている。",
        "Trễ hẹn quá lâu khiến anh ấy nổi giận lôi đình.",
        "激怒する, ぷんぷん",
        "にこやか, 穏やか"
    ),
    (
        "つんつん",
        "Hành Vi & Thái Độ",
        "Lạnh lùng kiêu kỳ / Gắt gỏng khó gần / Spiky",
        "不機嫌で冷たい態度をとる様子。また、尖っている様子。",
        "Thái độ lạnh lùng, kiêu kỳ khó gần không thèm tiếp chuyện; Hoặc mái tóc dựng đứng nhọn hoắt.",
        "彼女は話しかけてもつんつんしていて返事もしない。",
        "Bắt chuyện mà cô ấy cứ lạnh lùng kiêu kỳ chẳng thèm trả lời.",
        "不愛想, つれない",
        "愛想がいい, にこにこする"
    ),
    (
        "きびきび",
        "Hành Vi & Thái Độ",
        "Nhanh nhẹn dứt khoát / Hoạt bát tác phong quân đội",
        "動作や態度が元気がよく、引き締まっている様子。",
        "Tác phong làm việc nhanh nhẹn dứt khoát, di chuyển hoạt bát đầy năng lượng.",
        "新人社員はきびきびとした態度で働いている。",
        "Nhân viên mới đang làm việc với tác phong vô cùng nhanh nhẹn dứt khoát.",
        "はきはき, てきぱき",
        "だらだら, もたもた"
    ),
    (
        "きりきり",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Đau nhói quặn thắt (dạ dày) / Bận rộn quay cuồng",
        "胃などが刺すように痛む様子。また、忙しく働く様子。",
        "Cơn đau bụng quặn thắt dữ dội ở dạ dày do căng thẳng stress; Hoặc làm việc bận rộn quay cuồng liên tục.",
        "ストレスのせいで、胃がきりきり痛む。",
        "Do stress nên dạ dày tôi cứ đau nhói quặn thắt lại.",
        "ずきずき痛む, 胃痛",
        "痛みが治まる"
    ),
    (
        "むしむし",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Oi bức / Nóng ẩm ngột ngạt",
        "湿度が高くて蒸し暑い様子。",
        "Thời tiết mùa hè Nhật Bản có độ ẩm cực cao, gây ra cảm giác oi bức ngột ngạt khó chịu.",
        "日本の夏は湿気が高くて、毎日むしむしする。",
        "Mùa hè Nhật Bản độ ẩm cao nên ngày nào cũng oi bức ngột ngạt khó chịu.",
        "蒸し暑い, じめじめ",
        "からっと, ひんやり"
    ),
    (
        "じめじめ",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Ẩm mốc / Ẩm ướt khó chịu / U ám",
        "湿気が多くて湿っている様子。陰気な様子。",
        "Thời tiết mùa mưa làm phòng ốc ẩm mốc, quần áo ẩm ướt không khô; Hoặc tính cách u ám buồn bã.",
        "梅雨の時期は部屋の中がじめじめして嫌だ。",
        "Mùa mưa đến là trong phòng cứ ẩm ướt mốc meo thật khó chịu.",
        "じめじめする, 湿っぽい",
        "からっと, 乾燥する"
    ),
    (
        "からっと",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Giòn tan (tempura) / Khô ráo thoáng đãng / Tính cởi mở",
        "乾燥して爽やかな様子。揚げ物がサクサクしている様子。",
        "Hương vị đồ chiên giòn rụm không ngấy; Hoặc thời tiết khô ráo thoáng đãng sau cơn mưa; Tính cách cởi mở không để bụng.",
        "この天ぷらはからっと揚がっていて美味しい。",
        "Món tempura này được chiên giòn tan ăn ngon quá.",
        "からり, サクサク",
        "じめじめ, しつocい"
    ),
    (
        "さらっと",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Trơn tru nhẹ nhàng / Vị thanh nhẹ không bết dính",
        "ベタつかず、さっぱりしている様子。簡単に物事を行う様子。",
        "Làn da mịn màng không bị nhờn rít sau khi thoa kem; Hoặc vị canh thanh nhẹ dễ ăn.",
        "この化粧水を使うと、肌がさらっとする。",
        "Dùng loại nước hoa hồng này giúp da mịn màng thanh nhẹ không bết dính.",
        "さらさら, さっぱり",
        "べたべた, ぬるぬる"
    ),
    (
        "ざあざあ",
        "Mức Độ & Biến Đổi",
        "Mưa xối xả / Mưa như trút nước",
        "雨が激しく降る音や様子。",
        "Âm thanh tả tiếng mưa rơi xối xả, ào ào trút xuống mặt đất.",
        "急に雨がざあざあ降り出してきた。",
        "Trời đột ngột đổ mưa xối xả ào ào.",
        "どしゃ降り, 土砂降り",
        "しとしと, ぽつぽつ"
    ),
    (
        "しとしと",
        "Mức Độ & Biến Đổi",
        "Mưa rơi tí tách / Mưa phùn nhẹ nhàng",
        "静かに雨が降り続く様子。",
        "Mưa xuân hoặc mưa phùn nhẹ nhàng, rơi tí tách không tiếng động lớn nhưng kéo dài dai dẳng.",
        "春の雨がしとしとと降っている。",
        "Cơn mưa xuân đang rơi tí tách nhẹ nhàng.",
        "小雨, ぽつぽつ",
        "ざあざあ, どしゃ降り"
    ),
    (
        "ぱらぱら",
        "Mức Độ & Biến Đổi",
        "Mưa lác đác vài hạt / Lật sách xoành xoạch / Cơm rang tơi xốp",
        "小雨やあられがまばらに降る様子。本をめくる様子。ご飯がほぐれている様子。",
        "Ba ý nghĩa: Mưa lác đác vài hạt rơi rải rác; Lật trang sách nhanh xoành xoạch; Hoặc hạt cơm rang tơi xốp không bết dính.",
        "雨がぱらぱらと降り始めた。",
        "Mưa đã bắt đầu rơi lác đác vài hạt rồi.",
        "ぱらつく, ぽつぽつ",
        "ざあざあ, ぎっしり"
    ),
    (
        "ごうごう",
        "Mức Độ & Biến Đổi",
        "Tiếng gió rít ào ào / Tiếng nước chảy cuồn cuộn",
        "風が激しく吹く音。水が激しく流れる音。",
        "Tiếng gió bão rít mạnh gào rú ào ào bên ngoài cửa sổ hoặc tiếng nước sông lũ chảy xiết cuồn cuộn.",
        "台風の風がごうごうと吹き荒れている。",
        "Gió bão đang thổi rít lên ào ào gào rú dữ dội.",
        "ごうごうと, 轟々と",
        "しとしと, そよそよ"
    ),
    (
        "そよそよ",
        "Mức Độ & Biến Đổi",
        "Thổi hiu hiu / Nhè nhẹ (gió xuân)",
        "風が静かに心地よく吹く様子。",
        "Làn gió xuân thổi nhè nhẹ, hiu hiu dễ chịu làm rung rinh ngọn cỏ.",
        "春の風がそよそよと吹いていて気持ちがいい。",
        "Gió xuân thổi hiu hiu nhè nhẹ thật dễ chịu."
    )"""

def main():
    script_path = "/Users/tuyennq1001/htdocs/jlpt-n1/scratch/generate_goi.py"
    if not os.path.exists(script_path):
        print(f"Lỗi: Không tìm thấy tệp {script_path}")
        return
        
    with open(script_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Tìm đoạn cuối của words_data
    # Chúng ta biết "べたべた, ごつごつ" là thuộc từ "さらさら" (từ thứ 200 ban đầu)
    # Và tiếp sau đó là dấu ngoặc đóng ), và dấu ngoặc đóng ] của mảng words_data.
    target_str = '"べたべた, ごつごつ"\\n    )\\n]'
    # Để an toàn, hãy tìm chuỗi cụ thể của từさらさら và chèn trước dấu đóng mảng
    lines = content.splitlines()
    insert_idx = -1
    
    for idx in range(len(lines) - 1, -1, -1):
        if lines[idx].strip() == "]" and any("さらさら" in line for line in lines[idx-12:idx]):
            insert_idx = idx
            break
            
    if insert_idx != -1:
        # Thay thế dấu đóng ngoặc ) cuối của từ cũ bằng ),
        # Vì trước đó từさらさら kết thúc bằng:
        #     )
        # ]
        # Chúng ta cần đổi thành:
        #     ),
        #     (mục mới)...
        # ]
        # Hãy kiểm tra dòng ngay trước insert_idx
        prev_line_idx = insert_idx - 1
        if lines[prev_line_idx].strip() == ")":
            lines[prev_line_idx] = "    ),"
            
        # Chèn các từ mới
        new_lines = lines[:insert_idx] + [new_words_tuples] + lines[insert_idx:]
        
        with open(script_path, "w", encoding="utf-8") as f:
            f.write("\n".join(new_lines))
        print("Đã thêm thành công 50 từ vựng mới vào generate_goi.py!")
    else:
        print("Lỗi: Không tìm thấy vị trí thích hợp để chèn từ vựng.")

if __name__ == "__main__":
    main()
