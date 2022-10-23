import os

file_path = input()
output = (os.path.basename(file_path).split('/')[-1]).split('.')

print(f'File name: {output[0]}')
print(f'File extension: {output[1]}')
