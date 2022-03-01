from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

#########################################################
#                        ENCRYPTED                        #
#########################################################

#Se crea una funcion para cifrar una cadena de texto
def encrypt_file(original):

    # Leemos el archivo con la clave publica
    with open("public_key.pem", "rb") as f:
        recipient_public_key = f.read()

    # Cargamos la clave pública (instancia de clase RSA)
    key = RSA.importKey(recipient_public_key)

    #Instancia del cifrador asimétrico
    cipher_rsa = PKCS1_OAEP.new(key)

    #Encriptamos la cadena usando la clave pública
    enc_data = cipher_rsa.encrypt(original)

    with open("secreto_encrypted.txt", "wb") as encrypted_file:
        encrypted_file.write(enc_data)
    
    return print("El archivo se cifro correctamente") 

with open("secret.txt", "rb") as f:
    original = f.read()
    
encrypt_file(original)

