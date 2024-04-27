"""
prog_1:改善点報告
課題1-5で問題文に入力の二つのリストの間には「boundary」という文字列があるとする。という指定があるのにも関わらず、入力例にはそれが含まれていなかったため、入力として「boundary」を含む二つのリスト{string}を与えたときにも正しく動作するように改善したプログラムを作成した。
"""


input_string = input()
stations = input_string.split(",")


def change_to_komaba_todaimae(station_list):
    i = station_list.index("駒場東大前駅")
    new_station_list = station_list[:i] + ["駒場駅", "東大前駅"] + station_list[i + 1:]

    return new_station_list


# 入力されたリストに"boundary"の文字列がある場合とない場合で処理を分岐させる
if "boundary" in stations:

    # "boundary"によってリストを二つのリストに分割する

    i_boundary = stations.index("boundary")
    separated_stations = [stations[:i_boundary], stations[i_boundary+1:]]

    # "駒場東大前駅"が入っている場合にのみ"駒場駅"と"東大前駅"に分割する
    new_stations = []

    for station in separated_stations:
        if "駒場東大前駅" in station:
            new_stations += (change_to_komaba_todaimae(station))
        else:
            new_stations += station

    print(new_stations)

else:
    if "駒場東大前駅" in stations:
        print(change_to_komaba_todaimae(stations))
    else:
        print(stations)
