# -*- coding: utf-8 -*-
import os

# Danh sách 100 từ vựng láy tượng hình / tượng thanh tiếng Nhật (Giongo / Gitaigo)
# Định dạng: (từ_vựng, nhóm, ý_nghĩa, jp_def, sắc_thái, ví_dụ_jp, ví_dụ_vi, từ_đồng_nghĩa, từ_trái_nghĩa)
words_data = [
    # Nhóm 1: Trạng Thái Tinh Thần & Cảm Xúc (Mental & Emotional States) - 25 từ
    (
        "すっきり",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Sảng khoái / Nhẹ nhõm / Gọn gàng (sau khi trút bỏ gánh nặng)",
        "余計なものや面倒なものがなく、気持ちがよい様子。",
        "Cảm giác dễ chịu khi những điều phiền toái, thừa thãi hoặc mập mờ được giải quyết triệt để (ví dụ: dọn dẹp xong phòng sạch sẽ, giải tỏa lo lắng trong lòng, hoặc hát hò giải trí xong).",
        "カラオケで大声で歌ったら、気分がすっきりした。",
        "Hát thật to ở karaoke xong, tâm trạng sảng khoái hẳn.",
        "さっぱり, ほっと",
        "むかむか, もやもや"
    ),
    (
        "がっかり",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Thất vọng / Chán nản / Sụp đổ tinh thần",
        "期待が外れて、力落としをする様子。",
        "Trạng thái buồn bã, mất sạch năng lượng khi kỳ vọng lớn của bản thân bị đổ vỡ (dáng vẻ vai sụp xuống, cúi mặt).",
        "楽しみにしていたコンサートが中止になり、がっかりした。",
        "Buổi hòa nhạc mong đợi bấy lâu bị hủy bỏ khiến tôi vô cùng thất vọng.",
        "しょんぼり, 失望する",
        "うきうき, わくわく"
    ),
    (
        "いらいら",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Bực bội / Sốt ruột / Nóng lòng",
        "物事が思うようにならず、気持ちが落ち着かない様子。",
        "Cảm xúc bực bội, khó chịu khi mọi việc không diễn ra theo ý muốn hoặc phải chờ đợi lâu mà sốt ruột.",
        "渋滞で車が全然進まず、いらいらする。",
        "Vì kẹt xe nên xe hoàn toàn không tiến lên được, thật là bực bội.",
        "やきもき, 焦る",
        "のんびり, ほっと"
    ),
    (
        "どきどき",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Hồi hộp / Tim đập thình thịch",
        "運動や緊張、驚きなどで心臓の鼓動が速くなる様子。",
        "Tiếng tim đập nhanh do lo lắng, căng thẳng, sợ hãi hoặc phấn khích (ví dụ trước khi phát biểu, gặp người yêu, hoặc khi đứng trước kết quả thi).",
        "発表の番が近づいてきて、胸がどきどきしている。",
        "Lượt phát biểu đang đến gần, lồng ngực tôi đập thình thịch.",
        "はらはら, 緊張する",
        "ほっとする, 落ち着く"
    ),
    (
        "わくわく",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Háo hức / Hồi hộp mong chờ",
        "期待や喜びで胸が躍り、落ち着かない様子。",
        "Trạng thái háo hức, mong đợi những điều tốt đẹp, vui sướng sắp diễn ra (như trước chuyến đi du lịch, trước ngày khai giảng).",
        "明日から旅行なので, 心がわくわくしている。",
        "Vì ngày mai đi du lịch nên trong lòng vô cùng háo hức.",
        "うきうき, 期待する",
        "がっかり, しょんぼり"
    ),
    (
        "はらはら",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Lo lắng / Nhấp nhổm (lo sợ giùm cho người khác)",
        "他人の様子を見て、危なっかしくて心配する様子。",
        "Cảm giác lo sợ, hồi hộp khi nhìn thấy người khác ở trong tình thế nguy hiểm (như xem xiếc, nhìn em bé tập đi).",
        "子供が木に登っているのを見て、はらはらした。",
        "Nhìn thấy đứa trẻ trèo lên cây mà tôi lo nhấp nhổm cả người.",
        "どきどき, ハラハラする",
        "ほっとする, 安心する"
    ),
    (
        "うっとり",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Say đắm / Ngây ngất / Say sưa ngắm nhìn",
        "美しいものなどに心を奪われて、ぼんやりしている様子。",
        "Tâm trạng bị hút hồn, say đắm trước vẻ đẹp hoặc một tác phẩm nghệ thuật, âm nhạc xuất sắc.",
        "彼女は美しいバイオリンの音色にうっとり聞き入っていた。",
        "Cô ấy say sưa lắng nghe giai điệu vĩ cầm tuyệt đẹp.",
        "うっとりする, 恍惚とする",
        "無関心, 興ざめする"
    ),
    (
        "しょんぼり",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Ủ rũ / Buồn bã / Thẫn thờ",
        "元気がなく、うなだれている様子。",
        "Dáng vẻ buồn bã, ủ rũ vì bị mắng, thất bại nhẹ hoặc gặp chuyện buồn nhỏ.",
        "叱られた犬が、しょんぼりして座っている。",
        "Chú chó bị mắng đang ngồi ủ rũ một góc.",
        "がっかり, 落ち込む",
        "うきうき, 元気いっぱい"
    ),
    (
        "びくびく",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Run sợ / Phấp phỏng lo sợ / Sợ sệt",
        "恐れて、体が震える様子。心配で落ち着かない様子。",
        "Sự sợ hãi dồn dập, phấp phỏng vì sợ bị phát hiện lỗi lầm, sợ bị phạt hoặc gặp nguy hiểm.",
        "先生に叱られるのではないかと、びくびくしている。",
        "Tôi cứ phấp phỏng lo sợ không biết có bị thầy giáo mắng hay không.",
        "おどおど, 恐れる",
        "堂々とする, 泰然とする"
    ),
    (
        "おどおど",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Rụt rè / Lúng túng / Khép nép (thiếu tự tin)",
        "自信がなく、恐れて落ち着かない態度をとる様子。",
        "Thái độ e sợ, không tự tin, ngập ngừng lúng túng khi giao tiếp hoặc đứng trước đám đông.",
        "面接の時、緊張しておどおどしてしまった。",
        "Lúc phỏng vấn, vì căng thẳng nên tôi cứ lúng ta lúng túng.",
        "びくびく, 卑屈になる",
        "堂々とする, はきはきする"
    ),
    (
        "ほっと",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Thở phào nhẹ nhõm / Yên tâm",
        "緊張が解けて、安心する様子。",
        "Cảm giác trút bỏ căng thẳng, thở phào khi một nguy cơ trôi qua hoặc công việc kết thúc thành công.",
        "試験がすべて終わって、ほっとした。",
        "Kỳ thi đã kết thúc hoàn toàn, tôi thở phào nhẹ nhõm.",
        "安心する, 一安心",
        "はらはら, どきどき"
    ),
    (
        "むかむか",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Nôn nao / Bực tức / Tức tối lồng lộn",
        "吐き気がする様子。また、怒りでおさまらない様子。",
        "Có hai nghĩa: Cảm thấy nôn nao, buồn nôn ở dạ dày; Hoặc cảm giác tức tối phát điên vì hành động vô lý của ai đó.",
        "彼の失礼な態度を思い出すと、今でも胸がむかむかする。",
        "Nghĩ lại thái độ vô lễ của anh ta, đến giờ tôi vẫn thấy tức cành hông.",
        "いらいら, 吐き気がする",
        "すっきり, さっぱり"
    ),
    (
        "やきもき",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Sốt ruột / Bồn chồn lo lắng (về chuyện của người khác)",
        "他人のことが心配で、どうしていいか焦る様子。",
        "Sự bồn chồn sốt ruột vì lo lắng cho tình hình của người khác mà bản thân không thể can thiệp được.",
        "連絡が取れない息子を心配して、母はやきもきしていた。",
        "Lo lắng cho đứa con trai không liên lạc được, người mẹ cứ bồn chồn đứng ngồi không yên.",
        "いらいら, 心配する",
        "のんびり, 泰然とする"
    ),
    (
        "おろおろ",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Cuống cuồng / Lúng túng mất phương hướng",
        "どうしていいか分からず、慌てふためく様子。",
        "Trạng thái rối bời, không biết phải xử lý thế nào khi xảy ra sự cố đột ngột ngoài tầm kiểm soát.",
        "事故の現場を見て, 何もできずにおろおろするばかりだった。",
        "Nhìn thấy hiện trường tai nạn, tôi chỉ biết cuống cuồng lúng túng mà không làm được gì.",
        "うろたえる, パニックになる",
        "冷静沈着, 落ち着く"
    ),
    (
        "びっくり",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Giật mình / Kinh ngạc / Bất ngờ",
        "急な出来事に驚く様子。",
        "Sự ngạc nhiên, giật mình do những âm thanh lớn hoặc sự việc bất ngờ xảy ra ngay trước mắt.",
        "大きな音がして、びっくりして跳び上がった。",
        "Có tiếng động lớn phát ra khiến tôi giật mình nhảy dựng lên.",
        "驚く, 仰天する",
        "平気, 動じない"
    ),
    (
        "うきうき",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Hân hoan / Rộn ràng vui tươi",
        "嬉しくて気持ちが浮き立ち、楽しそうな様子。",
        "Tâm trạng phấn chấn, nhẹ nhàng, vui vẻ biểu hiện ra bên ngoài (như bước đi nhún nhảy vì vui).",
        "彼女は新しいデート服を着て、うきうきと出かけた。",
        "Cô ấy diện bộ đồ hẹn hò mới rồi hân hoan bước ra ngoài.",
        "わくわく, うきうきする",
        "しょんぼり, がっかり"
    ),
    (
        "めそめそ",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Khóc thút thít / Sụt sùi",
        "弱々しく泣き続ける様子。",
        "Hành động khóc nhỏ, kéo dài, thút thít (thường dùng cho trẻ con hoặc người yếu đuối).",
        "いつまでもめそめそ泣くのはやめなさい。",
        "Đừng có khóc thút thít suốt như thế nữa.",
        "しくしく, 泣く",
        "にこにこ, からから笑う"
    ),
    (
        "おずおず",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Rụt rè / Rón rén / Ngần ngại",
        "ためらいながら、恐る恐る物事を行う様子。",
        "Hành vi ngập ngừng, rụt rè tiến lại gần hoặc đặt câu hỏi vì sợ sệt hay kính cẩn.",
        "彼は社長室のドアをおずおずとノックした。",
        "Anh ấy rụt rè gõ cửa phòng giám đốc.",
        "恐る恐る, ためらう",
        "堂々と, 思い切って"
    ),
    (
        "もじもじ",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Ngượng nghịu / Ngại ngùng lúng túng",
        "恥ずかしがって、言いたいことが言えない様子。",
        "Thái độ ngượng ngùng, ngập ngừng không dám bộc lộ ý kiến hay hành động vì xấu hổ trước người khác.",
        "子供は知らない人の前で、恥ずかしそうにもじもじしていた。",
        "Đứa bé ngượng nghịu lúng túng trước mặt người lạ.",
        "はにかむ, 照れる",
        "堂々とする, はきはきする"
    ),
    (
        "てきぱき",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Nhanh nhẹn / Tháo vát / Nhanh nhảu",
        "仕事を要領よく、手際よく進める様子。",
        "Cách giải quyết công việc vô cùng nhanh chóng, có trình tự và hiệu quả cao.",
        "彼女は家事をてきぱきと片付けた。",
        "Cô ấy tháo vát dọn dẹp nhanh gọn việc nhà.",
        "さっさと, 手際よく",
        "ぐずぐず, のろのろ"
    ),
    (
        "ぬくぬく",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Ấm êm / Dễ chịu / Sung sướng",
        "暖かく快適に過ごす様子。楽をしている様子。",
        "Trạng thái sống thoải mái, ấm áp dễ chịu mà không phải chịu vất vả cực nhọc.",
        "寒い冬の日に、こたつでぬくぬく過ごすのは最高だ。",
        "Vào ngày đông giá rét, ngồi ấm êm trong bàn sưởi Kotatsu thì thật tuyệt vời.",
        "ぬくぬくする, 快適に過ごす",
        "がたがた, 震える"
    ),
    (
        "はっきり",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Rõ ràng / Dứt khoát",
        "形や意味が明確で、疑う余地がない様子。",
        "Trạng thái biểu đạt rõ ràng về mặt hình ảnh, âm thanh hoặc ý chí dứt khoát không mập mờ.",
        "富士山がはっきりと見えた。",
        "Núi Phú Sĩ đã nhìn thấy rõ mồn một.",
        "明確に, くっきり",
        "ぼんやり, うやむや"
    ),
    (
        "すくすく",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Mau lớn / Khỏe mạnh (trẻ em, cây cối)",
        "元気に成長する様子。",
        "Trạng thái lớn nhanh như thổi, phát triển khỏe mạnh của trẻ nhỏ hoặc thực vật.",
        "子供たちは健康に、すくすくと育っている。",
        "Lũ trẻ đang phát triển vô cùng khỏe mạnh, lớn nhanh như thổi.",
        "順調に育つ",
        "衰える, 枯れる"
    ),
    (
        "いそいそ",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Hớn hở vội vã / Hăm hở",
        "楽しみな事のために、嬉しそうに準備して出かける様子。",
        "Dáng vẻ hối hả chuẩn bị ra ngoài với tâm trạng phấn khởi vì có việc vui chờ đợi phía trước.",
        "彼はパーティーに行くために、いそいそと支度をしている。",
        "Anh ấy đang hớn hở chuẩn bị sửa soạn để đi dự tiệc.",
        "うきうき, 嬉しそうに",
        "とぼとぼ, 重い足取りで"
    ),
    (
        "じりじり",
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Nóng ruột chờ đợi / Sốt ruột",
        "焦って、いらだちながら待つ様子。",
        "Cảm giác sốt ruột, nóng lòng chờ đợi một thời khắc nào đó đang đến rất chậm.",
        "締め切り時間が近づき, じりじりしながら待った。",
        "Thời hạn chót đang đến gần, tôi sốt ruột nóng lòng chờ đợi.",
        "いらいら, 焦る",
        "のんびり, 泰然とする"
    ),

    # Nhóm 2: Cảm Giác Cơ Thể & Thể Chất (Physical Feelings & Food) - 25 từ
    (
        "さっぱり",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Sảng khoái mát mẻ / Thanh đạm (vị ăn) / Hoàn toàn không (kèm phủ định)",
        "汚れや不快感が消えて爽快な様子。しつこさがない様子。",
        "Thường dùng cho sự dễ chịu của cơ thể sau tắm, rửa sạch bụi bẩn, hoặc vị thức ăn thanh mát không ngấy. Ở phủ định chỉ sự hoàn toàn không hiểu/biết.",
        "お風呂に入って汗を流したので, さっぱりした。",
        "Tắm rửa sạch mồ hôi xong thật là sảng khoái.",
        "すっきり, 清々しい",
        "しつこい, むかむか"
    ),
    (
        "ぴったり",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Vừa khít / Vừa vặn hoàn hảo / Phù hợp nhất",
        "すき間なく重なったり合ったりする様子。条件や性格がよく合う様子。",
        "Diễn tả hai vật khớp với nhau không kẽ hở (giày vừa chân, quần áo vừa người) hoặc một công việc cực kỳ phù hợp với năng lực/tính cách.",
        "この新しいスニーカーは、私の足にぴったりだ。",
        "Đôi giày thể thao mới này vừa khít hoàn hảo với chân tôi.",
        "ちょうど, 適合する",
        "だぶだぶ, ゆるゆる"
    ),
    (
        "ぐっすり",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Ngủ say / Ngủ ngon giấc",
        "深く眠っている様子。",
        "Trạng thái ngủ sâu, ngon giấc, không bị chập chờn hay thức giấc giữa chừng.",
        "昨夜は疲れていたので, 朝までぐっすり眠った。",
        "Tối qua mệt quá nên tôi ngủ một mạch say nồng tới sáng.",
        "熟睡する, ぐうぐう",
        "うとうと, 目をぱちくりする"
    ),
    (
        "ぺこぺこ",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Đói cồn cào / Khúm núm cúi đầu",
        "非常にお腹が空いている様子。また, 頭を何度も下げる様子。",
        "Hai ý nghĩa chính: Cảm giác bụng đói cồn cào, kêu réo; Hoặc thái độ cúi đầu khúm núm xin lỗi hay nịnh bợ.",
        "お腹がぺこぺこで、もう歩けない。",
        "Bụng đói cồn cào rồi, tôi không đi nổi nữa.",
        "腹ペコ, お辞儀する",
        "満腹, 堂々とする"
    ),
    (
        "からから",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Khô khốc / Khát khô cổ",
        "水分が完全になくなっている様子。",
        "Tình trạng khô hạn hoàn toàn (như ruộng đồng khô nứt nẻ), hoặc cổ họng khát khô không có một giọt nước.",
        "喉がからからなので, 冷たい水が飲みたい。",
        "Cổ họng khát khô rồi, tôi muốn uống nước lạnh quá.",
        "乾燥する, 乾く",
        "しっとり, じっとり"
    ),
    (
        "ぱっちり",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Tròn xoe / To tròn (mắt)",
        "目が大きく、はっきりと開いている様子。",
        "Đôi mắt mở to tròn, sáng ngời, thường dùng mô tả đôi mắt của trẻ em hoặc các cô gái xinh đẹp.",
        "彼女はぱっちりした目をしている。",
        "Cô ấy sở hữu đôi mắt to tròn xoe.",
        "目が大きい, はっきり",
        "糸目, 細い目"
    ),
    (
        "ぽかぽか",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Ấm áp / Dễ chịu (cơ thể, thời tiết)",
        "体が心地よく温まる様子。",
        "Cảm giác ấm áp dịu nhẹ từ bên trong cơ thể (như sau khi uống trà nóng) hoặc thời tiết mùa xuân ấm áp dễ chịu.",
        "日差しを浴びていると, 体がぽかぽかしてきた。",
        "Tắm trong ánh nắng làm cơ thể tôi ấm áp hẳn lên.",
        "ぬくぬく, 暖かい",
        "ぞくぞく, ひんやり"
    ),
    (
        "ゾクゾク",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Rùng mình vì lạnh hoặc vì phấn khích",
        "寒さや恐怖, 興奮で体が震える様子。",
        "Cảm giác rùng mình nổi gai ốc do cơ thể sắp bị sốt (ớn lạnh), do sợ hãi hoặc do quá phấn khích, cảm động.",
        "熱があるのか、寒気で体がゾクゾクする。",
        "Hình như bị sốt hay sao mà cơ thể tôi cứ run lên bần bật vì ớn lạnh.",
        "ぞっとする, ぶるぶる",
        "ぽかぽか, 温まる"
    ),
    (
        "ずきずき",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Đau nhói / Đau buốt liên tục từng cơn",
        "脈打つように、絶えず痛む様子。",
        "Cảm giác đau nhức nhối theo từng nhịp đập của mạch máu (thường dùng cho đau răng, vết thương hở hoặc đau đầu).",
        "虫歯のせいで、歯がずきずき痛む。",
        "Do sâu răng nên răng tôi cứ đau buốt lên từng cơn.",
        "ずきずき痛む, 疼く",
        "痛みが和らぐ"
    ),
    (
        "むずむず",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Ngứa ngáy / Bứt rứt muốn hành động",
        "かゆくて落ち着かない様子。何かしたくてたまらない様子。",
        "Có hai nghĩa: Cảm giác ngứa ngáy nhẹ trên da thịt; Hoặc cảm giác bứt rứt, nóng lòng muốn làm việc gì đó ngay lập tức.",
        "春になると, 花粉のせいで鼻がむずむずする。",
        "Cứ đến mùa xuân là mũi tôi lại ngứa ngáy khó chịu vì phấn hoa.",
        "うずうず, かゆい",
        "すっきりする"
    ),
    (
        "じんじん",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Tê rần rần / Tê buốt",
        "しびれたり、痛みが響いたりする様子。",
        "Cảm giác tê buốt hoặc tê rần rần ở tay chân khi bị lạnh buốt hoặc sau khi ngồi xếp bằng quá lâu.",
        "寒さで手がかじかんで, じんじんする。",
        "Cái lạnh làm tay tôi tê buốt rần rần.",
        "しびれる, 痺痛",
        "感覚が戻る"
    ),
    (
        "くたくた",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Mệt rã rời / Mệt lử / Nhão nhẹt",
        "ひどく疲れえて、力が入らない様子。",
        "Trạng thái mệt mỏi rã rời, không còn chút sức lực nào sau khi hoạt động nặng nhọc; Hoặc đồ ăn được nấu nhừ nhão.",
        "一日中歩き回って、もうくたくただ。",
        "Đi bộ cả ngày trời nên tôi mệt rã rời cả người rồi.",
        "へとへと, 疲れ果てる",
        "元気いっぱい, シャキッとする"
    ),
    (
        "へとへと",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Mệt đứt hơi / Kiệt sức hoàn toàn",
        "疲れ果てて、全く力が出ない様子。",
        "Mức độ mệt mỏi cực độ, kiệt quệ hoàn toàn thể lực đến mức không thể đứng vững hay cử động.",
        "残業が続いて、毎日へとへとだ。",
        "Làm thêm giờ liên tục khiến ngày nào tôi cũng kiệt sức hoàn toàn.",
        "くたくた, 疲労困憊",
        "元気いっぱい, 活気がある"
    ),
    (
        "ぶるぶる",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Run cầm cập / Run lẩy bẩy",
        "寒さや恐怖で、小刻みに震える様子。",
        "Cơ thể run rẩy liên tục do thời tiết quá lạnh hoặc do nỗi sợ hãi tột độ.",
        "寒さで体がぶるぶる震えた。",
        "Cơ thể tôi run lên cầm cập vì lạnh.",
        "がくがく, ガタガタする",
        "じっとしている"
    ),
    (
        "がくがく",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Run bủn rủn (đầu gối, khớp xương)",
        "関節が緩んで、がたがた震える様子。",
        "Cảm giác khớp xương, đầu gối run rẩy bủn rủn đứng không vững sau khi leo núi mệt hoặc do quá sợ hãi.",
        "登山の後で、足の膝ががくがくしている。",
        "Sau khi leo núi xong, đầu gối chân tôi cứ run bủn rủn.",
        "ぶるぶる, ガタガタ",
        "しゃんとする, 安定する"
    ),
    (
        "ぞっと",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Rợn tóc gáy / Nổi gai ốc / Kinh hãi",
        "恐怖や冷気で、一瞬背筋が寒くなる様子。",
        "Cảm giác ớn lạnh chạy dọc sống lưng, rợn người khi nghĩ đến một tình huống đáng sợ đã xảy ra hoặc phim kinh dị.",
        "事故のことを考えると、今でもぞっとする。",
        "Nghĩ lại vụ tai nạn đó, đến giờ tôi vẫn thấy rợn tóc gáy.",
        "ゾクゾクする, 身の毛がよだつ",
        "ほっとする, 安心する"
    ),
    (
        "ひんやり",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Mát lạnh se se / Dễ chịu",
        "冷たくて心地よく感じられる様子。",
        "Cảm giác mát lạnh se se, dễ chịu của không khí ban mai hoặc nước mát.",
        "早朝の森の空気は、ひんやりとしていて気持ちがいい。",
        "Không khí rừng lúc sáng sớm mát lạnh se se thật là dễ chịu.",
        "冷やりとする, 涼しい",
        "むんむん, ぽかぽか"
    ),
    (
        "むんむん",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Oi bức nồng nặc / Ngột ngạt",
        "熱気やにおいが立ち込めている様子。",
        "Bầu không khí ngột ngạt chứa đầy nhiệt độ nóng bức hoặc mùi hương quá nồng nặc lan tỏa trong không gian kín.",
        "満員電車の中は熱気がむんむんしていた。",
        "Bên trong toa tàu điện chật ních người tỏa ra hơi nóng ngột ngạt.",
        "蒸し暑い, むっとする",
        "ひんやり, すーすーする"
    ),
    (
        "ねばねば",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Dính dính nhớp nháp / Độ dính kéo sợi",
        "粘り気があって、糸を引く様子。",
        "Trạng thái dính dính và kéo sợi đặc trưng của các món ăn như đậu nành lên men Natto, khoai mỡ.",
        "この納豆はねばねばしている。",
        "Món Natto này nhớt và dính dính kéo sợi.",
        "べたべた, 粘り気",
        "さらさら, かさかさ"
    ),
    (
        "ぬるぬる",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Trơn tuột / Nhớt nhúa",
        "表面が滑りやすく、つかみにくい様子。",
        "Trạng thái bề mặt có một lớp nhớt bôi trơn dễ trơn tuột khi chạm vào (như lươn, xà phòng).",
        "石鹸で手がぬるぬるする。",
        "Tay bị trơn tuột nhớt nhúa do dính xà phòng.",
        "滑りやすい, ヌルヌル",
        "かさかさ, ざらざら"
    ),
    (
        "ぴちぴち",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Tươi rói (cá nhảy) / Tràn đầy sức sống tươi trẻ",
        "元気がよく、生き生きしている様子。",
        "Tả cá vừa đánh bắt nhảy tanh tách tươi rói, hoặc làn da, dáng vẻ trẻ trung căng tràn sức sống tuổi thanh xuân.",
        "ぴちぴちした魚が網の中で跳ねている。",
        "Những con cá tươi rói đang nhảy tanh tách trong lưới.",
        "生き生き, 新鮮な",
        "しなびた, よぼよぼ"
    ),
    (
        "がさがさ",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Khô ráp / Nhám nhúa / Xột xoạt",
        "水分がなくて荒れている様子。また, 紙などが擦れ合う音。",
        "Da dẻ khô ráp, nứt nẻ thiếu độ ẩm; Hoặc âm thanh xột xoạt khi giấy tờ, lá khô chà xát nhau.",
        "冬になると, 手の皮膚ががさがさになる。",
        "Mỗi khi đông về, da tay tôi lại trở nên khô ráp.",
        "ざらざら, 荒れる",
        "つるつる, すべすべ"
    ),
    (
        "べたべた",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Bết dính / Nhớp nháp khó chịu",
        "粘り気のあるものが付着して、気持ち悪い様子。",
        "Cảm giác da dẻ dính dấp mồ hôi khó chịu hoặc đồ ngọt dính ra tay bết lại.",
        "汗でシャツが体にべたべた貼り付く。",
        "Mồ hôi làm chiếc áo sơ mi dính dấp bết chặt vào người.",
        "ねばねば, べったり",
        "さらさら, かさかさ"
    ),
    (
        "つるつる",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Trơn nhẵn / Láng mịn bóng bẩy",
        "表面が滑らかで、光っている様子。",
        "Bề mặt nhẵn bóng không tì vết (như làn da đẹp, mặt đá hoa cương) hoặc trơn trượt dễ ngã.",
        "温泉に入ったら、肌がつるつるになった。",
        "Tắm suối nước nóng xong, làn da tôi trở nên láng mịn trơn nhẵn.",
        "すべすべ, なめらか",
        "ざらざら, がさがさ"
    ),
    (
        "ごつごつ",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Gồ ghề / Thô ráp / Góc cạnh",
        "表面が硬くて平らでない様子。骨ばっている様子。",
        "Bề mặt đá gồ ghề thô ráp hoặc bàn tay xương xẩu góc cạnh, lao động nhiều.",
        "彼の父親は, 労働で鍛えられたごつごつした手をしている。",
        "Bố của anh ấy có bàn tay thô ráp, chai sạn vì lao động.",
        "ざらざら, 骨ばる",
        "なめらか, 柔らかい"
    ),

    # Nhóm 3: Hành Vi & Thái Độ (Behavior & Action) - 25 từ
    (
        "うっかり",
        "Hành Vi & Thái Độ",
        "Lơ đãng / Vô ý / Lỡ đễnh (quên đồ, làm sai)",
        "注意が足りなくて, ぼんやりしている様子。",
        "Bản thân thiếu chú ý nhất thời dẫn đến quên việc, nhầm lẫn ngoài ý muốn. Mang sắc thái tự trách nhẹ nhàng.",
        "電車の中にうっかり傘を忘れてきてしまった。",
        "Tôi lơ đãng quên khuấy mất cây dù trên tàu điện.",
        "うかつにも, 不注意",
        "しっかり, ちゃんと"
    ),
    (
        "しっかり",
        "Hành Vi & Thái Độ",
        "Chắc chắn / Vững vàng / Đáng tin cậy",
        "体制や構造が頑丈で揺るがない様子。考えや人柄が信用できる様子。",
        "Nắm chắc vật gì đó (nắm tay, trói chặt), hoặc thái độ/suy nghĩ chín chắn, đáng tin cậy. Dùng để nhắc nhở ai đó nghiêm túc.",
        "お姉ちゃんは弟の手をしっかり握って、道路を渡った。",
        "Người chị nắm chắc tay em trai dắt qua đường.",
        "ちゃんと, きちんと",
        "うっかり, ぼんやり"
    ),
    (
        "のんびり",
        "Hành Vi & Thái Độ",
        "Thong thả / Thong dong / Nhàn nhã thảnh thơi",
        "焦らず、ゆったりとくつろぐ様子。",
        "Hành động thong thả, không vội vàng, tận hưởng thời gian nghỉ ngơi thư thái mà không vướng bận lo nghĩ.",
        "週末は田舎の温泉でのんびり過ごしたい。",
        "Cuối tuần tôi muốn dành thời gian nghỉ ngơi thong thả ở suối nước nóng vùng quê.",
        "ゆったり, だらだら",
        "いそいそ, せかせか"
    ),
    (
        "うろうろ",
        "Hành Vi & Thái Độ",
        "Lảng vảng / Đi tới đi lui (không mục đích)",
        "目的もなく、あちこち歩き回る様子。",
        "Hành động đi qua đi lại một khu vực nào đó mà không có mục đích rõ ràng (dễ gây nghi ngờ cho cảnh sát).",
        "道に迷って、同じ場所をうろうろしてしまった。",
        "Do lạc đường nên tôi cứ đi quanh quẩn lảng vảng ở cùng một nơi.",
        "うろつく, 徘徊する",
        "じっとする, 立ち止まる"
    ),
    (
        "ぶらぶら",
        "Hành Vi & Thái Độ",
        "Đi loanh quanh dạo chơi / Nhàn rỗi đi dạo",
        "当てもなく、のんびり歩き回る様子。",
        "Hành vi đi dạo thong dong thư giãn, ngắm cảnh mà không vội vàng hay có lịch trình ép buộc.",
        "天気がいいので、近所の公園をぶらぶら散歩した。",
        "Thời tiết đẹp nên tôi đi dạo quanh công viên gần nhà.",
        "のんびり歩く, 散策",
        "さっさと走る, 急ぐ"
    ),
    (
        "よろよろ",
        "Hành Vi & Thái Độ",
        "Lảo đảo / Loạng choạng không vững",
        "足元がふらついて, しっかり歩けない様子。",
        "Dáng đi không vững vàng, bước thấp bước cao do say xỉn, già yếu hoặc kiệt sức.",
        "お年寄りが重い荷物を持って, よろよろ歩いている。",
        "Cụ già mang hành lý nặng bước đi loạng choạng.",
        "ふらふら, おぼつかない",
        "しゃんとする, しっかり歩く"
    ),
    (
        "とぼとぼ",
        "Hành Vi & Thái Độ",
        "Lầm lũi bước đi / Lê lết mệt mỏi",
        "元気なく、力なく歩く様子。",
        "Dáng vẻ bước đi chậm chạp, buồn bã, mệt mỏi sau khi gặp chuyện buồn hoặc kiệt sức.",
        "試験に落ちた彼は、とぼとぼと家路についた。",
        "Cậu ấy trượt kỳ thi nên lầm lũi bước đi trên con đường về nhà.",
        "力なく歩く, しょんぼり",
        "いそいそ, 軽快に進む"
    ),
    (
        "こっそり",
        "Hành Vi & Thái Độ",
        "Lén lút / Vụng trộm / Âm thầm",
        "人に知られないように、秘密裏に行う様子。",
        "Hành động che giấu người khác để làm việc gì đó một cách âm thầm, không muốn ai phát hiện.",
        "彼は夜中にこっそり台所でケーキを食べた。",
        "Anh ta lén lút ăn bánh ngọt trong bếp vào nửa đêm.",
        "こっそり, 秘密裏に",
        "堂々と, おおやけに"
    ),
    (
        "こっくり",
        "Hành Vi & Thái Độ",
        "Gật gù (ngủ gật) / Đồng ý gật đầu",
        "居眠りをして、頭が下に下がる様子。",
        "Đầu gật xuống khi ngủ gật trong giờ học hoặc cuộc họp; Hoặc cái gật đầu nhẹ để đồng ý.",
        "彼は授業中にこっくりこっくり居眠りをしている。",
        "Cậu ấy cứ ngủ gật gật gù gù trong giờ học.",
        "うとうと, 船を漕ぐ",
        "ぱっちり目が覚める"
    ),
    (
        "さっさと",
        "Hành Vi & Thái Độ",
        "Nhanh chóng / Mau lẹ (không chần chừ)",
        "ためらわずに、素早く物事を行う様子。",
        "Làm việc dứt khoát, nhanh gọn, không để phí thời gian hay chần chừ lề mề.",
        "無駄口を叩かずに、さっさと仕事を終わらせなさい。",
        "Đừng nói nhảm nữa, hãy nhanh chóng kết thúc công việc đi.",
        "てきぱき, 素早く",
        "ぐずぐず, のろのろ"
    ),
    (
        "せっせと",
        "Hành Vi & Thái Độ",
        "Cần mẫn / Chăm chỉ / Siêng năng",
        "休まずに、熱心に働き続ける様子。",
        "Hành động chăm chỉ làm lụng, tích lũy từng chút một không ngừng nghỉ hướng tới mục tiêu.",
        "彼女は将来のために、せっせと貯金をしている。",
        "Cô ấy đang cần mẫn tiết kiệm tiền tích lũy cho tương lai.",
        "こつこつ, 勤勉に",
        "怠ける, ぐずぐず"
    ),
    (
        "じっと",
        "Hành Vi & Thái Độ",
        "Chằm chằm (nhìn) / Đứng yên phăng phắc / Chịu đựng",
        "動かずに、同じ状態を保つ様子。",
        "Giữ nguyên tư thế không cử động (đứng yên) hoặc nhìn không chớp mắt (nhìn chằm chằm), chịu đựng đau đớn.",
        "彼は壁の写真をじっと見つめていた。",
        "Anh ấy nhìn chằm chằm vào bức ảnh trên tường.",
        "つくづく, 凝視する",
        "きょろきょろ, ちらちら"
    ),
    (
        "ぼんやり",
        "Hành Vi & Thái Độ",
        "Thơ thẩn / Ngẩn ngơ / Mơ hồ không rõ",
        "意識が集中せず、やる気がない様子。形がはっきりしない様子。",
        "Tâm trí lơ đãng ngồi không nghĩ ngợi gì; Hoặc phong cảnh mờ ảo khuất sau màn sương.",
        "彼は授業中、いつも窓の外をぼんやり眺めている。",
        "Trong giờ học, anh ấy toàn ngơ ngẩn nhìn ra ngoài cửa sổ.",
        "うっかり, おぼろげ",
        "はっきり, くっきり"
    ),
    (
        "ぐずぐず",
        "Hành Vi & Thái Độ",
        "Lề mề / Chần chừ / Kỳ kèo lười nhác",
        "動作が遅く、決断力がない様子。",
        "Hành động chậm chạp kéo dài thời gian, không dứt khoát đưa ra hành động hay quyết định.",
        "ぐずぐずしていると, 電車に遅れてしまうよ。",
        "Nếu cứ lề mề như vậy là muộn giờ tàu điện đấy.",
        "のろのろ, もたもた",
        "さっさと, てきぱき"
    ),
    (
        "ばたばた",
        "Hành Vi & Thái Độ",
        "Bận rộn tíu tít / Luống cuống dập dồn",
        "慌ただしく動き回る様子。",
        "Trạng thái bận rộn chạy đôn chạy đáo lo toan nhiều việc phát sinh cùng lúc.",
        "急な来客のせいで, 朝からばたばたしている。",
        "Có khách đột xuất ghé thăm nên từ sáng tôi đã cứ tíu tít luống cuống cả lên.",
        "慌ただしい, あたふた",
        "ゆったり, のんびり"
    ),
    (
        "ちょこちょこ",
        "Hành Vi & Thái Độ",
        "Lăng xăng / Đi thoăn thoắt / Thường xuyên",
        "小股で素早く歩く様子。また、頻繁に物事を行う様子。",
        "Bước đi nhỏ nhanh thoăn thoắt (như trẻ em hay động vật nhỏ); Hoặc hành động lặp lại nhiều lần trong khoảng thời gian ngắn.",
        "妹はちょこちょこと busy そうに動き回っている。",
        "Em gái tôi cứ lăng xăng đi lại trông thật bận rộn.",
        "ちょこまか, しばしば",
        "じっと, めったに〜ない"
    ),
    (
        "うとうと",
        "Hành Vi & Thái Độ",
        "Mơ màng / Thiu thiu ngủ / Ngủ gà ngủ gật",
        "浅い眠りに入りかける様子。",
        "Cơn buồn ngủ kéo đến nhẹ nhàng khiến mắt lim dim sắp chìm vào giấc ngủ ngắn (thường trên sofa hoặc xe buýt).",
        "テレビを見ているうちに、うとうとしてしまった。",
        "Đang xem tivi thì tôi ngủ thiu thiu lúc nào không biết.",
        "こっくり, とろとろ",
        "ぱっちり目が覚める"
    ),
    (
        "ぐうぐう",
        "Hành Vi & Thái Độ",
        "Ngủ khò khò / Kêu réo (bụng đói)",
        "深く眠って、いびきをかく音。また、お腹が鳴る音。",
        "Âm thanh ngủ say sưa phát ra tiếng ngáy; Hoặc tiếng bụng đói kêu réo ùng ục.",
        "弟は疲れていたのか、ベッドでぐうぐう寝ている。",
        "Em trai tôi chắc mệt quá nên đang nằm trên giường ngủ khò khò.",
        "ぐっすり, 熟睡",
        "目をぱちくりする"
    ),
    (
        "すらすら",
        "Hành Vi & Thái Độ",
        "Trôi chảy / Trơn tru / Vèo vèo",
        "滞りなく、順調に進む様子。",
        "Làm việc gì đó trôi chảy không bị vấp váp (như đọc bài trơn tru, làm toán vèo vèo).",
        "彼女は難しい質問にすらすらと答えた。",
        "Cô ấy trả lời câu hỏi khó trôi chảy vèo vèo.",
        "すらすらと, 流暢に",
        "つっかえる, どもる"
    ),
    (
        "ぺらぺら",
        "Hành Vi & Thái Độ",
        "Lưu loát (nói ngoại ngữ) / Mỏng dính / Nói hớt",
        "外国語を流暢に話す様子。また, 紙や服が薄い様子。",
        "Nói tiếng nước ngoài rất trôi chảy lưu loát; Hoặc quần áo mỏng manh rẻ tiền; Hoặc người ba hoa hay tiết lộ bí mật.",
        "彼は日本語がぺらぺらだ。",
        "Anh ấy nói tiếng Nhật trôi chảy lưu loát lắm.",
        "流暢に, ペラペラ",
        "無口, たどたどしい"
    ),
    (
        "ちらちら",
        "Hành Vi & Thái Độ",
        "Liếc nhìn / Lác đác (tuyết rơi) / Chập chờn",
        "小刻みに動いたり、見え隠れしたりする様子。",
        "Thỉnh thoảng liếc mắt nhìn trộm ai đó; Hoặc tuyết rơi lác đác bay trước mắt; Hoặc ánh đèn chập chờn.",
        "授業中、時計をちらちら見てしまう。",
        "Trong giờ học, tôi cứ thỉnh thoảng liếc nhìn đồng hồ.",
        "ちらりと見る",
        "じっと見る, 凝視"
    ),
    (
        "じろじろ",
        "Hành Vi & Thái Độ",
        "Nhìn soi mói / Nhìn chằm chằm thiếu lịch sự",
        "人の姿などを、不遠慮に見つめる様子。",
        "Nhìn người khác từ đầu đến chân một cách dò xét, thiếu tế nhị khiến họ cảm thấy khó chịu.",
        "人の顔をじろじろ見るのは失礼だ。",
        "Nhìn chằm chằm soi mói vào mặt người khác là bất lịch sự.",
        "じっと見る, 注視する",
        "ちらちら見る, チラ見"
    ),
    (
        "ぐんぐん",
        "Hành Vi & Thái Độ",
        "Vùn vụt / Nhanh như thổi",
        "勢いよく、急速に進む様子。",
        "Độ tăng trưởng, tiến bộ vượt bậc, tiến lên phía trước với tốc độ cực nhanh và mạnh mẽ.",
        "彼の日本語の実力は、この数ヶ月でぐんぐん伸びた。",
        "Năng lực tiếng Nhật của anh ấy đã tiến bộ vùn vụt trong vài tháng qua.",
        "急速に, どんどん",
        "じわじわ, そろそろ"
    ),
    (
        "てくてく",
        "Hành Vi & Thái Độ",
        "Đi bộ túc tắc / Cặm cụi đi bộ",
        "遠い距離を、ただひたすら歩く様子。",
        "Hành trình cặm cụi đi bộ quãng đường dài bằng chân một cách đều đặn, bền bỉ.",
        "駅まで20分、てくてく歩いて通っている。",
        "Tôi cặm cụi đi bộ túc tắc mất 20 phút để đi đến ga hàng ngày.",
        "とぼとぼ, 歩行する",
        "さっさと走る, 乗車する"
    ),
    (
        "きょろきょろ",
        "Hành Vi & Thái Độ",
        "Dáo dác nhìn quanh / Lơ ngơ ngó nghiêng",
        "落ち着きなく、あたりを見回す様子。",
        "Ngó nghiêng xung quanh một cách không yên lòng (như người lạ lạc đường hoặc tìm kiếm cái gì).",
        "知らない街に着いて, 不安そうにきょろきょろした。",
        "Đến một thành phố lạ, tôi cứ lơ ngơ dáo dác nhìn quanh đầy vẻ lo lắng.",
        "見回す, うろうろ",
        "じっと見つめる"
    ),

    # Nhóm 4: Mức Độ & Biến Đổi (Degree & Transformation) - 25 từ
    (
        "めっきり",
        "Mức Độ & Biến Đổi",
        "Rõ rét / Đáng kể (biến đổi theo thời gian)",
        "変化の様子が、目に見えてはっきり感じられる様子。",
        "Chỉ sự biến đổi trạng thái diễn ra nhanh và rõ nét tới mức cảm nhận rõ rệt (thời tiết thu lạnh đi, tóc bạc đi, khách khứa giảm đi).",
        "10月に入って、朝晩はめっきり涼しくなった。",
        "Sang tháng 10, sáng tối thời tiết mát mẻ lên trông thấy (rõ rệt).",
        "顕著に, 急激に",
        "じわじわ, 徐々に"
    ),
    (
        "すっかり",
        "Mức Độ & Biến Đổi",
        "Hoàn toàn / Sạch sành sanh",
        "残るものが全くない様子。完全にその状態になっている様子。",
        "Chỉ trạng thái biến đổi đã hoàn thành 100%, không còn gì sót lại (hoa nở rực rỡ hoàn toàn, quên sạch sành sanh, khỏi bệnh hoàn toàn).",
        "桜の花がすっかり咲いて、満開になった。",
        "Hoa anh đào đã nở hoàn toàn, đạt độ rực rỡ nhất.",
        "完全に, 全部",
        "ほとんど, すこし"
    ),
    (
        "ぎっしり",
        "Mức Độ & Biến Đổi",
        "Nét chặt / Đầy chật ních / San sát",
        "すき間なく詰まっている様子。",
        "Trạng thái đồ đạc hoặc con người được nhét đầy ắp, không còn một kẽ hở nào trống (lịch trình bận kín mít, vali xếp chật đồ).",
        "箱の中に本がぎっしり詰まっている。",
        "Trong thùng sách được xếp chật ních đầy ắp.",
        "みっしり, ぎゅうぎゅう",
        "がらがら, すかすか"
    ),
    (
        "ずらり",
        "Mức Độ & Biến Đổi",
        "Xếp hàng san sát / San sát tăm tắp",
        "多くのものが一列に並んでいる様子。",
        "Rất nhiều người hoặc vật được sắp xếp thẳng hàng lối, nối đuôi nhau kéo dài (như sách trên kệ, ô tô đỗ bên đường).",
        "本棚には専門書がずらりと並んでいる。",
        "Trên kệ sách xếp san sát tăm tắp toàn sách chuyên ngành.",
        "ずらっと, 整列して",
        "ばらばら, ぽつぽつ"
    ),
    (
        "たっぷり",
        "Mức Độ & Biến Đổi",
        "Dồi dào / Đầy ắp / Đầy tràn",
        "十分にあって, ゆとりのある様子。",
        "Lượng vật chất hoặc thời gian dư dả, thoải mái, quá đủ để đáp ứng nhu cầu.",
        "時間はたっぷりあるので, 急ぐ必要はない。",
        "Thời gian còn dồi dào lắm nên không cần phải vội đâu.",
        "たくさん, 豊富に",
        "すこし, 不足する"
    ),
    (
        "ばらばら",
        "Mức Độ & Biến Đổi",
        "Rời rạc / Rải rác / Mỗi người một ngả",
        "まとまりがなく, 別々になっている様子。",
        "Không có sự thống nhất, rời rạc rải rác mỗi người một nơi hoặc các mảnh vỡ vụn văng tung tóe.",
        "卒業後はクラスメイトがばらばらになった。",
        "Sau khi tốt nghiệp, các bạn cùng lớp mỗi người đi một ngả.",
        "ちりぢり, 別々に",
        "ずらり, 一致する"
    ),
    (
        "めちゃくちゃ",
        "Mức Độ & Biến Đổi",
        "Lộn xộn / Nát bét / Cực kỳ (tiếng lóng)",
        "秩序がなく、ひどい状態である様子。",
        "Tình trạng đổ nát, lộn xộn mất trật tự hoàn toàn; Hoặc được dùng như một phó từ cường điệu mang ý nghĩa 'cực kỳ/quá mức'.",
        "台風の後で、庭の植物がめちゃくちゃになってしまった。",
        "Sau cơn bão, cây cối trong vườn đã nát bét lộn xộn hết cả.",
        "ごちゃごちゃ, 滅茶苦茶",
        "整然とした, きちんとした"
    ),
    (
        "ごちゃごちゃ",
        "Mức Độ & Biến Đổi",
        "Bừa bộn / Lộn xộn lung tung",
        "整理されておらず, 乱雑に入り混じっている様子。",
        "Rất nhiều đồ vật vụn vặt bị xếp lẫn lộn bừa bãi không ngăn nắp trên mặt bàn hoặc trong tủ.",
        "机の上がごちゃごちゃしていて, 鍵が見つからない。",
        "Mặt bàn bừa bộn quá nên tôi mãi không tìm thấy chìa khóa.",
        "めちゃくちゃ, 乱雑",
        "すっきり, 整頓する"
    ),
    (
        "ぴかぴか",
        "Mức Độ & Biến Đổi",
        "Sáng loáng / Lấp lánh / Mới toanh",
        "磨かれて光り輝いている様子。",
        "Bề mặt đồ vật được chùi rửa sạch sẽ đến mức phản chiếu ánh sáng lấp lánh (như sàn nhà mới lau, giày da đánh bóng).",
        "靴をぴかぴかに磨いた。",
        "Tôi đã đánh bóng đôi giày của mình sáng loáng.",
        "きらきら, 輝く",
        "くすんだ, ぼろぼろ"
    ),
    (
        "がらがら",
        "Mức Độ & Biến Đổi",
        "Trống huơ trống hoác (tàu xe) / Tiếng ầm ầm đổ nát",
        "乗り物や場所が非常にすいている様子。",
        "Địa điểm, xe cộ cực kỳ vắng vẻ, hầu như không có người ngồi; Hoặc tiếng sạt lở ầm ầm.",
        "平日の昼間なので, 電車はがらがらだった。",
        "Vì là ban trưa ngày thường nên tàu điện trống huơ trống hoác.",
        "すいている, 空っぽ",
        "ぎっしり, 満員"
    ),
    (
        "どんより",
        "Mức Độ & Biến Đổi",
        "U ám / Xám xịt (thời tiết, ánh mắt)",
        "空気が濁って, 暗く沈んでいる様子。",
        "Trời nhiều mây mù xám xịt sắp mưa; Hoặc tâm trạng ủ rũ khiến ánh mắt mệt mỏi đờ đẫn.",
        "今日は朝から空がどんより曇っている。",
        "Hôm nay từ sáng bầu trời đã nhiều mây u ám xám xịt.",
        "曇る, 暗い",
        "からりと晴れる"
    ),
    (
        "しっとり",
        "Mức Độ & Biến Đổi",
        "Ẩm mịn / Dịu dàng / Yên ắng dễ chịu",
        "適度に湿り気があって、落ち着いた様子。",
        "Bề mặt ẩm mịn dễ chịu (da dẻ, bánh ngọt); Hoặc bầu không khí yên bình tĩnh lặng thấm đẫm chất thơ.",
        "化粧水のおかげで、肌がしっとりしてきた。",
        "Nhờ có nước hoa hồng nên da tôi đã trở nên ẩm mịn.",
        "しっとりする, 潤う",
        "からから, かさかさ"
    ),
    (
        "からり",
        "Mức Độ & Biến Đổi",
        "Khô ráo thoáng đãng / Cởi mở dứt khoát",
        "湿気がなく、さわやかに晴れ渡る様子。",
        "Thời tiết khô ráo, mây mù tan biến nhường chỗ cho nắng ấm; Hoặc tính cách thẳng thắn cởi mở không để bụng.",
        "雨が上がって、空がからりと晴れた。",
        "Cơn mưa tạnh hẳn, bầu trời quang đãng khô ráo.",
        "からっと晴れる, カラリ",
        "じめじめ, どんより"
    ),
    (
        "じっとり",
        "Mức Độ & Biến Đổi",
        "Đầm đìa / Ẩm ướt khó chịu (mồ hôi)",
        "湿気が多くて、じとじと濡れている様子。",
        "Mức độ ẩm ướt, nhớp nháp khó chịu do mồ hôi đẫm ra quần áo hoặc không khí phòng quá bí bách.",
        "暑さのせいで、背中にじっとり汗をかいた。",
        "Cái nóng làm lưng tôi đổ mồ hôi đầm đìa khó chịu.",
        "じめじめ, 湿る",
        "からり, かさかさ"
    ),
    (
        "どっさり",
        "Mức Độ & Biến Đổi",
        "Nhiều đống lớn / Trĩu nặng",
        "分量が非常に多い様子。",
        "Lượng quà cáp, bài tập hoặc tiền bạc chất cao như núi, trĩu nặng.",
        "お土産にリンゴをどっさりもらった。",
        "Tôi được tặng nhiều táo chất thành cả đống lớn làm quà.",
        "たっぷり, 大量に",
        "すこし, わずか"
    ),
    (
        "びっしょり",
        "Mức Độ & Biến Đổi",
        "Ướt sũng / Ướt đẫm",
        "ひどく濡れている様子。",
        "Cơ thể hoặc quần áo bị thấm đẫm nước mưa hoặc mồ hôi ướt sũng hoàn toàn.",
        "突然の雨で、服がびっしょり濡れてしまった。",
        "Cơn mưa bất chợt khiến quần áo của tôi bị ướt sũng hoàn toàn.",
        "びしょ濡れ, ずぶ濡れ",
        "からから, 乾く"
    ),
    (
        "ぼろぼろ",
        "Mức Độ & Biến Đổi",
        "Rách nát tơi tả / Lã chã (lệ rơi) / Rệu rã",
        "ひどく傷んで壊れかかっている様子。粒がこぼれ落ちる様子。",
        "Đồ vật rách nát, nhà cũ nát; Hoặc nước mắt rơi lã chã từng hạt; Hoặc tinh thần cơ thể rệu rã kiệt quệ.",
        "長年使い込んだ辞書がぼろぼろになった。",
        "Cuốn từ điển dùng nhiều năm đã rách nát tơi tả.",
        "よれよれ, 崩壊する",
        "新品, ぴかぴか"
    ),
    (
        "ざらざら",
        "Mức Độ & Biến Đổi",
        "Nhám ráp / Đầy cát sạn",
        "表面が荒れていて、滑らかでない様子。",
        "Bề mặt thô ráp dính nhiều cát sạn hoặc da dẻ thô ráp không mịn màng.",
        "砂浜を歩いたので, 足の裏がざらざらする。",
        "Đi dạo trên bãi cát làm lòng bàn chân tôi bám đầy cát ráp ráp.",
        "がさがさ, 荒い",
        "つるつる, すべすべ"
    ),
    (
        "まるまる",
        "Mức Độ & Biến Đổi",
        "Tròn trịa mập mạp / Tròn vẹn toàn bộ",
        "丸々と太っている様子。全体がそのまま残っている様子。",
        "Em bé hoặc thú cưng mập mạp tròn trịa dễ thương; Hoặc thời gian, tiền bạc còn nguyên vẹn chưa sứt mẻ tí nào.",
        "まるまると太った可愛い赤ちゃんですね。",
        "Một em bé mập mạp tròn trịa dễ thương quá nhỉ.",
        "ぷくぷく, すっかり",
        "やせ細る, わずか"
    ),
    (
        "じわじわ",
        "Mức Độ & Biến Đổi",
        "Từ từ thấm dần / Tác động chậm chắc",
        "少しずつ、確実に変化が進む様子。",
        "Sự thay đổi hoặc tác động diễn ra rất chậm rãi từng chút một nhưng mang lại hiệu quả rõ rệt lâu dài.",
        "この薬の効果がじわじわと現れてきた。",
        "Hiệu quả của thuốc này đã bắt đầu từ từ thấm dần ra.",
        "じわっと, 徐々に",
        "どんどん, 急激に"
    ),
    (
        "どんどん",
        "Mức Độ & Biến Đổi",
        "Nhanh chóng liên tục / Dồn dập",
        "物事が滞りなく、勢いよく進む様子。",
        "Hành động hoặc sự việc tiến triển cực kỳ thuận lợi, nhanh chóng dồn dập không có rào cản.",
        "アイデアがどんどん湧いてくる。",
        "Ý tưởng cứ nhanh chóng tuôn ra dồn dập liên tục.",
        "ぐんぐん, 急速に",
        "じわじわ, とぼとぼ"
    ),
    (
        "ますます",
        "Mức Độ & Biến Đổi",
        "Càng ngày càng / Tăng tiến",
        "前よりも程度が強くなる様子。",
        "Độ mạnh hoặc mức độ của trạng thái gia tăng liên tục so với thời điểm trước đó.",
        "台風が近づいて, 風がますます強くなってきた。",
        "Cơn bão đang đến gần, gió càng ngày càng mạnh lên.",
        "いよいよ, さらに",
        "だんだん衰える"
    ),
    (
        "いよいよ",
        "Mức Độ & Biến Đổi",
        "Cuối cùng thì / Ngày càng tăng tiến mức độ",
        "ある事態が迫ってくる様子。程度が一層強まる様子。",
        "Thời khắc mong đợi hoặc một sự kiện trọng đại cuối cùng cũng đã sát nút; Hoặc mức độ nghiêm trọng gia tăng.",
        "いよいよ明日は大学入試の合格発表だ。",
        "Cuối cùng thì ngày mai cũng là ngày công bố kết quả thi đại học.",
        "ついに, ますます",
        "はじめは"
    ),
    (
        "そろそろ",
        "Mức Độ & Biến Đổi",
        "Sắp sửa đến lúc / Chuẩn bị",
        "ある時間や状態になりかけている様子。",
        "Đã đến lúc cần thực hiện một hành động nào đó (như chuẩn bị đi ngủ, chuẩn bị ra về).",
        "もう11時なので, そろそろ寝る時間だ。",
        "Đã 11 giờ rồi, chuẩn bị đến giờ đi ngủ thôi.",
        "まもなく, やがて",
        "まだまだ"
    ),
    (
        "だんだん",
        "Mức Độ & Biến Đổi",
        "Dần dần / Từng bước một",
        "時間の経過とともに、少しずつ変化する様子。",
        "Sự biến đổi trạng thái theo thời gian một cách chậm rãi, có trình tự tự nhiên.",
        "春になって、だんだん暖かくなってきた。",
        "Xuân về, thời tiết dần dần trở nên ấm áp hơn.",
        "次第に, 徐々に",
        "急激に, 突如"
    )
]

# Các từ vựng đã được tạo hình ảnh AI minh họa thực tế
ILLUSTRATED_WORDS = {
    "すっきり": "sukkiri.png",
    "がっかり": "gakkari.png",
    "さっぱり": "sappari.png",
    "ぴったり": "pittari.png",
    "うっかり": "ukkari.png",
    "しっかり": "shikkari.png",
    "めっきり": "mekkiri.png",
    "すっかり": "sukkari.png",
    "いらいら": "iraira.png",
    "どきどき": "dokidoki.png",
    "のんびり": "nonbiri.png",
    "ぐっすり": "gussuri.png",
    "わくわく": "wakuwaku.png",
    "はらはら": "harahara.png",
    "うっとり": "uttori.png",
    "しょんぼり": "shonbori.png",
    "びくびく": "bikubiku.png"
}

def generate_markdown():
    output_path = "/Users/tuyennq1001/htdocs/jlpt-n1/goi/goi_onomatopoeia.md"
    
def format_word_links(text, all_words_map):
    if not text:
        return ""
    parts = [p.strip() for p in text.split(",")]
    result_parts = []
    for part in parts:
        if part in all_words_map:
            num = all_words_map[part]
            anchor = f"{num}-{part}"
            result_parts.append(f"[{part}](#{anchor})")
        else:
            result_parts.append(part)
    return ", ".join(result_parts)

def generate_markdown():
    output_path = "/Users/tuyennq1001/htdocs/jlpt-n1/goi/goi_onomatopoeia.md"
    
    # Tạo bản đồ từ vựng -> số thứ tự tuyệt đối
    all_words_map = {item[0]: idx for idx, item in enumerate(words_data, 1)}
    
    # Gom nhóm dữ liệu
    groups = {}
    for idx, item in enumerate(words_data, 1):
        _, group, _, _, _, _, _, _, _ = item
        if group not in groups:
            groups[group] = []
        groups[group].append((idx, item))
        
    markdown_content = []
    markdown_content.append("# 🎨 Từ Láy & Phó Từ Tượng Hình Tiếng Nhật (Goi - Onomatopoeia)")
    markdown_content.append("")
    markdown_content.append("Sổ tay trực quan tổng hợp 100 từ láy tượng thanh, tượng hình (擬音語・擬態語) và phó từ thường gặp trong JLPT. Các từ được phân nhóm ý nghĩa rõ ràng giúp bạn dễ dàng so sánh và học tập hiệu quả.")
    markdown_content.append("")
    markdown_content.append("---")
    markdown_content.append("")
    
    # Thứ tự phân nhóm thủ công để số thứ tự đi từ 1 đến 100
    ordered_groups = [
        "Trạng Thái Tinh Thần & Cảm Xúc",
        "Cảm Giác Cơ Thể & Thể Chất",
        "Hành Vi & Thái Độ",
        "Mức Độ & Biến Đổi"
    ]
    
    for group_name in ordered_groups:
        if group_name not in groups:
            continue
            
        markdown_content.append(f"## 📌 Phân Nhóm: {group_name}")
        markdown_content.append("")
        
        for num, item in groups[group_name]:
            word, _, meaning, jp_def, nuance, ex_jp, ex_vi, syn, ant = item
            
            # Định dạng các từ đồng nghĩa/trái nghĩa thành link nếu có trong file
            formatted_syn = format_word_links(syn, all_words_map)
            formatted_ant = format_word_links(ant, all_words_map)
            
            markdown_content.append(f'### <span id="{num}-{word}"></span>{num}. {word}')
            markdown_content.append(f"* **Ý nghĩa:** {meaning}")
            markdown_content.append("")
            
            # Ảnh minh họa (chỉ chèn ảnh nếu đã có tệp ảnh)
            if word in ILLUSTRATED_WORDS:
                img_name = ILLUSTRATED_WORDS[word]
                markdown_content.append(f'<img src="images/onomatopoeia/{img_name}" width="300" />')
            else:
                markdown_content.append("*(Ảnh minh họa cho từ này sẽ được bổ sung ở các đợt học sau)*")
            markdown_content.append("")
            
            # Khối thông tin (Định nghĩa, sắc thái, đồng nghĩa, trái nghĩa) - Dùng [!NOTE] của GitHub
            markdown_content.append("> [!NOTE]")
            markdown_content.append("> **Định nghĩa & Sắc thái**")
            markdown_content.append(f"> * **日本語:** {jp_def}")
            markdown_content.append(f"> * **Sắc thái:** {nuance}")
            markdown_content.append(f"> * **Từ đồng nghĩa:** {formatted_syn}")
            markdown_content.append(f"> * **Từ trái nghĩa:** {formatted_ant}")
            markdown_content.append("")
            
            # Khối ví dụ - Dùng [!TIP] của GitHub
            markdown_content.append("> [!TIP]")
            markdown_content.append("> **Ví dụ thực tế (例文)**")
            markdown_content.append(f"> * {ex_jp}")
            markdown_content.append(f">   * *{ex_vi}*")
            markdown_content.append("")
            markdown_content.append("---")
            markdown_content.append("")
            
    # Ghi nội dung ra file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(markdown_content))
    print("XUẤT FILE THÀNH CÔNG!")

if __name__ == "__main__":
    generate_markdown()
