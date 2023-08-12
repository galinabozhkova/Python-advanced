parantheses = list(input())

is_balanced = False

data_check = []

for el in parantheses:
    if el in "{[(":
        data_check.append(el)
    else:
        if len(data_check)==0:
            is_balanced = False
            break
        elif len(data_check)>0:
            if el == "}":
                if data_check.pop() != "{":
                    is_balanced = False
                    break
            elif el == "]":
                if data_check.pop() != "[":
                    is_balanced = False
                    break
            elif el == ")":
                if data_check.pop() != "(":
                    is_balanced = False
                    break
    is_balanced = True


if len(data_check)==0:
    if is_balanced:
        print("YES")
    else:
        print("NO")
else:
    print("NO")


