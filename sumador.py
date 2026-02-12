
def AND(a,b):
    return a & b

def OR(a,b):
    return a | b

def NOT(a):
    return 1-a

def XOR(a,b):
    return OR(AND(NOT(a),b), AND(a,NOT(b)))


def full_adder(a,b,carry):
    suma = XOR(XOR(a,b),carry)
    carry = OR(AND(a,b), AND(carry, XOR(a,b)))
    return suma, carry


def operar(A, B, modo): 
    
    A = [int(x) for x in A]
    B = [int(x) for x in B]

    if modo == "-":
        for i in range(4):
            B[i] = NOT(B[i])
        carry = 1
    else:
        carry = 0

    resultado = [0,0,0,0]

    for i in range(3,-1,-1):
        resultado[i], carry = full_adder(A[i],B[i],carry)

    return "".join(str(x) for x in resultado)



print("Suma 0101 + 0011 =", operar("0101","0011","+"))  # 5 + 3 = 8
print("Suma 1111 + 0001 =", operar("1111","0001","+"))  # overflow normal en 4 bits

print("Resta 0101 - 0010 =", operar("0101","0010","-")) # 5 - 2 = 3
print("Resta 0110 - 0100 =", operar("0110","0100","-")) # 6 - 4 = 2

