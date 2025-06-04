
# reminding myself how defaultdict from collections works


from collections import defaultdict

d = defaultdict(set)

d[0].add(1)
d[0].add(2)
print(d)

d[0].remove(2)
print(d)


# d[0].remove(3) # errors
# print(d)