#Дни недели пронумерованы следующим образом: 0 — воскресенье, 1 — понедельник, 2 — вторник, …, 6 — суббота. Дано целое число K, лежащее в диапазоне 1–365. 
# Определить номер дня недели для K-го дня года, если известно, что в этом году 1 января было четвергом.
def number_of_weekend(K):
    weekday_number = 2
    day_counter = 1
    while day_counter != K:
        weekday_number += 1
        day_counter += 1
        if weekday_number == 7:
            weekday_number = 0
    return weekday_number


K = int(input('Введите номер дня\n'))
weekday = number_of_weekend(K)
print("номер дня недели для {}-го дня равен: {}".format(K, weekday))
