import re
sync_time=input("enter delay/undelay time in format hh:mm:ss:ms ")
file_name=input("enter file name: ")
# font=input("font style: ")
# color=input("font colour: ")
# font_style="<font color=\""+color+"\">"
# font_end="</font>"
decrease=False
if sync_time[0]=='-':
	decrease=True
print(decrease)
sync_time=[int(i) for i in sync_time.split(':')]
print(sync_time)
diff=0
if decrease:
	sync_time[0]=-sync_time[0]
for i in range(4):
	if sync_time[i]:
		if i<3:
			diff=diff+sync_time[i]*1000*pow(60,2-i)
		else:
			diff=diff+sync_time[i]

if decrease:
	diff=-diff
print(diff)

file = open(file_name, "r+")

print ("Name of the file: ", file.name,"open successfully")
lines = file.readlines()

new_file = open("new.srt", "w")
for line in lines :
	s=re.findall('\d+:\d+:\d+,\d+', line)
	if len(s)==2:
		#print(s)
		count=0
		for i in s:
			time=i.split(':')
			x,y=time[2].split(',')
			time[2]=x
			time.append(y)

			if len(time)==4:
				carry=0
				for j in range(3,-1,-1):
					time[j]=int(time[j])
				actual_time=0
				for i in range(4):
					if time[i]:
						if i<3:
							actual_time=actual_time+time[i]*1000*pow(60,2-i)
						else:
							actual_time=actual_time+time[i]
				actual_time=actual_time+diff
				hh=int(actual_time/(1000*pow(60,2)))
				actual_time=actual_time%(1000*pow(60,2))
				mm=int(actual_time/(1000*60))
				actual_time=actual_time%(1000*60)
				ss=int(actual_time/1000)
				ms=actual_time%1000
				new_time=str('{:02}'.format(hh))+":"+str('{:02}'.format(mm))+":"+str('{:02}'.format(ss))+","+str('{:03}'.format(ms))
				new_file.write(str(new_time))
				print(new_time)
				print(str(new_time))
				if count==0:
					new_file.write(' --> ')
			count=count+1
		new_file.write('\n')
	else:
		# try:
		# 	number=line.split('\n')
		# 	if int(number[0]):
		# 		new_file.write(str(number[0]))
		# except Exception as e:
				
			# new_file.write(font_style)
			new_file.write(line)
			# new_file.write(font_end)

new_file.close()
file.close()