Hat = [4,11,51,23,67,88,11,10]
print(sum(Hat))
print(max(Hat))
print(Hat.count(11))

Hat = list(dict.fromkeys(Hat))
print(Hat)