#Muhammad Ahtir Saeed
#22-10337
import ast
import rsa
string_=input("Enter text: ")
#Generating Key
publicKey, privateKey = rsa.newkeys(256)

#Storing Private key in file named as my_rsa_private.pem
f=open('private.pem','wb')
f.write (privateKey.save_pkcs1('PEM'))
f.close()
###########################################################################################

encrypt_text = rsa.encrypt(string_.encode(),publicKey)
 

print("The text is encrypted:"+str(encrypt_text))
print()
encrypt_text_user_input=input("Copy paste above encrypted text and enter to decryt:") 

f1=open("private.pem",'rb')
priv=rsa.PrivateKey.load_pkcs1(f1.read())
decMessage = rsa.decrypt(ast.literal_eval(str(encrypt_text_user_input)), priv).decode()
 
print("Decrypted string:",decMessage)
