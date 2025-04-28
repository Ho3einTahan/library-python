import json
import os
import time

pathDir = './files'
pathFile = './files/data.json'

if not os.path.isdir(pathDir):
    os.mkdir(pathDir)

if not os.path.isfile(pathFile):
    with open(pathFile, 'w') as f:
        f.write('{"books": []}')

def addBook(bookName, author, addDate):
    with open(pathFile, 'r+') as file:
        content = file.read()
        
        if not content.strip():
            data = {"books": []}
        else:
            data = json.loads(content)

        data['books'].append({
            "bookName": bookName,
            "author": author,
            "addDate": addDate
        })

        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=4)

addBook("Python Basics", "Hossein Tahan",time.time())
    
    
# def removeBook():


# def showAllBook():
    

# def barrowBook():
    
    
# def ledBook():