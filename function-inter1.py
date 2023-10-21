import random
def randInt(min=  0 , max= 100  ):
    num = random.random()*(max-min)+min
    return round(num)
print(randInt()) 

print(randInt(max=50)) 	

print(randInt(min=50)) 

print(randInt(min=50, max=500))   

print(randInt(max=-100))

print(randInt(min=100, max=0))