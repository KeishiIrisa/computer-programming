input_string = input().split(",")

# boundaryのindexを調べて、井の頭線の駅のリストと急行が止まる駅のリストに分割する
i = input_string.index("boundary")
inokashira_list, inokashira_express_list = input_string[:i], input_string[i + 1:]

# 急行に止まらない駅のリストを作成する
inokashira_non_express_list = [j for j in inokashira_list if j not in inokashira_express_list]
        
print(inokashira_non_express_list)