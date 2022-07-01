import os
import time
import shutil

path = r'C:\Users\Uncle Engineer\Desktop\HK\Trojan-Test'

file = os.path.join(path,'homework.docx')

file_name = 'homework3.docx'
for i in range(4,10):
	copyfile = os.path.join(path,file_name)
	shutil.copyfile(file,copyfile)
	file_name = 'homework{}.docx'.format(i)
	print(file_name)
	time.sleep(2)