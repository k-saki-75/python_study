# import os, shelve, pprint

# print(os.path.join('usr', 'bin', 'spam'))

# my_files = ['account.txt', 'details.csv', 'invite.docx']
# for filename in my_files:
#     print(os.path.join('C:\\Users\\asweigart', filename))

# print(os.getcwd())
# os.chdir('C:\\Windows\\System32')
# print(os.getcwd())



# print(os.path.abspath('.'))

# print(os.path.abspath('.\\Scripts'))

# print(os.path.isabs('.'))
# print(os.path.isabs(os.path.abspath('.')))

# print(os.path.relpath('C:\\Windows', 'C:\\'))
# print(os.path.relpath('C:\\Windows', 'C:\\spam\\eggs'))
# print(os.getcwd())
# path = 'C:\\Windows\\System32\\calc.exe'
# print(os.path.basename(path))
# print(os.path.dirname(path))

# print(os.path.getsize('C:\\Windows\\System32\\calc.exe'))
# #print(os.listdir('C:\\Windows\\System32'))

# total_size = 0
# for filename in os.listdir('C:\\Windows\\System32'):
#     total_size = total_size + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))

# print(total_size)

# print(os.path.exists('C:\\Windows'))
# print(os.path.exists('C:\\some_made_up_floder'))
# print(os.path.isdir('C:\\Windows\\System32'))
# print(os.path.isfile('C:\\Windows\\System32'))
# print(os.path.isdir('C:\\Windows\\System32\\calc.exe'))
# print(os.path.isfile('C:\\Windows\\System32\\calc.exe'))
# print(os.path.exists('D:\\'))

#hello_file = open('C:\\github_pyhon\\python_study\\hello.txt')
#hello_content = hello_file.read()

# bacon_file = open('C:\\github_pyhon\\python_study\\bacon.txt', 'w')
# bacon_file.write('Hello world\n')
# bacon_file.close()
# bacon_file = open('C:\\github_pyhon\\python_study\\bacon.txt', 'a')
# bacon_file.write('Bancon is not a vegetable.')
# bacon_file.close()
# bacon_file =open('C:\\github_pyhon\\python_study\\bacon.txt')
# content = bacon_file.read()
# print(content)


# shelf_file = shelve.open('mydata')
# cats = ['Zopphie', 'Pooka', 'Simon']
# shelf_file['cats'] = cats
# print(type(shelf_file))
# print(shelf_file['cats'])
# print(list(shelf_file.keys()))
# print(list(shelf_file.values()))
# shelf_file.close()


# path = os.getcwd()

# print(path)

# cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
# print(pprint.pformat(cats))
# file_obj = open('myCats.py', 'w')
# file_obj.write('cats='+pprint.pformat(cats)+'\n')
# file_obj.close()

import myCats
print(myCats.cats)
print(myCats.cats[0])
print(myCats.cats[0]['name'])