import sys

option = sys.argv[1] # sys.argv[0]은 파일의 이름이 들어가기 때문에 사용할 필요 없다.

if option == '-a' : # 내용 추가하기
    with open("notepad.txt", "a") as f :
        txt = sys.argv[2]
        f.write(txt)
        f.write("\n")

elif option == '-p' : # 내용 출력하기
    with open("notepad.txt", "r") as f :
        print(f.read())

elif option == '-e' : # 내용 전체 지우기
    with open("notepad.txt", "w+") as f :
        f.write("")