import json
x = open('folder directory')
data = json.load(x)
f = open("file.txt", "a")
for i in data:
 b = i.replace("file/d/","uc?id=")
 y = b.replace("/view?usp=sharing","&export=download")
 f.write(y+'\n')  
x.close()
f.close()


