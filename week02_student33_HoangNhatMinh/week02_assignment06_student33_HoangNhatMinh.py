from math import sqrt

def foo(a : int, b : int, c : int) : 
    if a == 0 : 
        return ((-b/c))
    else : 
        delta = b*b - 4*a*c
        if delta < 0 : return ()
        elif delta == 0 :
            return (-b/(2*a), -b/(2*a))
        else :
            sqrtDelta = sqrt(delta)
            return ((-b - sqrtDelta)/(2*a), (-b + sqrtDelta)/(2*a))

print(foo(2,3,4)) # ()
print(foo(0,-2,1)) # 2.0
print(foo(1,-2,1)) # (1.0, 1.0)
print(foo(1,-3,2)) # (1.0, 2.0)


