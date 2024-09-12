def prime_chk(n):
    c = 0
    for i in range(2,n):
        if n % i == 0:
            c = c + 1
    if c == 0:
        return 1
    else:
        return 0


LB = int(input("Enter LB:"))
UB = int(input("Enter UB:"))

for val in range(LB, UB+1):
    if prime_chk(val) == 1:
        print(val)
        
         
# This comment is from local system
# This is my second comment from local system


