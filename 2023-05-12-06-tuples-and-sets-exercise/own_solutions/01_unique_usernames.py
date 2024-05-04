# print(*set(input() for _ in range(int(input()))), sep="\n")
print(*{input() for _ in range(int(input()))}, sep="\n")

