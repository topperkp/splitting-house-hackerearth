# Test comment 1 for program
n = int(input())
string = list(map(str,input().split()))

l = len(string)

s = ''

if string[0]==string[l-1]:
    print('YES')
    for i in string:
        print(i)
        if i is '.' :
            s= s+'B'
        else:
            s=s+i    


    print(s)

else:
    pass        
        
      
        
