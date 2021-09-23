a =[34,5,6,7,8,9,5,6,7,8]
b=[2,4,5,6,7,8,9,34,66,7,7,8,3]
c=[]

for i in range (len(b)):
  if b[i] in a:
      c.append(b[i])
print(c)