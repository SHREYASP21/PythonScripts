a=open('example.txt','a')
a.write('  rock')
a.write('   paper')
a.close()
with open("example.txt","r") as file:
    data=file.readlines()
    for line in data:
        words=line.split()
        print(words)



