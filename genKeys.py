from Crypto.PublicKey import RSA

#########################################################
#                GENERACIÓN DE LA CLAVE                 #
#########################################################

# Creacion de la funcion llamada rsa_genKeys para genarar el par de llaves RSA
def rsa_genKeys(bits):
    
    # Generación de llaves dependiendo del tamaño que el usuario 
    # escoga y se guardan en la variable key
    key = RSA.generate(bits)

    # Se exporta la llave privada y se guarda en la variable private_key
    private_key = key.export_key()

    # Se genera el archivo private_key.pem para guardar la llave privada
    with open("private_key.pem", "wb") as f:
        f.write(private_key)

    # Se exporta la llave publica y se guarda en la variable public_key
    public_key = key.public_key().export_key()

    # Se genera el archivo public_key.pem y se guarda la llave publica
    with open("public_key.pem", "wb") as f:
        f.write(public_key)
        
    # Se imprime en pantala que las llaves se crearon correctamente
    return print("Las llaves se crearon con exito")


def main():

    # Se pregunta al suaurio el tamaño de bits con el cual se generaran 
    # las llaves y se guardan en la variable bits
    bits = int(input("Ingrese el tamaño de las llaves: "))
    
    # Se ejecuta la funcion rsa_genKeys
    rsa_genKeys(bits)


if __name__ == '__main__':
    main()
