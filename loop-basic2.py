
# biggie size

def biggie_size(Alist):
    for i in range (len(Alist)):
        if Alist[i]>0:
            Alist[i]="big"
    print(Alist)
    
biggie_size([-1, 3, 5,-5])
# ==========================================

# Count positive

def count_positives(Alist):
    counter=0
    for i in range (len(Alist)):
        if Alist[i]>0:
            counter=counter+1
    Alist[len(Alist)-1]=counter
    print(Alist)
    
count_positives([-1,1,1,1])
count_positives([1,6,-4,-2,-7,-2])
# ===========================================

# Sum total

def sum_total(Alist):
    sum=0
    for i in range (len(Alist)):
        sum=sum+Alist[i]
    print(sum)
    return sum
    
sum_total([1,2,3,4])
sum_total([6,3,-2])
# =============================================

# Average

def average(Alist):
    sum=0
    for i in range (len(Alist)):
        sum=sum+Alist[i]
    avg=sum/len(Alist)
    print(avg)
    return avg
    
average([1,2,3,4])
# ===============================================

# Length

def length(Alist):
    sum=0
    for i in range (len(Alist)):
        sum=sum+1
    print(sum)
    return sum

length([37,2,1,-9])
length([])
# ================================================

# Minimum

def minimum(Alist):
    if len(Alist)<1:
        print("False")
        return "False"
    else:
        min=Alist[0]
        for i in range (len(Alist)):
            if min>Alist[i]:
                min=Alist[i]
        print(min)
        return min
                
minimum([37,2,1,-9])
minimum([])
# ===============================================

# Maximum

def maximum(Alist):
    if len(Alist)<1:
        print("False")
        return "False"
    else:
        max=Alist[0]
        for i in range (len(Alist)):
            if max<Alist[i]:
                max=Alist[i]
        print(max)
        return max
                
maximum([37,2,1,-9])
maximum([])
# =================================================

# Ultimate analysis

def ultimate_analysis(Alist):
    analysis={}
    sum=0
    for i in range (len(Alist)):
        sum=sum+Alist[i]
    analysis['sumTotal'] = sum
    sum=0
    for i in range (len(Alist)):
        sum=sum+Alist[i]
    avg=sum/len(Alist)
    analysis['average'] = avg
    if len(Alist)<1:
        print("False")
    else:
        min=Alist[0]
        for i in range (len(Alist)):
            if min>Alist[i]:
                min=Alist[i]
    analysis['minimum'] = min
    if len(Alist)<1:
        print("False")
    else:
        max=Alist[0]
        for i in range (len(Alist)):
            if max<Alist[i]:
                max=Alist[i]
    analysis['maximum']= max
    sum=0
    for i in range (len(Alist)):
        sum=sum+1
    analysis['length']=sum
    print(analysis)  
    
ultimate_analysis([37,2,1,-9])
# ===========================================

# Ultimate analysis method 2

def ultimate_analysis(Alist):
    analysis={}
    analysis['sumTotal'] = sum_total(Alist)
    analysis['average'] = average(Alist)
    analysis['minimum'] = minimum(Alist)
    analysis['maximum']= maximum(Alist)
    analysis['length']= length(Alist)
    print(analysis)

ultimate_analysis([37,2,1,-9])

# ==============================================

# Reverse list

def reverse_list(Alist):
    for i in range (0,len(Alist)-2):
        temp = Alist[i]
        Alist[i]= Alist[len(Alist)-1-i]
        Alist[len(Alist)-1-i] = temp
    print (Alist)

reverse_list([37,2,1,-9])
