from cryptography.fernet import Fernet


f = Fernet(b'2LmRk26wiVCyd3oaWH9QEDB_VPPSq2xfDYCUPwAqLH8=')


text = 'gAAAAABivxkYTKr6R8_Q3-dHyjq9T8hnwO-bnFyvHpsAkUfdIPN1FDIARrJ1B9hwJWTT2pAnb4o4pBp6fKQuuABcg8wYljzuFsE-f_rxoBXMmn2U1sJILF_TB2cjEknzBioazT_DpAggVJcypzNjXqQnuMch1ew1-fOuCTBUlSMg9ICSqdTs5YCeNQ76_Pk10TfAZGh89G7t5-iD98_Ui2aTuiOvQj9W4w=='

text_convert = text.encode('utf-8')
text_decrypt = f.decrypt(text_convert)
print(text_decrypt.decode('utf-8'))






'''
f = Fernet(b'G9AFRPKrA_jY5DFeEVvL8pg82-Q-A2bN-C46gGJtSaY=')

with open('hacker999.loong','r') as file:
	text = file.read()
	print(text)
	print(type(text))


text_convert = text.encode('utf-8')
print(text_convert)

text_decrypt = f.decrypt(text_convert)

print(text_decrypt)

with open('hacker999.docx','wb') as file:
	file.write(text_decrypt)
'''