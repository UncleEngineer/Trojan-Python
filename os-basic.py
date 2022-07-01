import os
import random
import time
import shutil

path = r'C:\Users\Uncle Engineer\Desktop\HK\Trojan-Test'

folder_list = os.listdir(path)

print(folder_list)

result_folder = []
result_file = []


for fd in folder_list:
	check = fd.split('.')
	if len(check) > 1:
		#print('File: ',fd)
		result_file.append(fd)
	else:
		#print('Folder: ',fd)
		result_folder.append(fd)

print('FD:',result_folder)
print('FL:',result_file)

# Initialize
file_dict = {}

for f in result_file:
	select = random.choice(result_folder)
	folderpath = os.path.join(path,select)
	filepath = os.path.join(folderpath,f) # output
	current = os.path.join(path,f)
	#print(current,'---->',filepath)
	file_dict[f] = {'current':current,'next':filepath}

while True:
	for fk,fv in file_dict.items():
		current = fv['current']
		nextpath = fv['next']
		shutil.move(current,nextpath)

		select = random.choice(result_folder)
		folderpath = os.path.join(path,select)
		file_next = os.path.join(folderpath,fk)
		file_dict[fk]['current'] = nextpath
		file_dict[fk]['next'] = file_next
	time.sleep(2)