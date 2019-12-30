import os, re, argparse
files = []
matches = []
insideFile = []
extensions = ['txt','docx','doc','php','c','html','css','json','py','pdf','xml','js','java','jsp']
def changeDir(path):
    try:
        os.chdir(path)
        checkdirs(os.getcwdb().decode())
    except:
        pass
def checkdirs(path):
    subfolders = [f.path for f in os.scandir(path)]
    for sub in subfolders:
        if os.path.isdir(sub):
            changeDir(sub)
        else:
            files.append(sub)
def checkName(file, nameOfFile):
    file = str(file).split('\\')[-1]
    match = re.search(r"(?i)" + str(nameOfFile), file)
    if match is not None:
        matches.append(file)
def checkFile(filePath,key):
    ext = os.path.splitext(filePath)[1]
    ext=ext.replace(".","")
    if ext in extensions:
        a=open(filePath, 'r',encoding="ascii", errors="surrogateescape").read().find(key)
        if a!=-1:
            insideFile.append(filePath)
if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--path", required=True, help="The path of dirs you'd like to search")
    ap.add_argument("-n", "--name", required=False, help="The name of file you'd like to search")
    ap.add_argument("-k", "--key", required=False, help="The key for searching inside the files")
    args = vars(ap.parse_args())
    changeDir(args["path"])
    for file in files:
        if args["name"] is not None:
            checkName(file, args["name"])
        if args["key"] is not None:
            checkFile(file,args["key"])
    print("FILES:")
    if len(matches) == 0:
        print("There is no matches!!")
    else:
        for match in matches:
            print(match)
    print("--------------------------------------------------------------")
    print("KEY:")
    if len(insideFile) ==0:
        print("The key couldn't found!")
    else:
        for ins in insideFile:
            print(ins)