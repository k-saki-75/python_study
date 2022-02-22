import os
print(os.path.join('usr', 'bin', 'spam'))

my_files = ['account.txt', 'details.csv', 'invite.docx']
for filename in my_files:
    print(os.path.join('C:\\Users\\asweigart', filename))

print(os.getcwd())
os.chdir('C:\\Windows\\System32')
print(os.getcwd())



print(os.path.abspath('.'))

print(os.path.abspath('.\\Scripts'))

print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

print(os.path.relpath('C:\\Windows', 'C:\\'))
print(os.path.relpath('C:\\Windows', 'C:\\spam\\eggs'))
print(os.getcwd())
path = 'C:\\Windows\\System32\\calc.exe'
print(os.path.basename(path))
print(os.path.dirname(path))

