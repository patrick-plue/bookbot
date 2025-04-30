my_list = [{"a": 1}, {"b": 2}]


for x in my_list:
    print(list(x.keys())[0])
    print(list(x.values())[0])