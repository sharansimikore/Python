'''
Celcium to Fahrenheit
F = (C*9/5)+32

'''
def temperature(t):
    return (t*9/5)+32

t1 = int(input("input temp:\n"))
C_to_F = temperature(t1)
print("C_to_F:", C_to_F)