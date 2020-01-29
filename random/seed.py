import random
random.seed(10)
print(random.random())

c=random.randint(1,100)
print(c)
c1=random.randrange(1,100,2)
print(c1)
c2=random.getrandbits(16)
print(c2)
c3=random.uniform(10,100)
print(c3)
c3=random.choice([1,2,3,4])
print(c3)
c4=[1,2,3,4,5,6,7]
random.shuffle(c4)
print(c4)