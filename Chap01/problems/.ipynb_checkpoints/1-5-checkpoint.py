input_string = input()
inokashira_list = input_string.split(",")

i = inokashira_list.index("駒場東大前駅")
new_inokashira_list = inokashira_list[:i] + ["駒場駅", "東大前駅"] + inokashira_list[i + 1:]

print(new_inokashira_list)
