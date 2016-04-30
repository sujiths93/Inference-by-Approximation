import sys
import numpy
mode=sys.argv[1]
num_of_samples=sys.argv[2]
num_of_samples=int(num_of_samples)
list_of_events=[]

dic={}
#toplological order
topo=["B","E","A","J","M"]
#To store the tables
dic["B"]={"T":0.001}
dic["E"]={"T":0.002}
dic["A"]={"TT":0.95,"TF":0.94,"FF":0.001,"FT":0.29}
dic["J"]={"T":0.9,"F":0.05}
dic["M"]={"T":0.7,"F":0.01}
numerator_dic={}
denominator_dic={}
res_prior=0.0
evi=[]
que=[]

#Get the inputs for the program
print("INPUT")
e=input()
num_of_evidence,num_of_query=e.split()

for i in range(int(num_of_evidence)):
    temp=input().upper()
    evi.append(temp)
for i in range(int(num_of_query)):
    temp=input().upper()
    que.append(temp)

for i in evi:
    k,v=i.split()
    denominator_dic[topo.index(k)]=v


def result(num,denom):
    if denom==0:
        summ=0.0
    else:
        summ=(float(num)/float(denom))
    print(summ)

def counting(samples,numerator_dic,isLikeliHood):

    num=0
    denom=0
    for s in samples:
        n=0
        for key in numerator_dic:
            if s[key]!=numerator_dic[key]:
                break
            else:
                n+=1

        if n==len(numerator_dic):
            if isLikeliHood :
                num+=s[5]
            else:
                num+=1
        d=0
        for key in denominator_dic:
            if s[key]!=denominator_dic[key]:
                break
            else:
                d+=1

        if d==len(denominator_dic):
            if isLikeliHood:
               denom+=s[5]
            else:
                denom+=1
    result(num,denom)


def prior_sampling(num_of_samples):
    samples=[]

    #To generate samples in the given topological order

    for i in range(num_of_samples):
        sample=[]
        for j in topo:
            r=numpy.random.uniform(0,1)
            if j=="A":
                key=sample[0]+sample[1]

            elif j=="J" or j=="M":
                key=sample[2]
            else:
                key="T"

            if r<=dic[j][key]:
                sample.append("T")
            else:
                sample.append("F")

        samples.append(sample)


    for q in que:
        numerator_dic={}
        for i in evi:
            k,v=i.split()
            numerator_dic[topo.index(k)]=v
        numerator_dic[topo.index(q)]="T"
        counting(samples,numerator_dic,False)

def rejection_sampling(num_of_samples):
    samples=[]
    for i in range(num_of_samples):
        sample=[]
        for j in topo:
            r=numpy.random.uniform(0,1)
            if j=="A":
                key=sample[0]+sample[1]

            elif j=="J" or j=="M":
                key=sample[2]
            else:
                key="T"

            if r<=dic[j][key]:
                sample.append("T")
            else:
                sample.append("F")
        d=0
        for key in denominator_dic:
            if sample[key]!=denominator_dic[key]:
                break
            else:
                d+=1
        if d==len(denominator_dic):
            samples.append(sample)

    for q in que:
        numerator_dic={}
        for i in evi:
            k,v=i.split()
            numerator_dic[topo.index(k)]=v
        numerator_dic[topo.index(q)]="T"
        counting(samples,numerator_dic,False)


def likeliHood_sampling(num_of_samples):
    global evi
    samples=[]
    eviDict={}
    for i in evi:
        arr=i.split(" ")
        eviDict[arr[0]]=arr[1]
    #To generate samples in the given topological order

    for i in range(num_of_samples):
        sample=[]
        weight=1
        for j in topo:
            r=numpy.random.uniform(0,1)

            if j=="A":
                key=sample[0]+sample[1]
                if eviDict.__contains__(j):
                        prob = dic[j][key]
                        sample.append(eviDict[j])
                        if eviDict[j] == "T":
                            weight = weight * prob
                        else:
                            weight = weight * (1 - prob)
                        continue


            elif j=="J" or j=="M":
                key=sample[2]
                if eviDict.__contains__(j):
                        prob = dic[j][key]
                        sample.append(eviDict[j])
                        if eviDict[j] == "T":
                            weight = weight * prob
                        else:
                            weight = weight * (1 - prob)
                        continue
            else:
                key="T"
                if eviDict.__contains__(j):
                    prob = dic[j]["T"]
                    sample.append(eviDict[j])
                    if eviDict[j] == "T":
                        weight = weight * prob
                    else:
                        weight = weight * (1 - prob)
                    continue

            if r<=dic[j][key]:
                sample.append("T")
            else:
                sample.append("F")
        sample.append(weight)
        samples.append(sample)


    for q in que:
        numerator_dic={}
        for i in evi:
            k,v=i.split()
            numerator_dic[topo.index(k)]=v
        numerator_dic[topo.index(q)]="T"
        counting(samples,numerator_dic,True)


if(mode=="p"):
    prior_sampling(num_of_samples)
if(mode=="r"):
    rejection_sampling(num_of_samples)
if(mode=="l"):
    likeliHood_sampling(num_of_samples)