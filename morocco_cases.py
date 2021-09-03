import PyPDF2 
import re 
from datetime import date  
import requests 
import matplotlib.pyplot as plt 


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

#working from range ( specific pase date to today ) 
start_date = "01.7.21"


today_date = date.today()  

# Calculating todays date to make it adequat with the ministry website 

garbage = today_date.strftime("%dU%mU%y").split('U') 
garbage[1] = str(int(garbage[1])) 
date_end = '.'.join(garbage)


print("Start date : "+start_date) 
print("End date : "+date_end)

start_day , start_month ,year =  [int(x) for x in start_date.split('.') ]

end_dat , end_month , teeee = [int(x) for x in date_end.split('.') ]

dates = []
while start_day != end_dat or start_month !=end_month :
	if start_day != 31 :
		start_day+=1

	else :
		start_day = 1 
		start_month+=1
	dates.append("0"*(2-len(str(start_day)))+str(start_day)+"."+str(start_month)+"."+str(year))
	
		
#print(dates)
data = [] 
"""with open("02.9.21.COVID-19.pdf", "rb") as f : 
	pdfReader = PyPDF2.PdfFileReader(f)         
	PageObj = pdfReader.getPage(1)       
	data_unordered = PageObj.extractText()
	result = re.sub("\n+" ,"," ,data_unordered)                 
	result = result.replace(' ' , '').split(",")
	for x in result :
		if x <= '9' and x >= '0' :
			data.append(x)


	print(data)
	import sys 
	sys.exit()
"""
new_cases = [] 
for date in dates : 

	data = []	
	pdf_file = requests.get("http://www.covidmaroc.ma/Documents/BULLETIN/"+date+".COVID-19.pdf",headers=headers)
	
	if pdf_file.status_code == 200 :
		
		#with open("")
		with open("trash" , "wb") as f : 
			f.write(pdf_file.content)
	
		today_cases = open("trash" , "rb") 

		pdfReader = PyPDF2.PdfFileReader(today_cases) 

		PageObj = pdfReader.getPage(1) 

		data_unordered = PageObj.extractText()

		result = re.sub("\n+" ,"," ,data_unordered)
	
		result = result.replace(' ' , '').split(",")

		#print(result)
		for x in result :
			if x != '' :
				if x[0] <= '9' and x[0] >= '0' :
					data.append(x) 
		#print(data)

		new_cases.append(int(data[2]))

		print(date+" new_cases : "+str(new_cases[-1]))
	
	else :
		print("no response you fucking trash")	

dates = [x.replace('.','/')[:5] for x in dates ]
plt.plot(dates , new_cases) 

plt.xlabel("x - days")
plt.xlabel("y - new_cases")

plt.show()

