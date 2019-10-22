import myParser # include module, which read command-line
import sys

pars = myParser.createParser()
 #list of parameters
if __name__ == "__main__":
    parser = pars
    paramList = [param for param in sys.argv]

filename = paramList[1]
operation = paramList[2]

for i in paramList:
    print(i, end=' ')
print('\t')

f = open(filename, "r")
Datafile = [int(testline)for testline in f] # create a list, where an element is one string from the file
f.close()
Data =sorted(Datafile) #Sort the list in increasing order
#  CALCULATIONS
#-------------------------------------------------------------------------------------------------
result = 0
summa = 0
count = 0

# MEDIAN
if operation =='median':
    i = len(Data)//2                     # index of median element in list  
    if len(Data)%2 == 1:                 # check if the list includes odd number of elements
        median = Data[i]                 #  odd number of elements
        print('Median is:', int(median))
        result = int(median)      
    else:
        median = (int(Data[i]) + int(Data[i-1]))/2          # even number of elements
        print('Median is:', median)                         # niin kuin tehtävässä ei ollut ehtoa datatyypistä,
        result_median = [int(Data[i-1]), int(Data[i])]      # mediaanin on float, muut integer, mukaan lukien N.

# SUMMA | AVERAGE
else:
    for i in Data:
        count += 1                 # calculate number of elements
        summa = summa + i          # calculate sum of all elements
        avg = int(summa / count)        # calculate average of elements
    if operation == 'sum':
        print("Sum is: ", summa)
        result = summa
    elif operation == 'avg':
        print("Average is: ", avg)
        result = avg

# COMPARISON'S CASES
# ----------------------------------------------------------------------------------------------
# #for comparison number is defined from command-line,  check if statement is true 
if len(paramList) > 3:
    try:
        comparison = paramList[3]
        n = int(paramList[4])
        if comparison == 'gt': 
            if len(Data)%2 == 0 and operation =='median':
                for medi in result_median:
                    if medi > n: print(medi, "is greater than", n)
                    else: print(medi, "is not greater than", n)
            elif result > n: print(result, "is greater than", n)
            else: print(result, "is not greater than", n)

#------------------------------------------------------------------------------
        elif comparison =='lt':
            if len(Data)%2 == 0 and operation =='median':
                for medi in result_median:
                    if medi < n: print(medi, "is less than", n)
                    else: print(medi, "is not less than", n)
            elif result < n: print(result, "is less than", n)
            else: print(result, "is not less than", n)

#------------------------------------------------------------------------------
        elif comparison == 'eq':
            if len(Data)%2 == 0 and operation =='median':
                for medi in result_median:
                    if medi == n: print(medi, "is equal to", n)
                    else: print(medi, "is not equal to", n)
            elif result == n: print(result, "is equal to ", n)
            else: print(result, "is not equal to ", n) 
    except:
        print("Comparison number is not defined") 





