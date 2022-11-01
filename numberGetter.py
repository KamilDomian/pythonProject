INTEGER_TRY_AGAIN_ = "Not an integer !   Try again!"
FLOAT_TRY_AGAIN_ = "Not an float!  Try again!"


def input_float_number(message):
    while True:
        try:
            user_input = float(input(message))
        except ValueError:
            print(FLOAT_TRY_AGAIN_)
            continue
        else:
            return user_input


def input_int_number(message):
    while True:
        try:
            user_input = int(input(message))
        except ValueError:
            print(INTEGER_TRY_AGAIN_)
            continue
        else:
            return user_input


# int (integer) to są liczby całkowite czyli 1, 2, 4
# float (zmienno przecinkowe) czyli np 3.12 , 23.09123
# str (string) Tekst - "Ala ma kota", "Ala ma 2 koty!"
