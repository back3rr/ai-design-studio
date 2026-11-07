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
```

## Thay đổi ở bản này (2026-11-07)
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
