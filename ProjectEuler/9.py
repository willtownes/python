#Find Pythagorean Triplets
#By Will Townes

for b in range(2,1000,1):
    a = (500000-1000*b)/(1000-b)
    c = (a**2+b**2)**.5
    if a%1 != 0 or a>1000 or a<0 or a>=b or c%1 != 0 or c>1000 or c<0 or c<=b:
        pass
    else:
        break
print('a= '+str(a)+', b= '+str(b)+', c= '+str(c))
        
