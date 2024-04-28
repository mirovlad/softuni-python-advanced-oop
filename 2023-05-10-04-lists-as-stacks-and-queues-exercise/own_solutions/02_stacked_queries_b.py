# https://judge.softuni.org/Contests/Compete/Index/1831#1
# Failed tests https://judge.softuni.org/Contests/Compete/Index/1831#2

cnt = int(input())

numbers = []
for idx in range(cnt):
    line = input()
    nodes = line.split()
    cmd = nodes[0]

    if cmd == "1":
        number = int(nodes[1])
        numbers.append(number)
    elif cmd == "2":
        if numbers:
            numbers.pop()
    elif cmd == "3":
        if numbers:
            print(max(numbers))
    elif cmd == "4":
        if numbers:
            print(min(numbers))
    else:  # Unknown command
        #print("Unknown command")
        pass
    #print(f"numbers {numbers}")

reversed_numbers = []
while numbers:
    reversed_numbers.append(numbers.pop())

print(", ".join(map(str, reversed_numbers)))


# Failed test:
# Test #1 (Runtime error)
# Time used: 0.040 s
# Memory used: 0.00 MB
