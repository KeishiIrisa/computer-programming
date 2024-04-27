import copy

input_string = input().replace("[", "").replace("]", "").split(",")
i, j = map(int, input_string[:2])
x = list(map(int, input_string[2:]))

# リストの反転
f = copy.copy(x[i:j+1])
f.reverse()
new_x = x[:i] + f + x[j+1:]

print(new_x)