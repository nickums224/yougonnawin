Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>>
def you_gonna_win(amount=6):
"""Returns random lottery numbers in list of 6

>>>you_gonna_win()
How many numbers for this game? 6
[55, 3, 54, 23, 41, 25]

"""

from random import randint as numb
    return [numb(1,69) for number in range(amount)]

def tell_me_what(prompt="how many times are you going to play?"):
    return int(input(prompt))



