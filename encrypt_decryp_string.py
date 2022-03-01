from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import binascii

#########################################################
#                        ENCRYPTED                        #
#########################################################

#Se crea una funcion para cifrar una cadena de texto
def encrypt_string(string):
    
    # Trabajamos con bytes, codifcamos la cadena.
    bin_data = string.encode("utf-8")

    # Leemos el archivo con la clave publica
    with open("public_key.pem", "rb") as f:
        recipient_public_key = f.read()

    # Cargamos la clave pública
    key = RSA.importKey(recipient_public_key)

    # Instancia del cifrador asimétrico
    cipher_rsa = PKCS1_OAEP.new(key)

    # Encriptamos la cadena usando la clave pública
    global enc_data
    enc_data = cipher_rsa.encrypt(bin_data)

    return print("Encrypted:", binascii.hexlify(enc_data))

#########################################################
#                       DECRYPTED                       #
#########################################################

#Se crea una funcion para cifrar una cadena de texto
def decrypt_string(enc_data):

    # Leemos el archivo con la clave privada
    with open("private_key.pem", "rb") as f:
        recipient_private_key = f.read()

    # Cargamos la clave privada (instancia de clase RSA)
    key = RSA.importKey(recipient_private_key)

    # Instancia del cifrador asimétrico
    cipher_rsa = PKCS1_OAEP.new(key)

    # Desencriptamos la cadena usando la clave privada
    dec_data = cipher_rsa.decrypt(enc_data)

    # Decodificamos la cadena
    string_decrypt = dec_data.decode("utf-8")

    return print("Decrypted:", string_decrypt)
  
string = input("Escriba el texto a cifrara: ")
encrypt_string(string)
option_decrypt = input("Desea descifrar el mensaje? y/n ")
option_decrypt.lower()
if option_decrypt == "y" or option_decrypt == "yes":
    decrypt_string(enc_data)
    
    




