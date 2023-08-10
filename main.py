'''
>>> JAAR
>>> 8/9/2023
>>> Practicing Fundamentals Program 15
>>> Version 1
'''

'''
>>> Takes a csv file containing the first name, last name, and debt of an individual and prints it to the console. The program will then calculate the average debt for the list of individuals and will then create a list of individuals that are above the average and bellow the average.
'''
import csv

def print_members()->float :
    '''
    >>> Prints a list of each member as well as their current debt then calculates and returns the average debt for all members.

    >>> Return: (float) AVERAGE_DEBT
    '''
    AVERAGE_DEBT = 0
    with open('debt.csv', 'r') as csv_file :
        csv_reader = csv.DictReader(csv_file)
        print('Each members debt is listed below:')
        members = 0
        for row in csv_reader :
            print(f'\t{row["first_name"]}, {row["last_name"]} : ${float(row["debt_amount"]):,.2f}')
            members += 1
            AVERAGE_DEBT += float(row["debt_amount"])
        AVERAGE_DEBT = AVERAGE_DEBT / members
        print(f'Average Debt: {AVERAGE_DEBT:,.2f}')
        return AVERAGE_DEBT

def sort_debt(AVERAGE_DEBT : float)->dict :
    '''
    >>> Checks if an individuals debt is above or below the average and sorts them based on this.

    >>> Param : (float) AVERAGE_DEBT
    >>> Return : (dict) debt_comparator
    '''
    debt_comparator = {"less" : [],"greater" : [] }
    with open('debt.csv', 'r') as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            name = f'{row["first_name"]}, {row["last_name"]}'
            if float(row["debt_amount"]) < AVERAGE_DEBT :
                debt_comparator["less"].append(name)
            else :
                debt_comparator["greater"].append(name)
    return debt_comparator

def print_debt(debt_comparator : dict) :
    '''
    >>> Prints two sorted lists. One containing the members who's debt is over the average and one containing the members who's debt is below the average.
    '''
    print('\n\nMembers with debt greater than average debt:')
    for name in sorted(debt_comparator["greater"]) :
        print('\t' + name)
    print('\n\nMembers with less than average debt:')
    for name in sorted(debt_comparator["less"]) :
        print('\t' + name)

def main() :
    AVERAGE_DEBT = print_members()
    debt_comparator = sort_debt(AVERAGE_DEBT)
    print_debt(debt_comparator)

if __name__ == '__main__' :
    main()