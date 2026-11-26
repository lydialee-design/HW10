student_id = input("請輸入完整學號：").strip().upper()
tail = student_id[-3:]
a = int(student_id[-3])
b = int(student_id[-2])
c = int(student_id[-1])
s = a + b + c


def cumulative_spend(daily_spend, n):
    if n <= 0 or len(daily_spend) == 0:
        return 0
    return cumulative_spend(daily_spend, n - 1) + daily_spend[n - 1]


daily_spend = [
    100 + 10 * a,
    150 + 10 * b,
    0,
    200 + 10 * c,
    50 + 10 * s,
]
n = 3 + c % 3

total_n = cumulative_spend(daily_spend, n)
day_totals = [cumulative_spend(daily_spend, day) for day in range(0, 6)]
empty_spend = cumulative_spend([], 0)

print(f"學號：{student_id}")
print(f"每日費用：{daily_spend}")
print(f"指定n：{n}")
print(f"指定前{n}天累計：{total_n}元")
for day, total in enumerate(day_totals):
    print(f"前{day}天：{total}元")
print(f"空資料：{empty_spend}元")
