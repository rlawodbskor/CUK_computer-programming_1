human_choice= int(input("사람 선택(1:가위 2:바위 3:보):"))
import random
com_choice= random.randint(1,3)
print("컴퓨터의 선택(1:가위 2:바위 3:보)",com_choice)

if human_choice == com_choice:
    print ("비겼습니다.")
elif human_choice == 3 and com_choice == 1:
    print ("컴퓨터가 이겼습니다.")
elif human_choice == 1 and com_choice == 3:
    print ("사람이 이겼습니다.")
elif human_choice > com_choice:
    print ("사람이 이겼습니다.")
elif human_choice < com_choice:
    print ("컴퓨터가 이겼습니다.")

    
