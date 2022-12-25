def pascal_triangle(n):
    triangle = [[] for i in range (n)]
    #checking the type and whether n is zero
    if type(n) is not int and n <= 0:
        return []
    #looping through the rows
    for i in range (n):
        for j in range (i+1):
            # value will always be 1 if j is 0, i is zero or theyre equal
            if(j < i): 
                if (j==0):
                  #  print(f"when j is 0, i is {i} and j is {j}")
                    triangle[i].append(1)
                else:
                 #   print(f"when j above 0, i is {i} and j is {j}")
                    triangle[i].append(triangle[i - 1][j] + triangle[i - 1][j - 1])
            elif(j==i):
                #print(f"when j is equal to i, {i} , {j}")
                triangle[i].append(1)
                
    return triangle

    
#print(pascal_triangle(10))
