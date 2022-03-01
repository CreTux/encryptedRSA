from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

#########################################################
#                       DECRYPTED                      #
#########################################################

#Se crea una funcion para cifrar una cadena de texto
def decrypt_file(encrypted):
    
    # Leemos el archivo con la clave privada
    with open("private_key.pem", "rb") as f:
        recipient_private_key = f.read()

    # Cargamos la clave privada (instancia de clase RSA)
    key = RSA.importKey(recipient_private_key)

    # Instancia del cifrador asimétrico
    cipher_rsa = PKCS1_OAEP.new(key)

    # Desencriptamos la cadena usando la clave privada
    dec_data = cipher_rsa.decrypt(encrypted)

    with open('secret_decrypt.txt', 'wb') as dec_file:
        dec_file.write(dec_data)
    
    return print("El archivo se descifro correctamente")
        
with open("secreto_encrypted.txt", "rb") as f:
    encrypted = f.read()
    
decrypt_file(encrypted)