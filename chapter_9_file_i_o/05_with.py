# f=open("myfile.txt")
# print(f.read())
# f.close()

#the same can be written using wwith statament like this:
with open ("file.txt") as f:
    print(f.read())# you do't have to explicitly close the file in here with  'with statement'