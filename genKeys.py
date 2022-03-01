from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


#########################################################
#                GENERACIÓN DE LA CLAVE                 #
#########################################################

def rsa_genKeys(bits):
    key = RSA.generate(bits)

    private_key = key.export_key()

    with open("private_key.pem", "wb") as f:
        f.write(private_key)
    
    public_key = key.public_key().export_key()

    with open("public_key.pem", "wb") as f:
        f.write(public_key)
    
    return print("Las llaves se crearon con exito")

bits = int(input("Ingrese el tamaño de las llaves: "))
rsa_genKeys(bits)
    


