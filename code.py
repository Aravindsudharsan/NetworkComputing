import os
import csv


#google hangouts

#converting pcapng file to csv ffile
'''os.system('tshark -r wireshark.pcapng -T fields -e frame.number -e _ws.col.Time -e _ws.col.Source -e _ws.col.Destination -e _ws.col.Protocol -e _ws.col.Length -e _ws.col.Info -e _ws.col.DeltaTime  -E header=y -E separator=, -E quote=d  > test1.csv')
os.system('tshark -r Data.pcapng -T fields -e frame.number -e _ws.col.Time -e _ws.col.Source -e _ws.col.Destination -e _ws.col.Protocol -e _ws.col.Length -e _ws.col.Info -e _ws.col.DeltaTime  -E header=y -E separator=, -E quote=d  > test2.csv')

#opening the  1st CSV file
port_output_new=[]
delta_time=[]
delta1_time=[]
delta2_time=[]
delta3_time=[]

delta_new_time=[]
delta1_new_time=[]
delta2_new_time=[]
delta3_new_time=[]
with open('test1.csv','rb') as file_csv:
	reader_output=csv.reader(file_csv)
	for row in reader_output:
		 temp_value=row[6]
		 port_output=row[6].split(' ')
		 port_output_new.append(port_output[0]) # putting the port numbers is a seperate list
		 # getting the delta time for all the ports
		 if '62456' in row[6]:
		 	delta_time.append(float(row[7]))
		 if '19305' in row[6]:
		 	delta1_time.append(float(row[7]))
		 if '52183' in row[6]:
		 	delta2_time.append(float(row[7]))
		 if '52437' in row[6]:
		 	delta3_time.append(float(row[7]))
# printing the delta time
print "delta time for 1st port",delta_time
print "delta time for 2nd port",delta1_time
print "delta time for 3rd port",delta2_time
print "delta time for 4th port",delta3_time

	

#opening the  2nd CSV file

port1_output_new=[]
with open('test2.csv','rb') as file1_csv:
	reader1_output=csv.reader(file1_csv)
	for row1 in reader1_output:
		 temp1_value=row1[6]
		 port1_output=row1[6].split(' ')
		 port1_output_new.append(port1_output[0]) # putting the port numbers in a seperate list
		 # getting the delta time for all the ports
		 if '62822' in row1[6]:
		 	delta_new_time.append(float(row1[7]))
		 if '19305' in row1[6]:
		 	delta1_new_time.append(float(row1[7]))
		 if '62456' in row1[6]:
		 	delta2_new_time.append(float(row1[7]))
		 if '52437' in row1[6]:
		 	delta3_new_time.append(float(row1[7]))
# printing the delta time
print "delta time for 1st port",delta_new_time
print "delta time for 2nd port",delta1_new_time
print "delta time for 3rd port",delta2_new_time
print "delta time for 4th port",delta3_new_time

# calculating the mean time for all and printing

sum1=0
sum2=0
sum3=0
sum4=0
sum5=0
sum6=0
sum7=0
sum8=0
for item in range(len(delta_time)):
	sum1=sum1+delta_time[item]
mean_time=sum1/len(delta_time)
print "mean time is", mean_time

for item in range(len(delta1_time)):
	sum2=sum2+delta1_time[item]
mean1_time=sum2/len(delta1_time)
print "mean time is", mean1_time

for item in range(len(delta2_time)):
	sum3=sum3+delta2_time[item]
mean2_time=sum3/len(delta2_time)
print "mean time is", mean2_time

for item in range(len(delta3_time)):
	sum4=sum4+delta3_time[item]
mean3_time=sum4/len(delta3_time)
print "mean time is", mean3_time

for item in range(len(delta_new_time)):
	sum5=sum5+delta_new_time[item]
mean4_time=sum5/len(delta_new_time)
print "mean time is", mean4_time

for item in range(len(delta1_new_time)):
	sum6=sum6+delta1_new_time[item]
mean5_time=sum6/len(delta1_new_time)
print "mean time is", mean5_time

for item in range(len(delta2_new_time)):
	sum7=sum7+delta2_new_time[item]
mean6_time=sum7/len(delta2_new_time)
print "mean time is", mean6_time

for item in range(len(delta3_new_time)):
	sum8=sum8+delta3_new_time[item]
mean7_time=sum8/len(delta3_new_time)
print "mean time is", mean7_time'''

# facebook

#converting pcapng file to csv ffile
'''os.system('tshark -r facebook.pcapng -T fields -e frame.number -e _ws.col.Time -e _ws.col.Source -e _ws.col.Destination -e _ws.col.Protocol -e _ws.col.Length -e _ws.col.Info -e _ws.col.DeltaTime  -E header=y -E separator=, -E quote=d  > test3.csv')
os.system('tshark -r aravindfacebook.pcapng -T fields -e frame.number -e _ws.col.Time -e _ws.col.Source -e _ws.col.Destination -e _ws.col.Protocol -e _ws.col.Length -e _ws.col.Info -e _ws.col.DeltaTime  -E header=y -E separator=, -E quote=d  > test4.csv')

#opening the  3rd CSV file
facebook_output_new=[]
facebook_time=[]
facebook1_time=[]


facebook_new_time=[]
facebook1_new_time=[]

with open('test3.csv','rb') as file2_csv:
	reader2_output=csv.reader(file2_csv)
	for row2 in reader2_output:
		 temp2_value=row2[6]
		 facebook_output=row2[6].split(' ')
		 facebook_output_new.append(facebook_output[0]) # putting the port numbers is a seperate list
		 # getting the delta time for all the ports
		 if '49238' in row2[6]:
		 	facebook_time.append(float(row2[7]))
		 if '57276' in row2[6]:
		 	facebook1_time.append(float(row2[7]))
		 
# printing the delta time
print "delta time for 1st port",facebook_time
print "delta time for 2nd port",facebook1_time

#opening the  4th CSV file

facebook1_output_new=[]
with open('test4.csv','rb') as file3_csv:
	reader3_output=csv.reader(file3_csv)
	for row3 in reader3_output:
		 temp3_value=row3[6]
		 facebook1_output=row3[6].split(' ')
		 facebook1_output_new.append(facebook1_output[0]) # putting the port numbers in a seperate list
		 # getting the delta time for all the ports
		 if '49238' in row3[6]:
		 	facebook_new_time.append(float(row3[7]))
		 if '57276' in row3[6]:
		 	facebook1_new_time.append(float(row3[7]))
# printing the delta time
print "delta time for 1st port",facebook_new_time
print "delta time for 2nd port",facebook1_new_time


# calculating the mean time for all and printing

facebook_sum1=0
facebook_sum2=0
facebook_sum3=0
facebook_sum4=0

for item in range(len(facebook_time)):
	facebook_sum1=facebook_sum1+facebook_time[item]
facebook_mean_time=facebook_sum1/len(facebook_time)
print "mean time is", facebook_mean_time

for item in range(len(facebook1_time)):
	facebook_sum2=facebook_sum2+facebook1_time[item]
facebook_mean1_time=facebook_sum2/len(facebook1_time)
print "mean time is", facebook_mean1_time

for item in range(len(facebook_new_time)):
	facebook_sum3=facebook_sum3+facebook_new_time[item]
facebook_mean2_time=facebook_sum3/len(facebook_new_time)
print "mean time is", facebook_mean2_time

for item in range(len(facebook1_new_time)):
	facebook_sum4=facebook_sum4+facebook1_new_time[item]
facebook_mean3_time=facebook_sum4/len(facebook1_new_time)
print "mean time is", facebook_mean3_time'''

#skype

os.system('tshark -r skype.pcapng -T fields -e frame.number -e _ws.col.Time -e _ws.col.Source -e _ws.col.Destination -e _ws.col.Protocol -e _ws.col.Length -e _ws.col.Info -e _ws.col.DeltaTime  -E header=y -E separator=, -E quote=d  > test5.csv')
os.system('tshark -r aravindskype.pcapng -T fields -e frame.number -e _ws.col.Time -e _ws.col.Source -e _ws.col.Destination -e _ws.col.Protocol -e _ws.col.Length -e _ws.col.Info -e _ws.col.DeltaTime  -E header=y -E separator=, -E quote=d  > test6.csv')

#opening the  1st CSV file
skype_output_new=[]
skype_time=[]
skype1_time=[]
skype2_time=[]
skype3_time=[]

skype_new_time=[]
skype1_new_time=[]

with open('test5.csv','rb') as file4_csv:
	reader4_output=csv.reader(file4_csv)
	for row4 in reader4_output:
		 temp4_value=row4[6]
		 skype_output=row4[6].split(' ')
		 skype_output_new.append(skype_output[0]) # putting the port numbers is a seperate list
		 # getting the delta time for all the ports
		 if '3478' in row4[6]:
		 	skype_time.append(float(row4[7]))
		 if '6652' in row4[6]:
		 	skype1_time.append(float(row4[7]))
		 if '21692' in row4[6]:
		 	skype2_time.append(float(row4[7]))
		 if '58826' in row4[6]:
		 	skype3_time.append(float(row4[7]))
# printing the delta time
print "delta time for 1st port",skype_time
print "delta time for 2nd port",skype1_time
print "delta time for 3rd port",skype2_time
print "delta time for 4th port",skype3_time

	

#opening the  2nd CSV file

skype1_output_new=[]
with open('test6.csv','rb') as file5_csv:
	reader5_output=csv.reader(file5_csv)
	for row5 in reader5_output:
		 temp5_value=row5[6]
		 skype1_output=row5[6].split(' ')
		 skype1_output_new.append(skype1_output[0]) # putting the port numbers in a seperate list
		 # getting the delta time for all the ports
		 if '6652' in row5[6]:
		 	skype_new_time.append(float(row5[7]))
		 if '21692' in row5[6]:
		 	skype1_new_time.append(float(row5[7]))
		 
# printing the delta time
print "delta time for 1st port",skype_new_time
print "delta time for 2nd port",skype1_new_time


# calculating the mean time for all and printing

skype_sum1=0
skype_sum2=0
skype_sum3=0
skype_sum4=0
skype_sum5=0
skype_sum6=0

for item in range(len(skype_time)):
	skype_sum1=skype_sum1+skype_time[item]
skype_mean_time=skype_sum1/len(skype_time)
print "mean time is", skype_mean_time

for item in range(len(skype1_time)):
	skype_sum2=skype_sum2+skype1_time[item]
skype_mean1_time=skype_sum2/len(skype1_time)
print "mean time is", skype_mean1_time

for item in range(len(skype2_time)):
	skype_sum3=skype_sum3+skype2_time[item]
skype_mean2_time=skype_sum3/len(skype2_time)
print "mean time is", skype_mean2_time

for item in range(len(skype3_time)):
	skype_sum4=skype_sum4+skype3_time[item]
skype_mean3_time=skype_sum4/len(skype3_time)
print "mean time is", skype_mean3_time

for item in range(len(skype_new_time)):
	skype_sum5=skype_sum5+skype_new_time[item]
skype_mean4_time=skype_sum5/len(skype_new_time)
print "mean time is", skype_mean4_time

for item in range(len(skype1_new_time)):
	skype_sum6=skype_sum6+skype1_new_time[item]
skype_mean5_time=skype_sum6/len(skype1_new_time)
print "mean time is", skype_mean5_time

temp_value=[]
#packet loss
# applying filter and converting to CSV file
os.system('tshark -r wireshark.pcapng -Y "tcp.analysis.lost_segment" -T fields -e frame.number -e _ws.col.Time -e _ws.col.Source -e _ws.col.Destination -e _ws.col.Protocol -e _ws.col.Length -e _ws.col.Info -e _ws.col.DeltaTime  -E header=y -E separator=, -E quote=d  > test7.csv')

os.system('tshark -r Data.pcapng -Y "tcp.analysis.lost_segment" -T fields -e frame.number -e _ws.col.Time -e _ws.col.Source -e _ws.col.Destination -e _ws.col.Protocol -e _ws.col.Length -e _ws.col.Info -e _ws.col.DeltaTime  -E header=y -E separator=, -E quote=d  > test8.csv')

os.system('tshark -r facebook.pcapng -Y "tcp.analysis.lost_segment" -T fields -e frame.number -e _ws.col.Time -e _ws.col.Source -e _ws.col.Destination -e _ws.col.Protocol -e _ws.col.Length -e _ws.col.Info -e _ws.col.DeltaTime  -E header=y -E separator=, -E quote=d  > test9.csv')

os.system('tshark -r aravindfacebook.pcapng -Y "tcp.analysis.lost_segment" -T fields -e frame.number -e _ws.col.Time -e _ws.col.Source -e _ws.col.Destination -e _ws.col.Protocol -e _ws.col.Length -e _ws.col.Info -e _ws.col.DeltaTime  -E header=y -E separator=, -E quote=d  > test10.csv')

os.system('tshark -r skype.pcapng -Y "tcp.analysis.lost_segment" -T fields -e frame.number -e _ws.col.Time -e _ws.col.Source -e _ws.col.Destination -e _ws.col.Protocol -e _ws.col.Length -e _ws.col.Info -e _ws.col.DeltaTime  -E header=y -E separator=, -E quote=d  > test11.csv')

os.system('tshark -r aravindskype.pcapng -Y "tcp.analysis.lost_segment" -T fields -e frame.number -e _ws.col.Time -e _ws.col.Source -e _ws.col.Destination -e _ws.col.Protocol -e _ws.col.Length -e _ws.col.Info -e _ws.col.DeltaTime  -E header=y -E separator=, -E quote=d  > test12.csv')
# printing the count from csv file
'''with open('test7.csv','rb') as loss_csv:
	loss_output=csv.reader(loss_csv)
	i=-1
	for row in loss_output:
		i=i+1
	print "packet loss of first application is",i'''

'''with open('test8.csv','rb') as loss1_csv:
	loss1_output=csv.reader(loss1_csv)
	i=-1
	for row in loss1_output:
		i=i+1
	print "packet loss of second file is",i'''

'''with open('test9.csv','rb') as loss2_csv:
	loss2_output=csv.reader(loss2_csv)
	i=-1
	for row in loss2_output:
		i=i+1
	print "packet loss of second application is",i'''

'''with open('test10.csv','rb') as loss3_csv:
	loss3_output=csv.reader(loss3_csv)
	i=-1
	for row in loss3_output:
		i=i+1
	print "packet loss of fourth file is",i'''

'''with open('test11.csv','rb') as loss4_csv:
	loss4_output=csv.reader(loss4_csv)
	i=-1
	for row in loss4_output:
		i=i+1
	print "packet loss of third application is",i'''

with open('test8.csv','rb') as loss5_csv:
	loss5_output=csv.reader(loss5_csv)
	i=-1
	for row in loss5_output:
		i=i+1
	print "packet loss of sixth file is",i
