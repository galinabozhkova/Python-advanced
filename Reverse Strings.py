sentence = list(input())

reversed = []

while len(sentence)>0:
    reversed.append(sentence.pop())

print(''.join(reversed))