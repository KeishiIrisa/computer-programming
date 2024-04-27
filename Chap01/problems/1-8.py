input_string = input().split(",")
i = input_string.index("boundary")
stations, express_station = input_string[:i], input_string[i + 1:]

# 急行が止まる駅のindexのリストを作成
express_index = [stations.index(station) for station in stations if station in express_station]

# express_indexの差分のリストを作成
express_index_difference_list = [express_index[i + 1] - express_index[i] - 1 for i in range(len(express_index) - 1)]

print(express_index_difference_list)