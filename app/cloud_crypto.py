from cryptography.fernet import Fernet


KEY = Fernet.generate_key()

cipher = Fernet(KEY)



def encrypt_data(text:str):

    return cipher.encrypt(

        text.encode()

    ).decode()



def decrypt_data(data:str):

    return cipher.decrypt(

        data.encode()

    ).decode()