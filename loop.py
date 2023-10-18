
# Basics

for i in range (151):
    print(i)

# Multiples of five

for i in range(5,1001,5):
    print(i)
    
# Counting, the Dojo way

for i in range(1,101,1):
    if (i%10==0) and (i%5 ==0):
        print("Coding Dojo")
    elif i%5==0:
        print("Coding")
    else:
        print(i)
    
# summation of odd number (0,500.000)

count = 0
for i in range(500001):
    if(i%2!=0):
        count=count+i
print(count)

# Countdown by Four

for i in range (2018,0,-4):
    print(i)

# Flexible Counter

def flexibleCounter(lowNum,highNum,mult):
    for i in range(lowNum,highNum,1):
        if i%mult==0:
            print(i)

flexibleCounter(2,10,3)