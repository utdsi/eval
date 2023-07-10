
str = "Python is fun"


def reverse_str(str):
    
    bag=""
    
    i = len(str)-1
    
    while(i<=0):
        bag+=str[i]
        i=i-1
    
    print(bag)


res = reverse_str(str)

print(res)    