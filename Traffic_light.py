total_time=""
intersection=""
streets=''
cars=""
index=0
master_dic=dict()
routes=list()
var=input("Enter the filename: ")


with open(var + ".txt") as fh:
	for line in fh:
		temp_list=line.strip().split()
		if index==0:
			total_time=int(temp_list[0])
			intersection=int(temp_list[1])
			streets=int(temp_list[2])
			cars=int(temp_list[3])
		elif index>0 and index<=streets:
			temp_lis=[]
			temp_lis.append(temp_list[0])
			temp_lis.append(temp_list[1])
			temp_lis.append(temp_list[3])
			master_dic[temp_list[2]]=temp_lis
		else:
			temp_list2=list()
			for i in range(1,(int(temp_list[0])+1)):
				temp_list2.append(temp_list[i])
			routes.append(temp_list2)
		index=index+1
#print(routes)
#print(master_dic)
index=0



master_interaction=list()
for route in routes:
	node=list()
	time=0
	for index in range(0,(len(route)-1)):
		if index==0:
			node.append(master_dic[route[index]][1])
			if (master_dic[route[index]][1]) not in master_interaction:
				master_interaction.append(master_dic[route[index]][1])
		else:
			node.append(master_dic[route[index]][1])
			time+=int(master_dic[route[index]][2])
			if (master_dic[route[index]][1]) not in master_interaction:
				master_interaction.append(master_dic[route[index]][1])
	time+=int(master_dic[route[(len(route)-1)]][2])


	#print(node)
	#print(time)
# master_interaction.pop(-1)
#print(master_interaction)
incoming=[0]*intersection
street=list()
for i in range(intersection):
	street.append([])
for keys in master_dic:
	for i in range(intersection):
		if int(master_dic[keys][1])==i:
			incoming[i]+=1
			street[i].append(keys)

print(incoming)

print(street)
f1=open(var+"_output.txt","w+")
# f1.writelines(str(len(master_interaction))+'\n')
f1.writelines((str(len(master_interaction)),'\n'))
for i in range(len(master_interaction)):
    f1.writelines(str(master_interaction[i])+'\n')
    f1.writelines(str(incoming[int(master_interaction[i])])+'\n')
    for i2 in street[int(master_interaction[i])]:
    	f1.writelines(str(i2)+' ')
    	f1.writelines(str(incoming[int(master_interaction[i])])+'\n')
# f1.writelines((len(master_interaction),'\n'))
# f1.writelines(str(time))
f1.close()
