import math

# Se buscan dos números primos lo suficientemente grandes p y q ambos tienen que ser distintos.
global p; p = 11
global q; q = 3

# A partir de este número se obtiene n = p * q
global n; n = p*q

# Se calcula z donde z = (p - 1) * (q - 1)
global z; z = (p-1)*(q-1)

# Se elige un numero k, tal que sea co-primo de z, es decir que k y z 
# no tengan ningún valor divisor común mas que 1. Para este ejemplo ocuparemos k = 7
# La clave publica va a ser el conjunto de números (n,k)
global k; k = 7

# Se calcula el exponente privado de RSA d = inv (k, z)
# d= inv (7,20) =3
# La clave privada va a ser el conjunto de (n, d)
global d; d = 3

# Se crea la funcion de cifrado
def encrypt(msg):
    
    # Formula de cifrado C = M^k mod n y se imprime en pantalla
    global enc_data; enc_data = int(math.pow(msg,k) % n)
    return print("El mensaje cifrado es: ", enc_data)

# Se crea funcion de descifrado
def decrypt(enc_data):
    
    # Formula de descifrado M = C^d mod n y se imprime en pantalla
    dec_data = int(math.pow(enc_data,d) % n)
    return print("El mensaje descifrado es: ", dec_data);
   
def main():
    
    # Se le pide al usuairo ingresar un numero para realziar el cifrado
    msg = int(input("Ingresa el numero a cifrara: "))
    
    # Se manda a llamar a la funcion de cifrado
    encrypt(msg)
    
    #Se manda a llamar a la funcion de descifrado
    decrypt(enc_data)
    
if __name__ == '__main__':
    main()