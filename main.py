import json
import os
import time

pathDir = './files'
pathFile = pathDir+'/data.json'

os.makedirs(pathDir, exist_ok=True)


if not os.path.isfile(pathFile):
    with open(pathFile, 'w') as file:
        json.dump({"books": []}, file, indent=4)

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
        file.close()

addBook("Python Basics", "Hossein Tahan",time.time())
 
    
# def removeBook():


# def showAllBook():
    

# def barrowBook():
    
    
# def ledBook():