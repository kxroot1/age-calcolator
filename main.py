from datetime import date, datetime

# 🔁 بدّل هاد السطر إذا بغيتي تحسب بحال المثال (2021-01-01)
# REFERENCE_DATE = date(2021, 1, 1)
REFERENCE_DATE = date.today()


def compute_age(birth_date: date, ref: date) -> int:
    """Compute age in full years at reference date."""
    years = ref.year - birth_date.year
    # إذا مازال عيد الميلاد ما جا فهاد العام
    if (ref.month, ref.day) < (birth_date.month, birth_date.day):
        years -= 1
    return years


def parse_line(line: str):
    """
    Expected format: Name, dd-mm-yyyy
    Returns (name, birth_date) or (name, None) if invalid.
    """
    if "," not in line:
        return None, None

    name_part, date_part = line.split(",", 1)
    name = name_part.strip()
    dstr = date_part.strip()

    # name فارغ => مدخل خايب
    if not name:
        return None, None

    # خاصها تكون dd-mm-yyyy
    parts = dstr.split("-")
    if len(parts) != 3:
        return name, None

    # منع الرموز/القيم السالبة: خاص كلشي يكون digits فقط
    if not all(p.strip().isdigit() for p in parts):
        return name, None

    dd, mm, yyyy = (int(p) for p in parts)

    # منع 0 أو قيم سالبة
    if dd <= 0 or mm <= 0 or yyyy <= 0:
        return name, None

    # تحقق حقيقي من التاريخ (كيطيح فـ 31-02-2020 مثلا)
    try:
        bd = date(yyyy, mm, dd)
    except ValueError:
        return name, None

    return name, bd


def main():
    print("دخل الأشخاص بصيغة: Name, dd-mm-yyyy")
    print("مثال: Khalid, 1-2-1989")
    print("كتب 'done' باش تسالي.\n")

    inputs_original = []   # باش نطبع نفس المدخلات
    people = []            # valid people: dicts with name, birth_date, age, weekday

    while True:
        line = input("> ").strip()
        if not line:
            continue
        if line.lower() == "done":
            break

        inputs_original.append(line)

        name, bd = parse_line(line)
        if name is None and bd is None:
            # صيغة ما فيهاش حتى فاصلة أو مشكل كبير: نعتبره invalid بلا اسم واضح
            print("Invalid date, Unknown")
            continue

        if bd is None:
            print(f"Invalid date, {name}")
            continue

        # إذا تاريخ الميلاد فالمستقبل بالنسبة لتاريخ المرجع => invalid
        if bd > REFERENCE_DATE:
            print(f"Invalid date, {name}")
            continue

        age = compute_age(bd, REFERENCE_DATE)
        weekday = bd.strftime("%A")  # English day name
        people.append({
            "name": name.strip().title(),   # نخليها بحال المثال (Khalid)
            "birth_date": bd,
            "age": age,
            "weekday": weekday
        })

    # ✅ طباعة معلومات كل شخص
    for p in people:
        print(f"{p['name']} is {p['age']} years old and she/he was born on {p['weekday']}")

    # ✅ oldest/youngest حسب الشروط
    if len(people) <= 1:
        print("There is no oldest or youngest person.")
    else:
        oldest = max(people, key=lambda x: x["age"])
        youngest = min(people, key=lambda x: x["age"])
        print(f"The oldest one is {oldest['name']}")
        print(f"The youngest one is {youngest['name']}")

    print(f"Total People: {len(people)}")

    # =========================
    # ✅ أسئلة إضافية
    # =========================

    # 1) ترتيب الأشخاص من الأكبر للأصغر
    if people:
        print("\nSorted (oldest -> youngest):")
        for p in sorted(people, key=lambda x: x["age"], reverse=True):
            print(f"- {p['name']} ({p['age']})")

    # 2) طباعة نفس المدخلات ولكن بالعكس
    if inputs_original:
        print("\nInputs reversed:")
        for line in reversed(inputs_original):
            print(line)

    # 3) أسماء الناس اللي تزادو نهار الأحد فقط
    sundays = [p["name"] for p in people if p["weekday"] == "Sunday"]
    print("\nBorn on Sunday only:")
    if sundays:
        for n in sundays:
            print(f"- {n}")
    else:
        print("None")


if __name__ == "__main__":
    main()