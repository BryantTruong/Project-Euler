j = []

for i in list(range(1,1000)):
    if i%3 == 0 or i%5 == 0:
       j.append(i)

print(sum(j))        
