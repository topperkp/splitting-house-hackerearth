# Test comment 1 for program
n = int(input())
string = list(map(str,input().split()))

l = len(string)

s = ''

if string[0]==string[l-1]:
    for i in string:
        if i is '.' :
            s= s+'B'
        else:
            s=s+i    


    print(s)

else:
    pass   
        
      
        
