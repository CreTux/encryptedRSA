import math
 
message = int(input("Enter the message to be encrypted: ")) 
 
p = 3
q = 11
e = 7
z = (p-1)*(q-1)
k = 3

n = p*q
 
def encrypt(message):
    en = math.pow(message,e)
    c = en % n
    print("Encrypted Message is: ", c)
    return c
 
print("Original Message is: ", message)
c = encrypt(message)

def decrypt(c):
    dec = math.pow(c,k)
    d = dec % n
    print("El mensaje descifrado es: ", d);
    return d


d = decrypt(c)
