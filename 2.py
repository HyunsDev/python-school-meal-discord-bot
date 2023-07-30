import random

# 가위바위보
user_hand = input("가위! 바위! 보!: ")
bot_hand = random.choice(["가위", "바위", "보"])

print("봇 : " + bot_hand)

winner = ""

if user_hand == bot_hand:
    winner = "비겼다"

elif user_hand == "가위":
    if bot_hand == "바위":
        print("졌다.")

    elif bot_hand == "보":
        print("이겼다!")

elif user_hand == "바위":
    if bot_hand == "가위":
        print("이겼다!")

    elif bot_hand == "보":
        print("졌다.")

elif user_hand == "보":
    if bot_hand == "가위":
        print("졌다.")

    elif bot_hand == "바위":
        print("이겼다.")


# if a == "가위":
#     a = 1

# elif a == "바위":
#     a = 2

# elif a == "보":
#     a = 3


# if a == b:
#     if b == 1:
#         print("봇 : 가위")
#         print("비겼다!")

#     if b == 2:
#         print("봇 : 바위")
#         print("비겼다!")

#     if b == 3:
#         print("봇 : 보")
#         print("비겼다!")

# if a == 1:
#     if b == 2:
#         print("봇 : 바위")
#         print("졌다.")

#     if b == 3:
#         print("봇 : 보")
#         print("이겼다!")

# if a == 2:
#     if b == 1:
#         print("봇 : 가위")
#         print("이겼다!")

#     if b == 3:
#         print("봇 : 보")
#         print("졌다.")

if a == 3:
    if b == 1:
        print("봇 : 가위")
        print("졌다.")

    if b == 2:
        print("봇 : 바위")
        print("이겼다!")
