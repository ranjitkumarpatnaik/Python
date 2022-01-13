'''
===loop control statements===
=============================
Used to control the iterations of our loop.
    ***break,continue,pass***
    break= used to stop the iterations in our loop and not the script
    continue= continue will skip the statements inside it. 
    pass= you can add pass inside the incomplete block to instruct python to ignore that block instead of commenting.
'''

cnt=1
while True:
    print(cnt)
    if cnt==9:
        break
    cnt+=1


for each in range(1,11):
    if each==7:
        continue
        each+=1
        print(a)
    print(each)

for each in range(1,100):
    pass
