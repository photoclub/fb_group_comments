# text = []
# subcomment = []

# text.append("This is dan")
# text.append("This is soul")
# text.append("This is jesee")
# text.append("This is pinkman")

# ind = text.index("This is dan")
# subcomment.insert(ind,"welcome dan")

# ind = text.index("This is pinkman")
# print(ind)
# subcomment.insert(ind,"welcome pinkman")
# print(subcomment)
# print(subcomment[1])
d = {'dan' : ["This is dan","welcome dan","thank you"],
    'pinkman' : ["This is pinkaamna","welcome pinkman","thank you"]
}
text = []
sb = []

d['dan'].append('pleasure')
for k,v in d.items():
    text.append(k)
    sb.append(v)

print(text)
print(sb)