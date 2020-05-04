
import math

#parameters in the question
seed=1234567
a=7**5
c=0
m=(2**31)-1

randomNumbers=[]

def generateRandom():
    global seed
    seed=(a*seed+c)%m
    return round(seed/m,3)

for i in range(100):
    
    randomNumbers.append(generateRandom())

copyrandomNumbers=randomNumbers.copy()
randomNumbers.sort()

print(randomNumbers)


#this part here is for kolmogrov-smirnov test


dpluses=[]                                                      #array to store all d+ values
dnegatives=[]                                                   #array to store all d- values
for i in range(len(randomNumbers)):
    dpluses.append(((i+1)/len(randomNumbers))-randomNumbers[i]) #i in the for loop starts from 0 thats why i need +1 here
    dnegatives.append(randomNumbers[i]-((i)/len(randomNumbers)))   #i in the for loop starts from 0 thats why i dont need -1 here
dpluses.sort()
dnegatives.sort()
dplus = dpluses[len(randomNumbers)-1]
dnegative = dnegatives[len(randomNumbers)-1]
d=max(dplus,dnegative)

dalpha=1.36/math.sqrt(len(randomNumbers)) #alpha value

if(dalpha>d):
    print("numbers are uniform for alpha level of 0.05")
else:
    print("numbers are not uniform for alpha level of 0.05")

print("d𝛼 = ",dalpha)
print("d = ",d)


#this part is for runs up and runs down test
currentRunType=None
runCount=0

#loop for counting runs
for i in range(1,len(copyrandomNumbers)):
    num=copyrandomNumbers[i]
    if currentRunType!=None:
        if (num>copyrandomNumbers[i-1]):
            if(currentRunType=="-"):
                currentRunType="+"
                runCount+=1
        else:
            if(currentRunType=="+"):
                currentRunType="-"
                runCount+=1
    else:                                   #
        if(num>copyrandomNumbers[i-1]):
            currentRunType="+"
        else:
            currentRunType="-"
        runCount+=1


meana=((2*len(randomNumbers))-1)/3          #mean of a
vara=((16*len(randomNumbers))-29)/90        #variance of a
z=1.96                                      #z value that we need to compare with
z0=(runCount-meana)/math.sqrt(vara)

if (z0>-z and z0<z):
    print("numbers are independent for alpha level of 0.05")
else:
    print("numbers are not independent for alpha level of 0.05")
print("z = ",z)
print("z0 = ",z0)


