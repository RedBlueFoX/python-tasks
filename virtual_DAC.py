ratio = 1023/5

def V_DAC(value):
    return(round(value/ratio, 2))

input_value = int(input())
print(V_DAC(input_value))