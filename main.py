'''
>>> JAAR
>>> 8/9/2023
>>> Practicing Fundamentals Program 15
>>> Version 1.1
'''

'''
>>> Takes a csv file containing the first name, last name, and debt of an individual and prints it to the console. The program will then calculate the average debt for the list of individuals and will then create a list of individuals that are above the average and bellow the average.
'''
import csv

def main() :
    members = []
    sort_debt = {"average_debt" : 0, "less" : [], "greater" : []}
    with open('debt.csv', 'r') as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            members.append(row)
            sort_debt["average_debt"] += float(row["debt_amount"])
    sort_debt["average_debt"] = sort_debt["average_debt"]/len(members)
    print(f'The average member debt is: {sort_debt["average_debt"]:,.2f}')
    for member in members :
        name = f'{member["last_name"]}, {member["first_name"]}'
        if float(member['debt_amount']) < sort_debt["average_debt"] :
            sort_debt["less"].append(name)
        else :
            sort_debt["greater"].append(name)
    print('\nMembers greater than average debt:\n\t' + '\n\t'.join(sorted(sort_debt["greater"])))
    print('\nMembers less than average debt:\n\t' + '\n\t'.join(sorted(sort_debt["less"])))

if __name__ == '__main__' :
    main()