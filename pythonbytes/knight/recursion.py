# What will this program print out? 
def recursion(a): 
    if a == 0: return a
    return a + recursion(a-1)
    
answer = recursion(7)
print(answer)
