# encrypt-decrypt.py
# pip install cryptography

from cryptography.fernet import Fernet

key = Fernet.generate_key()
print('KEY:',key)

f = Fernet(key) # OBJECT FERNET

text = 'สวัสดีจ้าาาา ข้อความจากลุงเองจ้าาา'

message = f.encrypt(text.encode('utf-8'))
print('===========Encrypt============')

print(message.decode('utf-8'))

print('==============================')



'''
key = Fernet.generate_key()
print('KEY:',key)

f = Fernet(key) # OBJECT FERNET

with open('homework.docx','rb') as file:
	docfile = file.read()

# message = f.encrypt(text.encode('utf-8'))
message = f.encrypt(docfile)
print('===========Encrypt============')
# print(message.decode('utf-8'))
print(message.decode('utf-8'))

with open('hacker999.loong','w') as file:
	file.write(message.decode('utf-8'))

print('==============================')



'''