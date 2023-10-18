
# Countdown

def countdown(x):
    cd_list=[]
    for i in range(x,-1,-1):
        cd_list.append(i)
    print (cd_list)

countdown(5)

# =======================================================

# Print and return

def print_and_return(Alist):
    print(Alist[0])
    return Alist[1]

print_and_return([1,2])

# ======================================================

# first plus length

def first_plus_length(Alist):
    sum=Alist[0]+len(Alist)
    print(sum)

first_plus_length([1,2,3,4,5])

# ====================================================

# Values greater than second

def values_greater_than_second(Alist):
    ylist=[]
    counter=0
    if len(Alist)<=2:
        print("Flase")
    else:
        for i in range (len(Alist)):
            if Alist[i]>Alist[1]:
                ylist.append(Alist[i])
                counter=counter+1
        print(ylist)
        print(counter)

values_greater_than_second([3,4,5,2,5,6,1,2,3])
values_greater_than_second([3])

# ======================================================

# length and value

def length_and_value(a,b):
    Alist=[]
    for i in range (a):
        Alist.append(b)
    print(Alist)

length_and_value(4,7)
length_and_value(6,2)

# ==================================================