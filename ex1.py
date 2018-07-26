from lib.stack import Stack
s = Stack()

def dec_to_bin(dec):
    binary=0
    while (dec!=0):
        s.push(dec%2)
        dec=dec//2
    while( 	s.size()!=0 ):
        pop=s.pop()
        binary+=(10**s.size())*pop
    return binary

print(dec_to_bin(42))   # 回傳 101010
print(dec_to_bin(100))  # 回傳 1100100