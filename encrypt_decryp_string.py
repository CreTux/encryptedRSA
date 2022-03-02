from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import binascii

#########################################################
#                        ENCRYPTED                      #
#########################################################

# Se crea una funcion llamada encrypt_string que acepte una variable llamada string como argumento
# como entrada para cifrar una cadena de texto


def encrypt_string(string):

    # Como vamos a trabajar con bits, codificamos la cadena (utf-8) y la
    # guardamos en la variable bin_data
    bin_data = string.encode("utf-8")

    # Leemos el archivo public_key.pem con la clave publica y se alamcena en la variable
    # recipient_public_key
    with open("public_key.pem", "rb") as f:
        recipient_public_key = f.read()

    # Cargamos la clave pública a la variable key
    key = RSA.importKey(recipient_public_key)

    # Instancia del cifrador asimétrico con la llave publica y se alamcena en
    # la variable cipher_rsa
    cipher_rsa = PKCS1_OAEP.new(key)

    # Apicacion del algoritmo de cifrado a  la cadena usando la clave pública y se
    # alamavcena en la variable global enc_data, para que la funcion de descifrado
    # pueda ocuparla.
    global enc_data
    enc_data = cipher_rsa.encrypt(bin_data)

    # Imprimimos en pantalla el codigo cifrado, en hexadecimal con ayuda de la
    # librera binascii
    return print("Encrypted:", binascii.hexlify(enc_data))

#########################################################
#                       DECRYPTED                       #
#########################################################

# Se crea una funcion llamada decrypt_string que acepte una variable llamada enc_data como argumento
# como entrada para descifrar la cadena de texto


def decrypt_string(enc_data):

    # Leemos el archivo private_key.pem con la clave privada y se almacena en la variable
    # recipient_private_key
    with open("private_key.pem", "rb") as f:
        recipient_private_key = f.read()

    # Cargamos la clave privada a la variable key
    key = RSA.importKey(recipient_private_key)

    # Instancia del cifrador asimétrico con la llave privada y se alamcena en
    # la variable cipher_rsa
    cipher_rsa = PKCS1_OAEP.new(key)

    # Aplicamos el algoritmo de descifrado a la variable enc_data usando la clave privda
    # y se alamcena en la variable dec_data
    dec_data = cipher_rsa.decrypt(enc_data)

    # Ya que estamos trabajando con bits decodificamos la cadena  usando utf y se almacena
    # en la variable string_decrypt
    string_decrypt = dec_data.decode("utf-8")

    # Imprimimos en pantalla el mensjae descifrado
    return print("Decrypted:", string_decrypt)


def main():

    # Se le pide al usuario ingresar una cadena de texto que se va a cifrar
    string = input("Escriba el texto a cifrara: ")

    # Se ehecuta la funcion encrypt_string
    encrypt_string(string)

    # Se impime en pantalla que el usuario tome la opcion de descifrar o no
    # la cadena con apciones de y/n
    option_decrypt = input("Desea descifrar el mensaje? y/n ")

    # La respuesta se convierte a minusculas para evitar errores
    option_decrypt.lower()

    # Se evalua la respuesta con la funcion if
    if option_decrypt == "y" or option_decrypt == "yes":

        # Si la la respuesta es verdaddera se ejcuta la funcion decrypt_string
        decrypt_string(enc_data)


if __name__ == '__main__':
    main()
