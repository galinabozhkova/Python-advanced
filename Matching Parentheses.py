expression = list(input())
paranthesis_index= []
for i in range(len(expression)):
    if expression[i] == "(":
        paranthesis_index.append(i)
    elif expression[i] == ")":
        print("".join(expression[paranthesis_index.pop():i+1]))
