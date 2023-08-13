from collections import deque


def calc_time(time, add_time):
    hours, minutes, seconds = [int(el) for el in time.split(":")]
    seconds += add_time
    if seconds >= 60:
        seconds -= 60
        minutes += 1
        if minutes >= 60:
            minutes -= 60
            hours += 1
            if hours >= 24:
                hours -= 24
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


robots_info = input().split(";")
robot_data = {}
hour, min, sec = [int(el) for el in input().split(":")]

for el in robots_info:
    name, proc_time = el.split("-")
    robot_data[name] = [int(proc_time)]

list_products = deque()
current_time = f"{hour:02d}:{min:02d}:{sec:02d}"
current_index = 0
time_ready = ''

command = input()
while command != "End":
    list_products.append(command)
    command = input()

for key, value in robot_data.items():
    if len(list_products) > 0:
        current_time = calc_time(current_time, 1)
        value.append(current_time)
        value[1] = calc_time(current_time, value[0])
        print(f"{key} - {list_products.popleft()} [{current_time}]")

while len(list_products) >= 1:
    current_time = calc_time(current_time, 1)
    for key, value in robot_data.items():
        if value[1] == current_time:
            print(f"{key} - {list_products.popleft()} [{current_time}]")
            value[1] = calc_time(current_time, value[0])


