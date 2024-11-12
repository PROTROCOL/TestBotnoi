def print_pattern(x):
    # ขึ้นด้านบน
    for i in range(1, x + 1):
        print('*' * i)
    # ลงด้านล่าง
    for i in range(x - 1, 0, -1):
        print('*' * i)

# ทดสอบฟังก์ชัน
x = 5
print_pattern(x)
