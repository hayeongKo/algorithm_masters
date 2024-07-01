import sys

input = sys.stdin.readline
word = list(input().removesuffix("\n"))

lst_word = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        first = word[:i]
        second = word[i:j]
        third = word[j:]

        first.reverse()
        second.reverse()
        third.reverse()

        total = first + second + third
        lst_word.append(''.join(total))

lst_word.sort()
print(lst_word[0])