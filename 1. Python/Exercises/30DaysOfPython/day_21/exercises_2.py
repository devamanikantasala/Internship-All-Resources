# Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and 
# it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. 
# Incomes is a set of incomes and its description. The same goes for expenses.
class PersonAccount:
    import json as js;
    track_income = {}
    track_expense = {}
    def __init__(self, firstname='Deva', lastname='Manikanta', income=15000, expenses=17000):
        self.firstname = firstname
        self.lastname = lastname
        self.income = income
        self.expenses = expenses;
        PersonAccount.track_income[self.income] = 'Initial Income';
        PersonAccount.track_expense[self.expenses] = 'Initial Expense';
    def add_income(self, income=0, description='None'):
        self.income += income;
        PersonAccount.track_income[income] = description;
    def add_expense(self, expense=0, description='None'):
        self.expenses += expense;
        PersonAccount.track_expense[expense] = description;
    def total_income(self):
        return f'\nTotal Income : {self.income}$'
    def total_expenses(self):
        return f'\nTotal Expense : {self.expenses}$'
    def account_balance(self):
        return f'\nAccount Balance : {self.income - self.expenses}$'
    def account_info(self):
        return f'\nAccount Holder : {str(self.firstname)+' '+str(self.lastname)}\nInitial Income: {self.track_income['Initial Income']}$\nInitial Expense: {self.track_expense['Initial Expense']}$\nCurrent Income: {self.income}$\nCurrect Expenses: {self.expenses}$'
    def get_income_records(self):
        output = PersonAccount.js.dumps(PersonAccount.track_income, indent=4);
        return output;
    def get_expense_records(self):
        output = PersonAccount.js.dumps(PersonAccount.track_expense, indent=4);
        return output;
val = -1
while val != 0:
    print('1. Start an Account\n0. Exit');
    val = int(input('Your choice: '))
    if val == 1:
        first = input('First Name: ')
        last = input('Last Name: ')
        incom = int(input('Income: '))
        expen = int(input('Expenses: '))
        account = PersonAccount(firstname=first, lastname=last, income=incom, expenses=expen);
        print('Options\na) Add Income\nb) Add Expense\nc) Check Balance\nd) Total Expense\ne) Total Income\nf) Account info\ng) Close Account\nh) Get Income Records\ni) Get Expense Records\nEXIT Options:[-1, \'exit\', \'ex\', \'EXIT\', \'EX\']');
        choice = ''
        while choice not in ['-1', 'exit', 'ex', 'EXIT', 'EX']:
            choice = input('Your Choice: ');
            if str(choice.lower()).startswith('a'):
                new_income = int(input('Enter your new income: '));
                proof_description = input('How did you earned this?\n');
                account.add_income(income=new_income, description=proof_description);
                print('Added Successfully');
            elif str(choice.lower()).startswith('b'):
                new_expense = int(input('Enter your new expense: '));
                proof_description = input(f'What purpose did you spend this {new_expense} much money for?\n');
                account.add_expense(expense=new_expense, description=proof_description);
                print('Added Successfully');
            elif str(choice.lower()).startswith('c'):
                balance = account.account_balance();
                print(balance);
            elif str(choice.lower()).startswith('d'):
                expenses = account.total_expenses();
                print(expenses);
            elif str(choice.lower()).startswith('e'):
                income = account.total_income();
                print(income);
            elif str(choice.lower()).startswith('f'):
                print(account.account_info());
            elif str(choice.lower()).startswith('g'):
                confirm = input('Confirm to close your account : [y|n]: ');
                if confirm in ['y', 'yes', 'YES', 'Y', 1]:
                    del account;
                    print('Account was successfully deleted!')
                    break;
            elif str(choice.lower()).startswith('h'):
                output = account.get_income_records();
                print(output);
            
            elif str(choice.lower()).startswith('i'):
                output = account.get_expense_records();
                print(output);
            
            else:
                print('Invalid Option Choosen');
            print('Options\na) Add Income\nb) Add Expense\nc) Check Balance\nd) Total Expense\ne) Total Income\nf) Account info\ng) Close Account\nh) Get Income Records\ni) Get Expense Records\nEXIT Options:[-1, \'exit\', \'ex\', \'EXIT\', \'EX\']');
    elif val == 0:
        exit()
    else:
        print('Invalid Option Chosen');