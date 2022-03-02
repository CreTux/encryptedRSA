from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

#########################################################
#                       DECRYPTED                      #
#########################################################

# Se crea una funcion llamada decrypt_file  que acepte una varaible llamada encrypted
#  como argumento para descifrar un archivo


def decrypt_file(encrypted):

    # Leemos el archivo private_key.pem que contienela clave privada y se alamcena
    # en la variable recipient_private_key
    with open("private_key.pem", "rb") as f:
        recipient_private_key = f.read()

    # Cargamos la clave privada en la variable key
    key = RSA.importKey(recipient_private_key)

    # Instancia del descifrador asimétrico con la llave privada y se alamcena en
    # la variable cipher_rsa
    cipher_rsa = PKCS1_OAEP.new(key)

    # Aplicamos el algoritmo de descifrado al archivo  con la llave privada y se almacena
    # en la variable dec_data
    dec_data = cipher_rsa.decrypt(encrypted)

    # Se genera un archivo con el nombre secreto_decrypt.txt que contiene el resultado
    # del archivo descifrado
    with open('secret_decrypt.txt', 'wb') as dec_file:
        dec_file.write(dec_data)

    # Se imprime en pantalla que ela rchivo se descifro correctamente
    return print("El archivo se descifro correctamente")


def main():

    # Se inicializa la variable global encrypted que contendra el archivo a descifrar
    global encrypted

    # Se lee el archivo cifrado llamado secreto_encrypted.txt y se almacena en la variable encrypted
    with open("secreto_encrypted.txt", "rb") as f:
        encrypted = f.read()

    # Se ejecuta la funcion decrypt_file con la variable encrypted como argumento
    decrypt_file(encrypted)


if __name__ == '__main__':
    main()
