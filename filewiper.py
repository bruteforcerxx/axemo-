import json

file = input('Input file to wipe: ')

file_update = open(file, 'w')
json.dump([], file_update)
file_update.close()

print(f'{file} file cleared successfully')
