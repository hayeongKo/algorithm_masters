import sys

input = sys.stdin.readline

def palindrome(strings):
    count = [0 for i in range(26)] # 대문자만 있으니까 아스키코드를 이용해서 65~

    for string in strings:
        count[ord(string)-65] += 1

    cnt = 0
    mid = 999

    for i in range(len(count)):
        if len(strings) % 2 == 0: #짝수개 일때
            if count[i] % 2 == 1:
                print("I'm Sorry Hansoo")
                return
        else:
            if count[i] % 2 == 1: #홀수개 일때
                if cnt > 0:
                    print("I'm Sorry Hansoo")
                    return
                cnt += 1
                mid = i
    
    answer = ""
    for i in range(len(count)): #절반만 만들고 뒤집기
        half = count[i] // 2 if count[i] % 2 == 0 else (count[i]+1)//2
        while True:
            if count[i] == half:
                break
            else:
                answer += chr(i+65)
                count[i] -= 1
                    
    if mid != 999:
        answer = answer + chr(mid+65) + answer[::-1]
    else:
        answer = answer + answer[::-1]
    print(answer)
palindrome(input().rstrip())