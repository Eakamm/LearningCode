# 遍历
# names = ['ff','fffff','sdss']

# for name in names:
#   print(name)

people = {'age': '10', 'name': 'jack', 'sex': 'male'}

adds = []
adds = people.items()

for v in adds:
    print(v[0])

del people['age']

for v in adds:
    print(v[0])
# i = 0
# while True:

#     i+=1;
#     print("i")
