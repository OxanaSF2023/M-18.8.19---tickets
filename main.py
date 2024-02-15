
total_tickets = int(input("Количество билетов:   "))
full_sum = 0
for tickets in range(0, total_tickets):
    age = int(input("Ваш возраст:   "))
    if int(age) >= 25:
        print("Цена билета 1390 руб.")
        full_sum += 1390
    elif 18 <= int(age) < 25:
        print("Цена билета 990 руб.")
        full_sum += 990
    else:
        print("Вход свободный")

print("Стоимость билетов:   ", full_sum)

if total_tickets > 3:
    print("Скидка 10%: ", full_sum * 0.1)
    print("Стоимость билетов со скидкой:  ", full_sum - (full_sum * 0.1))

