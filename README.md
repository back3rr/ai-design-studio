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
scripts/draw.py       bốc ngẫu nhiên 1 ý tưởng ở Stage 0 (chế độ auto)
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
