import sys
# 시간 안에 못풀었습니다.
sys.stdin = open("_암호문1.txt")
command=[]
for testcase in range(10):
    Password_length=int(input()) # 첫 번째 줄 : 원본 암호문의 길이 N ( 10 ≤ N ≤ 20 의 정수)
    Password = input().split()  # 두 번째 줄 : 원본 암호문
    def_num=int(input())        # 세 번째 줄 : 명령어의 개수 ( 5 ≤ N ≤ 10 의 정수)
    for idx in range(def_num):    # 네 번째 줄 : 명령어
        def_ = input().split()
        command.append(def_) #[[def_],[def_],[def_],[def_],[def_].....] 이런 꼴

def I(Password,x,y,s):
    for i in range(len(Password)):
        Password[x]
