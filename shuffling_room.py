import json,random

with open("oldData.json","r") as f:
    oldDetails=json.load(f)
i=0
j=1
names_list=[]
while i<len(oldDetails):
    roomWiselist=oldDetails[i][str(j)]
    i=i+1
    j=int(j+1)
    k=0
    while k<len(roomWiselist):
        names_list.append(roomWiselist[k]["name"])
        k=k+1
duplicate_names=names_list.copy()
z=1
ouput_dic={}
while z<=4:
    ouput_dic[str(z)]=[]
    m=0
    list2=[1,2,3,4,5,6,7,8,9,10]
    duplicate_bed_no=list2.copy()
    while m<len(list2):
        inner_dic={}
        random_name=random.choice(duplicate_names)
        duplicate_names.remove(random_name)
        inner_dic["name"]=random_name
        inner_dic["room_no"]=z
        random_bed_no=random.choice(duplicate_bed_no)
        duplicate_bed_no.remove(random_bed_no)
        inner_dic["bed_no"]=random_bed_no
        if random_bed_no%2==0:
            inner_dic["bed_position"]="upper"
        else:
            inner_dic["bed_position"]="down"

        m=m+1
        ouput_dic[str(z)].append(inner_dic)
    z=int(z)+1
with open("shuffeld_room.json","w")as f:
    json.dump(ouput_dic,f,indent=4)

    print("jyoti")
