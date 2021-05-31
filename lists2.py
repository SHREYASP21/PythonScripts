import random
olympic_boxers=['Mary kom','Nicola Adams','Claressa Shields','Marlen Esparza','Natasha Jones','Ren Cancan','Savannah Marshall','Mary spencer']
newplayer={}
for a in range(len(olympic_boxers)//2):
    newplayer[a+1]=(olympic_boxers.pop(random.randrange(len(olympic_boxers))),olympic_boxers.pop(random.randrange(len(olympic_boxers))))