# Apartment-cost-data
In this task we will load data from a file containing data from apartment buildings for bill payment. More specifically, there is the data.csv file which contains data, building id, expense issue date, provider, amount, payment date (if any). In the event that there is no repayment date, then this expense is defined as a debt.

Some basic statistics should be calculated after the data is loaded.

A. First the data should be loaded:
A function should be created so that the program loads the data for a specific time period that will be given as input (optionally) by the user in the format dd/mm/yyyy. The start date and end date of the desired period will be given.

B. Then some statistics should be calculated:
A function should be made so that the program, for the selected dates, calculates the Minimum (min), Maximum (max), Mean, Standard Deviation (sd) and Difference (Variance var = (sd)2)

C. The debts per apartment building should then be calculated
A function should be created so that the program calculates the total of outstanding bills per apartment building.

D. Finally, the graph should be drawn for the requested data:
- Total debts per apartment building
- Dues per month/year
- Number of expenses per apartment building
- Total debts per apartment building per month
