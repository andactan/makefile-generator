import os, sys, re

queue = list()
directoryPath = sys.argv[1]
queue.append(directoryPath)

cwd = os.getcwd()
sourceFiles = {}
headerFiles = {}

for directory, subDirectories, files in os.walk(directoryPath):
    for file in files:
        name, ext = os.path.splitext(file)

        if ext == '.c':
            sourceFiles[file] = {'dir': directory}

        if ext == '.h':
            headerFiles[file] = {'dir': directory}

print sourceFiles
print headerFiles
# Extract internal structure of header files and get function names
# Check in which src files are header files included

includeRegex = re.compile(r"(#)(\s*)(include)(\s+)\"(.*?)\"")
dependencies = {}

for sourceFile, specs in sourceFiles.items():
    for line in open(os.path.join(specs["dir"], sourceFile), 'r+').readlines():
        #print line
        match = includeRegex.search(line)
        if(match):
            if(sourceFile in dependencies.keys()):
                dependencies[sourceFile].append(str(match.group(5)))
            else:
                dependencies[sourceFile] = [str(match.group(5))]


for headerFile, specs in headerFiles.items():
    for line in open(os.path.join(specs["dir"], headerFile), 'r+').readlines():
        #print line
        match = includeRegex.search(line)
        if(match):
            if(headerFile in dependencies.keys()):
                dependencies[headerFile].append(str(match.group(5)))
            else:
                dependencies[headerFile] = [str(match.group(5))]

print dependencies
with open(directoryPath + '\Makefile', 'w') as makefile:
    makefile.write("CC=gcc\n")
    targets = []
    for sourceFile, specs in sourceFiles.items():
        #check dependencies
        split = sourceFile.split(".")
        target = split[0] + ".o"
        targets.append(target)

        makefile.write(target + ":")
        makefile.write("\n\t")
        makefile.write("$(CC)")
        if(dependencies[sourceFile]):
            for dependency in dependencies[sourceFile]:
                makefile.write(" -I " + headerFiles[dependency]["dir"])

        makefile.write(" -c "  + specs["dir"] + "\\" + sourceFile)
        makefile.write("\n")

    makefile.write("all: " + " ".join(targets) + "\n\t")
    makefile.write("$(CC) " + " ".join(targets) + " -o hello")


