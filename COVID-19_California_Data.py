import csv
import numpy as np

deathIncrease, hospitalizedCurrently, inIcuCurrently, negativeIncrease, positiveIncrease, totalTestResultsIncrease = np.genfromtxt("california-history.csv",
                                                                                                                                                            dtype=int,
                                                                                                                                                            delimiter=',',
                                                                                                                                                            skip_header=1,
                                                                                                                                                            usecols=(3,4,5,7,10,12),
                                                                                                                                                            unpack=True)
print("Data history of COVID cases in California from '3-4-2020' to '12-6-2020'")
print("========================================================================")
print ("{:<17} {:<15} {:<15} {:<15} {:<15} {:<15} {:<20}".format('Value','GrowthDeath','InHospital','InICU', '(-)Increase', '(+)Increase', 'TestResultsGrowth'))
print("-------------------------------------------------------------------------------------------------------------------")
#Printing the Mean
print("Mean:", '\t\t ', '%.2f'%np.mean(deathIncrease),
               '\t ',   '%.2f'%np.mean(hospitalizedCurrently),
               '\t ',   '%.2f'%np.mean(inIcuCurrently),
               '\t ',   '%.2f'%np.mean(negativeIncrease),
               '\t ',   '%.2f'%np.mean(positiveIncrease),
               '\t ',   '%.2f'%np.mean(totalTestResultsIncrease))


#Printing the Median
print("Median:", '\t ', '%.2f'%np.median(deathIncrease),
               '\t ',   '%.2f'%np.median(hospitalizedCurrently),
               '\t ',   '%.2f'%np.median(inIcuCurrently),
               '\t ',   '%.2f'%np.median(negativeIncrease),
               '\t ',   '%.2f'%np.median(positiveIncrease),
               '\t ',   '%.2f'%np.median(totalTestResultsIncrease))

#Printing the Standard Deviation
print("Median:", '\t ', '%.2f'%np.std(deathIncrease),
               '\t ',   '%.2f'%np.std(hospitalizedCurrently),
               '\t ',   '%.2f'%np.std(inIcuCurrently),
               '\t ',   '%.2f'%np.std(negativeIncrease),
               '\t ',   '%.2f'%np.std(positiveIncrease),
               '\t ',   '%.2f'%np.std(totalTestResultsIncrease))

#Printing the Lowest Value
print("Lowest Value:", '\t ', '%.2f'%np.amin(deathIncrease),
               '\t\t ',   '%.2f'%np.amin(hospitalizedCurrently),
               '\t ',   '%.2f'%np.amin(inIcuCurrently),
               '\t ',   '%.2f'%np.amin(negativeIncrease),
               '\t\t ',   '%.2f'%np.amin(positiveIncrease),
               '\t\t ',   '%.2f'%np.amin(totalTestResultsIncrease))

#Printing the Highest Value
print("Highest Value:", '\t ', '%.2f'%np.amax(deathIncrease),
               '\t ',   '%.2f'%np.amax(hospitalizedCurrently),
               '\t ',   '%.2f'%np.amax(inIcuCurrently),
               '\t ',   '%.2f'%np.amax(negativeIncrease),
               '\t ',   '%.2f'%np.amax(positiveIncrease),
               '\t ',   '%.2f'%np.amax(totalTestResultsIncrease))

#Printing the 75th percentile
print("75th percentile:", '', '%.2f'%np.percentile(deathIncrease,75),
               '\t ',   '%.2f'%np.percentile(hospitalizedCurrently,75),
               '\t ',   '%.2f'%np.percentile(inIcuCurrently,75),
               '\t ',   '%.2f'%np.percentile(negativeIncrease,75),
               '\t ',   '%.2f'%np.percentile(positiveIncrease,75),
               '\t ',   '%.2f'%np.percentile(totalTestResultsIncrease,75))

#Printing out sources
print()
print("Data comes from: The COVID Data Project")
print("Website: https://covidtracking.com/")
print("CSV file was modified to cut out redundant data.")
