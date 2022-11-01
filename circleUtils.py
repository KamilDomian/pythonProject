import math

from numberGetter import input_float_number


def pole_task():
    promien = input_float_number("Podaj promień: ")
    pole = math.pi * promien ** 2
    print(f"Pole koła o promieniu {promien} wynosi  : {pole}")


def obwod_task():
    promien = input_float_number("podaj promien: ")
    obwod = math.pi * promien * 2
    print(f"Obwód koła o promieniu: {promien}  wynosi  :  {obwod}")
