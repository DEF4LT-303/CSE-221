def LCS(x,y,z):
    m = len(x)+1
    n = len(y)+1
    o = len(z)+1
    
    
    arr=[]
    mdown = m-1
    ndown = n-1
    odown = o-1
    
    c = [[[0 for i in range(o)] for j in range(n)] for k in range(m)]
    t = [[[0 for i in range(o)] for j in range(n)] for k in range(m)]   
    
    
    for i in range(1,m):
        for j in range(1,n):
            for k in range(1,o):
                               
                if(i == 0 or j == 0 or k == 0):
                    c[i][j][k]= 0
                    t[i][j][k]= None

                else:    
                    
                    if(x[i-1]==y[j-1] and x[i-1]==z[k-1]):
                        c[i][j][k]=1+c[i-1][j-1][k-1]
                        t[i][j][k]='diagonal'

                    else:

                        if(c[i-1][j][k]>=c[i][j-1][k]):
                            max=c[i-1][j][k]

                            if(max >= c[i][j][k-1]):
                                c[i][j][k]=max
                                t[i][j][k]='up-up-left'

                            else:
                                max=c[i][j][k-1]
                                c[i][j][k]=max
                                t[i][j][k]='left-up-up'

                        else:

                            max=c[i][j-1][k]

                            if(max >= c[i][j][k-1]):
                                c[i][j][k]=max
                                t[i][j][k]='up-left-up'

                            else:
                                max=c[i][j][k-1]
                                c[i][j][k]=max
                                t[i][j][k]='left-up-up'



    while mdown > 0 or ndown > 0 or k > 0:
        leader = t[mdown][ndown][odown]
        
        if leader =='up-up-left':
            mdown -= 1
            
        elif leader =='left-up-up':
            odown -= 1
            
        elif leader =='up-left-up':
            ndown -= 1
            
            
            
        elif leader == 'diagonal':
            arr.append(x[i-1])
            
            mdown -= 1
            ndown -= 1
            odown -= 1

        else:
            break
         
            
    reverse = list(reversed(arr))
    return reverse
    

input_file = open('F:\CODES\Python_VS\CSE221 Labs\Lab 06\Problem 2\input2.txt','r')
output_file=open('F:\CODES\Python_VS\CSE221 Labs\Lab 06\Problem 2\output2.txt',"w")
lines=input_file.read().splitlines()
input_file.close()

x=lines[0]
y=lines[1]
z=lines[2]

outputX=len(LCS(x,y,z))

output_file.write(f"{outputX}")
output_file.close()