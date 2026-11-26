student_id = input("請輸入完整學號：").strip().upper()
tail = student_id[-3:]
a = int(student_id[-3])
b = int(student_id[-2])
c = int(student_id[-1])
s = a + b + c


def collect_codes(raw_codes, saved=None):
    result = []
    if saved is not None:
        for code in saved:
            if code not in result:
                result.append(code)

    for raw in raw_codes:
        cleaned = raw.strip().upper()
        if cleaned and cleaned not in result:
            result.append(cleaned)

    return result


saved = ["BASE"]
raw_a = [
    " welcome" + tail + " ",
    "vip" + tail,
    "",
    "WELCOME" + tail,
    "   ",
]
raw_b = [
    " new" + tail + " ",
    " welcome" + tail + " ",
]

activity_a = collect_codes(raw_a, saved=saved)
activity_b = collect_codes(raw_b)
empty_result = collect_codes([])

print(f"學號：{student_id}")
print(f"活動A：{activity_a}")
print(f"活動B：{activity_b}")
print(f"原始saved：{saved}")
print(f"原始raw_a：{raw_a}")
print(f"空資料：{empty_result}")
