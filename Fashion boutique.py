stack_clothes = list(map(int, input().split()))
capacity = int(input())
current_capacity = capacity
rack = 1
while stack_clothes!=[]:
    for el in stack_clothes:
        if current_capacity>=stack_clothes[-1]:
            current_capacity-=stack_clothes.pop()
        else:
            current_capacity = capacity
            rack+=1

print(rack)
