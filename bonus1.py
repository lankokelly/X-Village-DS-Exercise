from lib.stack import Stack
s = Stack()

def base_converter(dec_number, base):
    digit="0123456789ABCDE"
    
    while (dec_number != 0):
        number = digit [ dec_number % base ]
        dec_number = dec_number//base
        s.push(number)
    string=""
    while( 	s.size()!=0 ):
        pop = s.pop()
        string += str(pop)
    return string


print( base_converter(1000, 16 ))  # 回傳 3E8
print( base_converter(700, 12) )  # 回傳 4A4