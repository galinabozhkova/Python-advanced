integers = input().split()

result = list()

while len(integers)>0:
    result.append(integers.pop())

print(" ".join(result))