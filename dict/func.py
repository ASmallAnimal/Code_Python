d = {"1":"A","2":"B","3":"C"}
del d["1"]
print(d)
print("2" in d)
print(d.keys())
print(d.values())
print(d.items())

print(len(d))
print(d.get("2"))
print(d.pop("2"))
print(d.popitem())
d["4"]="D"
print(len(d))
d.clear()
print(len(d))