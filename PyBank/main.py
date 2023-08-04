import os
import csv

with open(r'C:\Users\tsegi\OneDrive\Desktop\Python_challenge_resubmission-1\PyBank\Resources\budget_data.csv') as csv_file:
    csv_reader=csv.reader(csv_file)

    header = next(csv_reader)
    print(header)


    for row in csv_reader:
        print(row)
      
# number of lines - total number of months
with open(r'C:\Users\tsegi\OneDrive\Desktop\Python_challenge_resubmission-1\PyBank\Resources\budget_data.csv') as file:
    lines=file.readlines()[1:87]
    total_lines=len(lines)
    print('Total number of months:', total_lines)


# Net total profit/loss
with open(r'C:\Users\tsegi\OneDrive\Desktop\Python_challenge_resubmission-1\PyBank\Resources\budget_data.csv') as fin:
       header= next(fin)
       total=0
       for row in csv.reader(fin):
            total+=int(row[1])
       print('Total:', total)

#Change in profit/loss
with open (r'C:\Users\tsegi\OneDrive\Desktop\Python_challenge_resubmission-1\PyBank\Resources\budget_data.csv') as f:
     lines = f.readlines()
data=[]
for line in lines[1:]: # don't read the first line containing Date
     line=line.strip("/n") # erase the new line item from each line
     data.append(line.split(","))

output=[]
for index, number in enumerate (data[1:]): 
     output.append(int(number[1])-int(data[index][1]))
     average=sum(output)/len(output)
     maxValue=max(output)
     minValue=min(output)
     print(output)
     print('Average Change:', average)
     print('Greatest increase in ProfitLoss:', maxValue)
     print('Greatest decrease in ProfitLoss:', minValue)


outfile = os.path.join("C:\\Users\\tsegi\\OneDrive\\Desktop\\Python_challenge_resubmission-1\\PyBank\\Resources\\cbudget_analysis.txt")
with open(outfile,'w') as text_file:
    output=(
        f'Financial Analysis\n'
        f'-------------------------\n'
        f'Total Months: {total_lines}\n'
        f'Total:{total}\n'
        f'Average Change:{average}\n'
        f'Greatest Increase in Profits: Aug-16 {maxValue}\n'
        f'Greatest Decrease in Profits: Feb-14 {minValue}\n'
    )
    
    
    print(output)
    text_file.write(output)
