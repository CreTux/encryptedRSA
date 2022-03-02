from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

#########################################################
#                        ENCRYPTED                      #
#########################################################

# Se crea una funcion llamada encrypt_file que acepte una varaible llamada original
#  como argumento para cifrar un archivo


def encrypt_file(original):

    # Leemos el archivo public_key.pem que contienela clave publica y se alamcena
    # en la variable recipient_public_key
    with open("public_key.pem", "rb") as f:
        recipient_public_key = f.read()

    # Cargamos la clave pública en la variable key
    key = RSA.importKey(recipient_public_key)

    # Instancia del cifrador asimétrico con la llave publica y se alamcena en
    # la variable cipher_rsa
    cipher_rsa = PKCS1_OAEP.new(key)

    # Aplicamos el algoritmo de cifrado al archivo  con la llave publica y se almacena
    # en la variable enc_data
    enc_data = cipher_rsa.encrypt(original)

    # Se genera un archivo con el nombre secreto_encrypted.txt que contiene el resultado
    # del archivo cifrado
    with open("secreto_encrypted.txt", "wb") as encrypted_file:
        encrypted_file.write(enc_data)

    # Se imprime en pantalla que ela rchivo se cifro correctamente
    return print("El archivo se cifro correctamente")


def main():

    # Se inicializa la variable global original que contendra el archivo a cifrar
    global original

    # Se lee el archivo original llamado secreto.txt y se almacena en la variable original
    with open("secret.txt", "rb") as f:
        original = f.read()

    # Se ejecuta la funcion encrypt_file con la variable original como argumento
    encrypt_file(original)


if __name__ == '__main__':
    main()
