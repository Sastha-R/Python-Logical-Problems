
tot = 0
c = 0
lar = sma = None;
sec = 0 

with open("./numbers.txt","r") as file:
    
    for i in file:
        tot += int(i)
        c += 1

        if(lar == None):
            lar = int(i)

        if(int(i) > lar):
            sec = lar
            lar = int(i)  

        elif int(i) > sec and int(i) != lar:
            sec = int(i)  

        if(sma == None):
            sma = int(i)
        
        if(int(i) < sma):
            sma = int(i)  


print("total : ",tot)

print("average : ",tot / c)

print("Largest : ",lar)

print("Second Largest : ",sec)

print("smallest : ",sma)

