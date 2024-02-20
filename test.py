from random import randint
 
print("WElcome")
pc_choice = randint(1,100)
playing = True

# while 반복문을 사용할 수 있어야 함.주석 단축기 -> command +/
while playing:
    user_choice = int(input("choose number (1-100): "))
    if user_choice == pc_choice:
        print("win")
        playing = False # while문이 멈추는 시점은 if문의 조건이 일치하여 실행됐을 때이다.
    elif user_choice > pc_choice:
        print("Lower")
    elif user_choice < pc_choice:
        print("Higher") 

# 깃 최초 커밋시에 이메일 및 이름을 등록해야 한다.
# git config --global user.email "@gmail.com"
# git config --global user.name "kyoungminLee"