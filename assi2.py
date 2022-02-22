import pandas
import numpy
import matplotlib.pyplot as pyplot

#importing our csv
dataset  = pandas.read_csv("elections.csv")
#print(dataset["VCF0704A"].describe())
dataset = dataset.reset_index()

#the next lines create a new dataframe to visualize the data
newframe = pandas.DataFrame()
#add stuff to the newframe 
for x in range(len(dataset)):
	year = dataset.at[x,"VCF0004"]
	#only selecting dependent variables with data
	if((dataset.at[x,"VCF0704A"] == 1 or dataset.at[x,"VCF0704A"] == 2)):
		print("yes")
		print(x)
		print(dataset.at[x,"VCF0704A"])
		#next 2 lines assign a dummy variable to the person's vote
		val = dataset.at[x,"VCF0704A"] 
		newval = val - 1
		#race variable
		race = dataset.at[x,"VCF0106A"]
		#age
		age = dataset.at[x,"VCF0101"]
		#marital status
		marry = dataset.at[x,"VCF0147"]
		#family income
		faminc = dataset.at[x,"VCF0114"]
		#did they donate
		#donate = dataset.at[x,"VCF0721"]
		#home ownership
		home = dataset.at[x,"VCF0146"]
		#contacted by democratic party
		demcontact = dataset.at[x,"VCF9030B"]
		#contacted by republican party
		repcontact = dataset.at[x,"VCF9030C"]

		#adding data to our new frame
		newframe = newframe.append({'Vote': newval,
		'Year': year,
		'Race': race,
		'Age': age,
		'Marital Status': marry,
		'Family Income': faminc,
		#'Donated': donate,
		'Home Ownership': home,
		'Contacted by Republicans': repcontact,
		'Contacted by Democrats': demcontact,
		},ignore_index = True)
#saving our new csv
newframe.to_csv("CSV/electiondata4.csv", index= False)