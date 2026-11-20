# ai-design-studio

Một skill cho Claude, chạy quy trình thiết kế kiểu studio để giao diện do AI dựng bớt "na ná AI":
1. Dùng chuỗi ngẫu nhiên (seed) để có hướng thiết kế khác nhau thật.
2. Viết brief tham vọng dựa trên gu của người dùng.
3. Cho một critic độc lập chấm chỉ qua ảnh chụp màn hình, lặp nhiều vòng.
4. Cắt bớt mạnh tay.
5. Rà các dấu hiệu "AI làm".

## Cài đặt
Chép thư mục này vào `~/.claude/skills/ai-design-studio/` (Claude Code), hoặc tải lên dưới dạng skill trong claude.ai.

```
SKILL.md              quy trình (tiếng Anh)
references/critic.md  prompt cho critic
references/ai-tells.md danh sách dấu hiệu "AI làm"
references/motion.md  bản đồ kỹ thuật chuyển động (Technique 5)
scripts/draw.py       bốc ngẫu nhiên 1 dòng: key message ở Stage 0 (auto), concept ở bước concept (auto)
```

## Thay đổi ngày 2026-11-20
Đổi `SKILL.md`, thêm `scripts/draw.py`:
1. **Thêm Stage 0 (ý tưởng).** AI liệt kê 8 cách hiểu đề. Chế độ thường: người dùng chọn. Chế độ auto: **bắt buộc bốc bằng script** `scripts/draw.py`, và script **bốc bằng seed**. Script tự tạo một seed string ngẫu nhiên (chữ + số, 48 ký tự), băm SHA-256, chia lấy dư cho số ý tưởng để ra dòng được chọn. AI không chọn, nên không lái được. Cùng seed và cùng danh sách thì luôn ra cùng một ý, nên ai có seed trong log cũng chạy lại được bằng `--seed` để kiểm. Nếu đề đã rõ (người dùng đưa sẵn một ý cụ thể) thì bỏ qua Stage 0, đi thẳng sang bước seed.
2. **Hai chế độ.** Thường: người dùng chọn ở Stage 0 và ở các checkpoint. Auto: AI tự đi hết, tự chọn và ghi lý do.
3. **Mặc định ra 3 hướng** (trước đây là 3–4).
4. **Hỏi làm rõ khi cần.** Ở chế độ thường, hỏi khi đề chưa rõ. Ở chế độ auto, không hỏi mà ghi lại giả định.

5. **Mặc định chạy chế độ thường.** Chỉ chạy auto khi người dùng nói rõ là muốn chạy tự động. Trước khi bắt đầu, AI giải thích quy trình và các điểm người dùng tham gia: Stage 0, dò gu, Checkpoint 1–3. Khi chạy auto, AI phải báo trước: *chạy tự động không đảm bảo ra kết quả tốt, chỉ nên dùng khi test skill.* Lý do (Le Bach): giá trị của skill nằm ở gu của người; auto chỉ để test.
6. **Stage 1 chạy theo thứ tự: dò gu trước, seed sau.** Mỗi hướng = 1 "thế giới" người dùng thích + 1 seed riêng. Thế giới đặt tầm nhìn, seed lo phần thế giới để ngỏ (màu, bố cục, chữ, điều hướng, chuyển động, tương tác). Người dùng thích ít hơn 3 thế giới thì các hướng còn lại chỉ chạy theo seed. Người dùng đã có sẵn thế giới thì cả 3 hướng dùng thế giới đó, bỏ qua bước dò gu. Lý do: trước đây skill không nói brief viết trước hay sau khi có hướng, nên mỗi lần chạy làm một kiểu. Cách này vừa giữ gu của người, vừa giữ các hướng khác nhau.

7. **Hướng dẫn người dùng ở từng điểm dừng.** Ở Stage 0, bước dò gu và Checkpoint 1–3, AI phải nói rõ 4 điều: người dùng đang xem gì, AI cần gì, trả lời thế nào (kèm câu trả lời mẫu), và bước tiếp theo là gì. Mỗi điểm dừng có sẵn một câu *Guide:* mẫu, AI nói lại bằng ngôn ngữ của người dùng.

8. **Technique 4 và 5: giữ ý chính của bài gốc, thêm nguyên tắc ngắn.** Lý do (Le Bach): các model hiện đã tạo được asset, 3D và animation, nên skill cần nói rõ điều này. Nhưng phải viết thành nguyên tắc, không liệt kê công cụ hay định dạng (danh sách lỗi thời nhanh, và model dễ coi đó là việc phải làm), và phải giữ ý chính của bài viết gốc.
   - **Giữ từ bản gốc:** CSS trang trí là dấu hiệu AI rõ nhất; dùng ảnh tạo ra (kèm shader hoặc 3D) khi nó thêm chất liệu, không gian, cảm xúc hay trạng thái; mỗi asset phải có việc; dùng công cụ tạo nào có sẵn; xem từng khung hình trong trình duyệt; chỉ dùng chuyển động khi thật sự tốt hơn; 2 cách dùng video đã kiểm chứng (clip lặp tách nền, clip chuyển trạng thái A → B); dùng aggregator như fal.ai.
   - **Thêm:** model nay tạo được cả 3D và animation; cả trang chung một ngôn ngữ hình ảnh; chọn dạng chuyển động nhẹ nhất; chuyển động phải mang ý nghĩa; trang vẫn dùng được trong lúc asset nặng đang tải.
9. **Bỏ luật hỏi trước khi tiêu tiền** (Le Bach yêu cầu). Các câu "hỏi trước lần gọi trả phí đầu tiên" ở Technique 4 và "luôn báo chi phí trước" ở Technique 5 cũng được bỏ cho khớp. Checkpoint 2 và 3 vẫn báo số tiền đã tiêu.

10. **Mọi chuyển động và hình ảnh đến từ concept** (Le Bach, sau lần test Kobe ra trang phẳng: 13 ảnh tĩnh, không video, không 3D, chỉ 2 hiệu ứng đổi màu).
   - **Luật chung mới:** mọi animation, transition, graphic phải đến từ thế giới của trang. Bắt đầu từ "động từ" của thế giới (rót, áp chảo, mở cổng, gió lùa cỏ) để làm transition; parallax trang trí là dạng yếu nhất. Mỗi chuyển động vẫn phải có việc, không chiếm quyền cuộn trang. Trang tĩnh không còn là lựa chọn an toàn mặc định. Không làm âm thanh (Le Bach bỏ).
   - **Dò gu:** danh sách sinh từ ý ở Stage 0 và phải trải qua nhiều hình thức trải nghiệm (cuộn kể chuyện, không gian 3D, công cụ, điện ảnh, trò chơi, khám phá phi tuyến); tối đa 3 ý là "trang cuộn tĩnh giả đồ in". Lý do: ở test Kobe cả 10 ý đều là đồ in giấy.
   - **Bản nháp Stage 1** phải có chuyển động chủ đạo và ít nhất một transition.
   - **Technique 5:** đảo mặc định. Viết "motion score" trước khi build; bỏ motion phải ghi lý do ở Checkpoint 2. Thêm `references/motion.md` (bản đồ kỹ thuật: GSAP/ScrollTrigger, CSS scroll-driven, View Transitions, three.js/WebGPU, shader, particle, Rive/Lottie, video trong suốt, quy trình asset AI) và luật kỹ thuật (reduced-motion, transform/opacity, nút dừng cho vòng lặp > 5 giây, không scrolljacking).
   - **Không bắt buộc dùng kỹ thuật cao khi build** (Le Bach): thực thi tuỳ công cụ và thời gian, nhưng chuyển động phải được nghĩ kỹ và trình bày cho người dùng: demo trong trang nếu được (CSS/SVG đơn giản cũng được), nếu không thì motion score + storyboard khung hình. Ở Checkpoint 1 mỗi hướng kèm ý tưởng chuyển động. Lý do: không phải lúc nào user cũng có công cụ tạo asset trong Claude (ChatGPT, Gemini thì có).
   - **Critic** xem thêm dải khung hình của chuyển động và chấm "chuyển động có đến từ thế giới không". Lý do: critic chỉ xem ảnh tĩnh nên thưởng cho trang tĩnh (2 vòng đều 6/10 ở test Kobe).
   - **Technique 6** cắt chuyển động chung chung, giữ chuyển động của thế giới. **ai-tells.md** thêm 3 dấu hiệu chuyển động.
   - Căn cứ: research "Chuyển động theo concept trang" (lý thuyết congruence, environmental storytelling, nguyên tắc motion, rủi ro seductive details / parallax / tiếp cận, ví dụ site đoạt giải). Chưa có nghiên cứu nào so trực tiếp motion theo concept với motion chung chung trên web; đây là heuristic có lý thuyết đỡ.

11. **Tách rõ ý tưởng (Stage 0) và gu/thế giới (dò gu)** (Le Bach). Ở lần test Kobe, 8 cách hiểu đề lẫn cả hình thức ("trang như giấy chứng nhận", "thanh trượt BMS", "mỗi section là một mốc thời gian"), nên người dùng phải chọn hình thức 2 lần. Giờ Stage 0 chỉ trả lời 3 câu: trang bán hoặc hứa gì, cho ai, khách cần tin điều gì để hành động; cấm mọi từ về bố cục, hình ảnh, ẩn dụ cho trang, cấu trúc, điều hướng, chuyển động, tương tác. Dò gu thì sinh các thế giới khác nhau cho cùng một thông điệp đã chọn, không đổi thông điệp.

12. **3 rule từ báo cáo research "Chuyển động theo concept trang"** (Le Bach đồng ý thêm):
   - **Câu tự kiểm** (Technique 6 và critic): "tắt chuyển động này đi thì khách mất gì?" Không mất gì thì cắt; mất thông tin thì giữ; chỉ mất cảm giác về thế giới thì giữ nếu nằm trong hạn mức. Lý do: rủi ro nằm ở chuyển động không có việc (seductive details: Rey 2012, Sundararajan & Adesope 2020), không nằm ở chủ đề.
   - **Hạn mức khoảnh khắc nổi bật:** một ở hero, một ở mỗi lần chuyển chương lớn, một ở hành động chính; còn lại là chuyển động nhẹ, có chức năng. Lý do: IBM Carbon dành motion "expressive" cho khoảnh khắc quan trọng; Sklar "avoid overload".
   - **Mạch truyện tối thiểu:** trang là một hành trình qua các section, không chỉ khoác chủ đề. Lý do: hiệu ứng "nhập vai" (narrative transportation, van Laer 2014) cần có câu chuyện.

13. **Người dựng đọc `references/ai-tells.md` trước khi dựng ở Stage 1** (Le Bach đồng ý). Trước đây danh sách dấu hiệu "AI làm" chỉ dùng ở Technique 7 (Stage 3), nên bản nháp cứ theo pattern quen rồi cuối quy trình mới sửa.

14. **Technique 4 chỉ ghi "dùng công cụ tạo asset mà model có"** (Le Bach). Bỏ phần viết sẵn prompt cho ChatGPT/Gemini khi không có công cụ, và bỏ rule kiểm giấy phép asset.

15. **Đổi tên theo thuật ngữ chuyên ngành** (Le Bach): dùng đúng từ của agency để người dùng dễ hiểu.
   - Stage 0 "Idea" → **Key message** (thông điệp chính: trang nói gì).
   - "Taste pass" (dò gu) → **concept step**; "world" → **concept** (creative concept: trang nói điều đó thế nào — hình ảnh, cấu trúc, chuyển động, tương tác). Technique 2 đổi tên thành "Creative concept, steered by the user's taste". Mỗi lựa chọn kèm ảnh moodboard nếu tạo được ảnh.
   - Giữ **design direction** cho 3 hướng dựng ở Stage 1 (mỗi hướng = 1 concept + 1 seed).
   - Đổi cả trong `references/` (critic, ai-tells, motion).

16. **Kỹ thuật ra concept táo bạo trong bước concept** (Le Bach: "Đưa kỹ thuật vào phần prompt concept"). Thêm vào Technique 2, bước 1 (đây là cách nghĩ, không phải nguồn để chép):
   - **Cấm ý hiển nhiên trước:** viết 5–10 concept mà ai cũng nghĩ ra, rồi không dùng. Thực hành phổ biến, không có tên chuẩn.
   - **Mượn từ lĩnh vực khác:** nghĩ xem thông điệp sẽ thế nào nếu nằm ở một thế giới xa chủ đề, chỉ giữ phần vẫn nói đúng thông điệp. Gốc: lateral thinking của de Bono (*Lateral Thinking*, 1970) và bisociation của Koestler (*The Act of Creation*, 1964). **Không dùng danh sách lĩnh vực có sẵn, không bắt buộc số lượng** (Le Bach: AI bám keyword trong reference rồi làm theo đó, không nghĩ thêm). Bản trước có `references/domains.txt` và bước bốc lĩnh vực; đã bỏ khỏi skill.
   - **Đổi thang đo, góc nhìn:** chữ M (Magnify/Minify) của SCAMPER (Eberle, 1971, dựa trên checklist của Osborn).
   - **Mỗi concept có vai của khách, động từ, luật thế giới:** mình ghép từ thiết kế game (player fantasy), không phải kỹ thuật kinh điển.
   - **Ít nhất 3/10 ý "nghe như không ổn"** (trước là "a few"): nguyên tắc hoãn phán xét của Osborn (*Applied Imagination*, 1953); con số 3 là mình đặt.
   - **Gắn nhãn mỗi dòng:** mức táo bạo (safe/bold/wild) × mức bám thông điệp (strong/weak).
   - Nguồn gốc các kỹ thuật ghi theo hiểu biết của Claude, chưa tra lại.

17. **Concept phải tả trải nghiệm, không tả bố cục** (từ lần test Kobe; session chạy test tự nhận brief của mình "là mô tả bố cục, chưa phải brief tham vọng"). Thêm vào Technique 2, bước 2–3:
   - Người dùng chỉ trả lời số ("7 và 6") thì hỏi lại một lần là thích gì ở mỗi ý. Lý do: concept phải viết từ ghi chú của người dùng; ở test Kobe AI không hỏi nên tự lấp chỗ trống bằng ý an toàn.
   - Concept nói khách cảm thấy gì, thấy gì chuyển động, cảnh thay đổi ra sao, cùng vai/động từ/luật.
   - Có **ít nhất 1 yêu cầu khó** bắt bản dựng phải làm được, không chỉ có danh sách "tránh". Không tự cấm chuyển động ("tĩnh, chậm") trừ khi người dùng muốn. Lý do: brief của hướng B ở test Kobe ghi "Tĩnh, chậm", tự cấm chuyển động từ đầu.
   - Thêm 1 cặp ví dụ: brief "đồng hồ một đêm" bản tả bố cục và bản viết lại thành concept (một cảnh quay từ ghế số 7).
   - **Chế độ auto: script bốc 3 concept** từ 10 ý AI đã liệt kê (`process/concepts.txt`, dùng lại `scripts/draw.py`, ghi seed), AI không tự chọn (Le Bach). Lý do: giống Stage 0, AI chọn từ danh sách của chính nó thì hội tụ về ý an toàn. Mọi concept trong danh sách phải liên quan đến thông điệp và chủ đề.

18. **Bỏ "Cấm ý hiển nhiên trước"** ở bước concept (Le Bach: "Concept -> Không cần bỏ 8 ý ai cũng nghĩ ra"). Các kỹ thuật còn lại của mục 16 giữ nguyên.

19. **Thêm Stage 0.5 · Content và IA map** (Le Bach, sau lần test điện gió: "sau stage 0 chưa có define content và IA"; "có content thì bước làm concept mới define IA được"). Thứ tự mới: key message → content → concept (concept định IA) → seed → dựng.
   - **Stage 0.5 · Content** (`process/content.md`, dùng chung cho mọi hướng): câu hỏi người đọc mang tới, xếp theo ưu tiên, đánh dấu bắt buộc / nên có; câu trả lời bằng sự thật, chưa có thì để placeholder lộ rõ, không bịa; người đọc cần **cảm thấy gì** khi xem xong; một hành động chính. Không có thứ tự section, bố cục hay hình thức. Chế độ thường: người dùng sửa và bổ sung. Chế độ auto: ghi giả định.
   - **IA map** cho mỗi concept: bảng "nội dung → nằm ở đâu trên đường đi của concept". Câu hỏi bắt buộc phải có chỗ rõ ràng; concept quyết định thứ tự. Truyền IA map cho người dựng.
   - **Sau mỗi vòng critic**, AI tự đối chiếu trang với IA map và dòng "cảm thấy gì" (critic không được xem). Câu hỏi bắt buộc mà trang không còn trả lời rõ thì tính là một lỗ hổng, xếp cùng các lỗ hổng lớn của critic. **Technique 6** không được cắt chỗ duy nhất trả lời một câu hỏi bắt buộc.
   - Lý do: ở test điện gió, skill nhảy từ key message (một câu) sang concept. Mỗi agent dựng tự đặt cấu trúc trang, và critic chê hướng được chọn là "template tuyển dụng khoác áo concept". Nếu chốt IA trước concept thì mọi concept ra cùng một khung, nên IA để concept quyết; còn dòng "cảm thấy gì" là để chấm độ hợp với người đọc, thứ critic không chấm.

20. **Đánh nhãn riêng cho hai danh sách** (sau lần test điện gió). Key message đánh K1–K8, concept đánh C1–C10. Nếu người dùng chỉ nói số ("ý tưởng 8") mà số đó có ở cả hai danh sách, phải hỏi lại trước khi tiêu gì cho nó (dựng trang, chạy critic, tạo asset). `scripts/draw.py` bỏ được nhãn K/C khi bốc. Lý do: người dùng muốn thử key message #8, AI hiểu thành concept #8 và dựng nguyên một hướng, tốn một lượt dựng, một lượt critic và khoảng 945 credit ảnh.

21. **Giọng văn ở Stage 0.5, viết copy sau khi có UI** (Le Bach: copy sau ai-tells "vẫn cụt lủn, khó hiểu, thiếu mạch và văn phong phù hợp"; "viết copy nên làm sau khi có UI… nếu viết trước thì UI bị fix cứng").
   - **Stage 0.5 thêm giọng văn:** ai nói với ai, 3 từ cho giọng, 2–3 câu mẫu, từ vựng nên dùng và nên tránh. Chỉ chốt giọng, không chốt độ dài.
   - **Lúc dựng:** agent viết chữ tạm theo giọng đó, thành câu nối nhau, không dán từng mẩu sự thật; độ dài theo UI.
   - **Thêm bước viết copy ở đầu Stage 3**, sau vòng critic (UI đã ổn định): viết lại toàn bộ chữ thành một mạch theo đường đi của concept, khớp chỗ trống thật; được chỉnh UI một chút nếu cần. Một agent mới chỉ đọc chữ chấm: đọc to có trôi, có câu cụt, đoạn sau nối đoạn trước, giọng có hợp. Chuẩn chấm: skill `anti-ai-slop-writing` hoặc `humanizer` nếu có. Thứ tự Stage 3: viết copy → cắt giảm → ai-tells → người dùng viết dòng chính.
   - Lý do: ai-tells chỉ gỡ câu sáo, không tạo mạch; content.md là bảng sự thật nên agent dán thành câu rời; critic chỉ xem ảnh, không ai đọc chữ từ đầu tới cuối.

Lý do thêm Stage 0: ở các test, ý tưởng là chỗ AI hội tụ mạnh nhất. Khi để AI tự chọn, 5/5 lần ra cùng một cách hiểu. Khi code bốc từ danh sách AI tự viết, ra 5 ý khác nhau trong 5 lần.

## Thay đổi ở bản 2026-11-07
So với bản trước, chỉ có 4 thay đổi trong `SKILL.md`. `references/` giữ nguyên.

1. **Đọc seed theo prompt của Lenny.** Technique 1 dùng chuỗi chữ + số (thay cho hex). AI tìm "subpatterns, special numbers, anything that inspires you", thay cho câu cũ chỉ AI nhìn vào ký tự lặp và tần suất chữ.
2. **Đọc seed để ý cả tương tác.** Bước 2 thêm `navigation, motion, interaction` bên cạnh màu, bố cục, chữ.
3. **Tự dò gu khi không có người.** Ở chế độ tự chạy, AI không bỏ qua vòng dò gu. Nó tự phản ứng từ góc nhìn người xem trang, viết brief từ đó và ghi rõ đây là phản ứng của AI.
4. **Chạy hết trong một lượt.** Đợi critic (subagent) trả kết quả rồi làm tiếp, không dừng giữa chừng.

## Vì sao đổi
Rút ra từ các lần chạy thử nội bộ, cùng một đề (website công ty xây nhà, keyword "uy tín"):
- **Đổi 1:** 5 lượt mỗi bên, mỗi lượt 3 hướng. Câu đọc seed cũ cho 2/15 hướng thoát khỏi các khuôn quen (bản vẽ mặt cắt, tường gạch, con dấu). Câu của Lenny cho 6–7/15.
- **Đổi 3:** cả 5/5 lần chạy tự động bằng bản cũ đều bỏ qua bước brief tham vọng, vì bước này cần hỏi người dùng.
- **Đổi 4:** 2 lần chạy dừng giữa chừng ở câu "đang chờ critic".

Đây là phép thử nhỏ (5 lượt mỗi bên, 1 đề, người chấm không mù), chỉ đủ thấy khác biệt lớn.

## Rủi ro đã biết
Chuỗi chữ + số không có sẵn mã màu như chuỗi hex, nên AI tự chọn màu. Ở phép thử, 5/15 hướng ra gần cùng một tông đỏ gỉ.

## Nguồn
- Kỹ thuật seed phỏng theo *String Seed of Thought* (Sakana AI) và prompt seed của Anshu Chimala trên Lenny's Newsletter.
