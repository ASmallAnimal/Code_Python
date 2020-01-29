#break contine
#break: 

for c in "python":
    if c=='t':
        continue
    print(c)
print("")
for c in "python":
    if c=='t':
        break
    print(c)

s="python"
while s!="":
    for c in s:
        if c=="t":
            break
        print(c,end="")
    s=s[:-1]