parenthesis = list(input())

opening_parenthesis = []
is_balanced = True

for el in parenthesis:
    if el in "({[":
        opening_parenthesis.append(el)
    elif el in "}])":
        if len(opening_parenthesis) == 0:
            is_balanced = False
            break
        else:
            if f"{opening_parenthesis.pop()}{el}" not in ["[]", "()", "{}"]:
                is_balanced = False
                break

if len(opening_parenthesis) == 0 and is_balanced:
    print("YES")
else:
    print("NO")
