#LINEAR CONGRUENTIAL ALGORITHM

def pseudo(seed, a,c,m,list):      #a=multiplier, c=increment, m=modulus

    print(seed)


    list.append(seed)
    seed= (a*seed+c)%m
    #no=seed/m                                      #to get a uniform distribution between [0,1]
    

    if seed!=list[0]:
        pseudo(seed,a,c,m,list)
    

seed=int(input('enter seed value: '))

list=[]


pseudo(seed,13,0,64,list)

cycle_length= len(list)
print("cycle length is: ",cycle_length)


#Here, a major problem is that seed value affects the cycle length of the pseudo no generator & 

