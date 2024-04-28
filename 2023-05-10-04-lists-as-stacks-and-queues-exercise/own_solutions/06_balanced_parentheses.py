from collections import deque

expr = input()

opened = deque()
# opened = list()

matches = {
    "{": "}",
    "[": "]",
    "(": ")",
}
closables = matches.values()

balanced = True
for char in expr:
    if char in matches:
        opened.append(char)
    else:
        if char in closables:
            if opened:
                opening = opened.pop()
                if matches[opening] == char:
                    continue  # Happy!
                else: # Drama
                    # put the opening back, not necessarily needed
                    opened.append(opening)
                    balanced = False
            else:  # Found a closable before any opening
                balanced = False
                break

if balanced:
    print("YES")
else:
    print("NO")




