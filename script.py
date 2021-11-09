import os
import csv

processed = "processed/"
raw = "raw/"


#if directory doesnt exists
if os.path.isdir(raw)==False or os.path.isdir(processed)==False:
	print("directory not found ('processed','raw')")
	os._exit(0)


#get array of all the files
files = os.listdir("raw")


duplicates = 0;

#array to hold all the emails
main_list = [];





print("Started processing...")
print('-----------')

for filename in files:

	

	#check if its s csv file
	if filename[-3:].lower() == "csv":

		#reset the varaiable
		emails=[
			["EMAILS"]
		]




		# reading csv file
		with open(raw+filename, 'r') as csvfile:
		    # creating a csv reader object
		    csvreader = csv.reader(csvfile)
		  
		    # extracting each data row one by one
		    for row in csvreader:
		    	#rows.append(row)

		    	#check length, found email
		    	if len(row)>0 and '@' in row[0]:
		    		#small case
		    		row[0] = row[0].lower()

		    		#check if email exists in main_list
		    		if row[0] in main_list:
		    			duplicates += 1
		    		else:
		    			main_list.append(row[0])
		    			emails.append([row[0]])


		# writing to csv file 
		with open(processed+filename, 'w', newline='') as csvfile: 
			# creating a csv writer object 
			csvwriter = csv.writer(csvfile) 
			    
			# writing the data rows 
			csvwriter.writerows(emails)


		print(processed+filename)
		
		    		
print('-----------')
print("Duplicate emails : "+str(duplicates))


input("Press enter to exit")