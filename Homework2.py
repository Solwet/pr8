def Oct(a):
    return oct(a)[2::]
def Bin(a):
    return bin(a)[2::]
a=int(input("Введите число"))
print(Oct(a),Bin(a))