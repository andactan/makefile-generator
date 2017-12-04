import os

cwd = os.getcwd()

cFiles = {}
hFiles = {}

with open(os.path.join(cwd,'makefile'),'w') as out:
    for root, subFolders, files in os.walk(cwd):
        for file in files:
            fName, fExt = os.path.splitext(file)

            if fExt == '.c':
                cFiles[fName + '.o'] = {'path': (os.path.join(root, file)), 'fileName': file}

            elif fExt == '.h':
                hFiles[fName + '.o'] = (os.path.join(root, file))

    out.write('CC=gcc\n\n')

    out.write('all: hello\n\n')

    for key, item in cFiles.items():
        out.write(key + ': ' + ' ' + item['fileName']+'\n')
        out.write('\t$(CC) -c ' + item['path'] + '\n\n')

    out.write('hello: ')
    for key, item in cFiles.items():
        out.write(key + ' ')

    out.write('\n')
    out.write('\t$(CC) ')

    for key, value in cFiles.items():
        out.write(key + ' ')

    out.write('-o hello')


print cFiles
print hFiles