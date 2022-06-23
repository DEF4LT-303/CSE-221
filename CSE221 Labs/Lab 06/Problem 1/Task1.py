def LCS(x,y):
    m = len(x) + 1
    n = len(y) + 1  
    

    arr=[]
    mdown = m-1
    ndown = n-1
    
    c = [[0 for i in range(m)] for j in range(n)]
    t = [[None for i in range(m)] for j in range(n)]
     
    for i in range(0,m):
        for j in range(0,n):     

            if x[i-1] == y[j-1]:                         
                c[i][j] = c[i-1][j-1] + 1
                t[i][j] = 'diagonal'
                
            elif c[i-1][j] >= c[i][j-1]:                 
                c[i][j] = c[i-1][j]
                t[i][j] = 'up'
                
            else:
                c[i][j] = c[i][j-1]
                t[i][j] = 'left'


    while mdown > 0 or ndown > 0:
        leader = t[mdown][ndown]
        
        if leader == 'diagonal':
            arr.append(x[mdown-1])
            mdown -= 1
            ndown -= 1
            
        elif leader == 'up':
            mdown -= 1
            
        else:
            ndown -= 1

    reverse = list(reversed(arr))
    return reverse

input_file = open('F:\CODES\Python_VS\CSE221 Labs\Lab 06\Problem 1\input1.txt','r')
output_file = open('F:\CODES\Python_VS\CSE221 Labs\Lab 06\Problem 1\output1.txt','w')
lines=input_file.read().splitlines()
input_file.close()

NoOfZones = int(lines[0])
prediction = lines[1]
actual = lines[2]

zones = {"Y":"Yasnaya","P":"Pochinki","S":"School","R":"Rozhok","F":"Farm","M":"Mylta","H":"Shelter","I":"Prison"}

outputX = LCS(prediction, actual)
prediction = ((len(outputX)*100/NoOfZones))



for i in outputX:
    output_file.write(f"{zones[i]} ")

output_file.write(f"\nCorrectness of prediction: {(prediction)}%")
output_file.close()