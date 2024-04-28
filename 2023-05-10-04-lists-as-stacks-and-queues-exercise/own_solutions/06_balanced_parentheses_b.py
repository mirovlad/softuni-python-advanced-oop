# Own solution from 2023

# https://judge.softuni.org/Contests/Compete/Index/1831#5

expr = input()

brackets = []
brackets.append({"open": "(", "close": ")", "name": "round"})
brackets.append({"open": "[", "close": "]", "name": "square"})
brackets.append({"open": "{", "close": "}", "name": "curly"})
#print(f"brackets A {brackets}")

# Will stack the opened brackets that are not yet closed
nodes = []

is_balanced = True
for idx, c in enumerate(expr):
    for bracket_idx, bracket in enumerate(brackets):
        node = {
            "idx": idx,
            "c": c,
            "bracket_idx": bracket_idx
        }
        if c == bracket["open"]:
            nodes.append(node)
            break  # No need ot check for other type of bracket
        elif c == bracket["close"]:
            if nodes:
                # Having a closing bracket, we want to check if it matches the type of the last opening bracket
                prev_node = nodes.pop()
                prev_node_bracket_idx = prev_node["bracket_idx"]
                prev_node_bracket = brackets[prev_node_bracket_idx]
                prev_node_close = prev_node_bracket["close"]
                if prev_node_close != c:
                    # The closing bracket we have does not match the one expected by the most recent opening bracket
                    is_balanced = False
            else:
                is_balanced = False
            break # No need ot check for other type of bracket

        if not is_balanced:
            break

if is_balanced:
    print("YES")
else:
    print("NO")


