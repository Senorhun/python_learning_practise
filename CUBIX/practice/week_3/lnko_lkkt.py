def LNKO(a, b):    
    while a != b:        
        if a > b:        
            a -= b        
        else:        
            b -= a        
    return a

def LKKT(a, b):
    return (a * b) // LNKO(a, b)

if __name__ == "__main__":
    a = 30
    b = 12
    
    print("Legnagyobb közös osztó (LNKO):", LNKO(a, b))
    print("Legkisebb közös többszörös (LKKT):", LKKT(a, b))