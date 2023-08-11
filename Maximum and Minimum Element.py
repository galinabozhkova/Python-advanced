sequence = []
n = int(input())

for _ in range(n):
    query = input()
    if query.startswith("1") :
        sequence.append(int(query.split()[1]))
    if len(sequence)>0:
        if query == "2":
                sequence.pop()
        elif query =="3":
            print(max(sequence))
        elif query == '4':
            print(min(sequence))

if len(sequence)>0:
    print(", ".join([str(sequence.pop()) for _ in range(len(sequence))]))


















