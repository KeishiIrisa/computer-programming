x = input()
y = x

for i in range(8):
    x += y
    
    if i == 7:
        x += "!"
    
print(x)