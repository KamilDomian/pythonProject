from circleUtils import *
from numberGetter import input_int_number

user_choice = -1

while user_choice != 0:
    print()
    print("1 oblicz pole koła")
    print("2 oblicz obwód koła")
    print("0 zamknij")
    user_choice = input_int_number("Wybierz metode ")

    if user_choice == 1:
        pole_task()
    elif user_choice == 2:
        obwod_task()
    elif user_choice != 0:
        print("Błędny wybór!")
