print([list(filter(lambda x: x % 2 == 0, [int(x) for x in input().split(', ')])) for _ in range(int(input()))])
