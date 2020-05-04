
import math

#parameters in the question
seed=123457
a=7**5
c=0
m=(2**31)-1

randomNumbers=[]

#function to create random numbers
def generateRandom():
    global seed
    seed=(a*seed+c)%m
    return round(seed/m,3)

for i in range(100):
    
    randomNumbers.append(generateRandom())

copyrandomNumbers=randomNumbers.copy()
randomNumbers.sort()

print(copyrandomNumbers)



#this part here is for kolmogrov-smirnov test


dpluses=[]                                                          #array to store all d+ values
dnegatives=[]                                                       #array to store all d- values
for i in range(len(randomNumbers)):
    dpluses.append(((i+1)/len(randomNumbers))-randomNumbers[i])     #i in the for loop starts from 0 thats why i need +1 here
    dnegatives.append(randomNumbers[i]-((i)/len(randomNumbers)))    #i in the for loop starts from 0 thats why i dont need -1 here


dpluses.sort()                                                      #sorting the array so we can get the max
dnegatives.sort()                                                   #sorting the array so we can get the max
dplus = dpluses[len(randomNumbers)-1]                               #getting the max         
dnegative = dnegatives[len(randomNumbers)-1]                        #getting the max
d=max(dplus,dnegative)                                              #getting the max

dalpha=1.36/math.sqrt(len(randomNumbers))                           #alpha value

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
    if currentRunType!=None:                #if it is not the first 2 elements this block runs

        if (num>copyrandomNumbers[i-1]):    #checks if the current element is greater than the previous element
            if(currentRunType=="-"):        #then checks if it runs down if it runs down it means now its running up
                
                currentRunType="+"          #thats why we change the run type

                runCount+=1                 #and increment the run count
            #there is not a else block because
            #if current run type is up we are continuing the run and there is no change in the run type
        
        else:                               #if previous number is greater than the current element 

            if(currentRunType=="+"):        #if it is running up that means now it started to run down
                currentRunType="-"          #so we change the run type and increment the counter
                runCount+=1
            #there is not a else block because
            #if current run type is down we are continuing the run and there is no change in the run type

    else:                                   # if we are checking the first 2 elements then this else block runs
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


