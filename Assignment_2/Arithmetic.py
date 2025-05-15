def Add(no1,no2):
    return no1 + no2

def Sub(no1,no2):
    return no1 - no2

def Mult(no1,no2):
    return no1 * no2

def Div(no1,no2):
    ans = 0.0
    if(no1 == 0 or no2 == 0):
        ans = "Division with zero not possible"
    else:
        ans = no1 / no2
    return ans