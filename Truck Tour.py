# from collections import deque
#
# n = int(input())
# data = deque()
# tank = 0
# index = 0
# possible = True
# sum_liters =0
# sum_distance =0
#
# for i in range(n):
#     petrol, distance = input().split()
#     data.append([int(petrol), int(distance)])
#     sum_liters +=int(petrol)
#     sum_distance +=int(distance)
#
# if sum_liters>=sum_distance:
#     index = 0
#     i = 0
#     while True:
#         if tank+data[i][0] >= data[i][1]:
#             tank += data[i][0] - data[i][1]
#             i = i + 1
#             if i == n:
#                 print(index)
#                 break
#         else:
#             tank = 0
#             data.rotate(-1)
#             index+=1
#             if index == n:
#                 break
#
#
#
#
from collections import deque
fuel = 0
pumps = int(input())
deque_pump = deque()
for _ in range(pumps):
    pump_info = input().split()
    deque_pump.append([int(pump_info[0]), int(pump_info[1])])

index = 0
pump = 0
while pump < pumps:
    if fuel + deque_pump[0][0] > deque_pump[0][1]:
        fuel += deque_pump[0][0] - deque_pump[0][1]
        for i in range(1, len(deque_pump)):
            if fuel + deque_pump[i][0] >= deque_pump[i][1]:
                fuel += deque_pump[i][0] - deque_pump[i][1]
            else:
                deque_pump.rotate(-1)
                count = 0
                index +=1
                fuel = 0
                break
    else:
        deque_pump.rotate(-1)
        index += 1
        fuel = 0
    pump+=1

if index<=pumps:
    print(index)


