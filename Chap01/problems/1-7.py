input_string = input().split(",")

i = input_string.index("boundary")
line1, line2 = input_string[:i], input_string[i + 1:]

# 乗り換え駅を見つける
transfer_station = [station for station in line1 if station in line2]

full_route = line1[:line1.index(transfer_station[0]) + 1] + line2[line2.index(transfer_station[0]) + 1:]

print(full_route)