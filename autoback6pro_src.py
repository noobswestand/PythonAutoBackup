import os
from shutil import copy2

users=next(os.walk('C:\\Users\\'))[1]

#remove baddies
bad=["All Users","Default","Default User","Public"]
for u in bad:
    users.remove(u)

print(users)

#go through + find files
valid=[]
docs=["Documents","Downloads","Desktop"]
docignore=["desktop.ini"]
_dir="C:/backups/"
for u in users:
    os.mkdir(_dir+u+"/")
    files=[]
    for d in docs:
        for x in os.walk('C:\\Users\\'+u+'\\'+d):
            for f in x[2]:
                if f not in docignore:
                    print(x[0]+'\\'+f)
                    files.append(x[0]+'\\'+f)
                    s=os.path.getsize(x[0]+'\\'+f)
                    copy2(x[0]+'\\'+f,_dir+u+'\\'+d+'\\'+f)
    if not files:
        os.rmdir(_dir+u+"/")
                
    
