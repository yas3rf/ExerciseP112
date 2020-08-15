gender = input("please enter 'F' for female and 'M' for male: ")
salary = int(input("Enter your salary amount: "))
bonus = ''
if gender == ('f' or 'F'):
    bonus = salary*0.10
elif gender == ('m' or 'M'):
    bonus = salary*0.05
    total_salary = bonus + salary
    print("salary = " + str(salary))
    print("bonus = " + str(bonus))
    print("-" * 100)
    print("salary_after_bonus = " + str(total_salary))
else:
    print("wrong input please try again")