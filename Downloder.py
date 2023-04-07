import requests

def download(link,name):
    file = requests.get(link)
    if file.status_code != 200:
        return False
    f = open(name,"wb")
    f.write(file.content)
    f.close()
    return True

link = input(" Link : ")
name = input(" Name : ")

result = download(link,name)
if result:
    print ("Ok !")
else:
    print("Error !")