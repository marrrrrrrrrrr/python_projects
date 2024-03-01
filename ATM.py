'''
პროგრამა მომხმარებელს საშუალებას აძლევს განახორციელოს ძირითადი საბანკო ოპერაციები,
როგორიცაა ბალანსის შემოწმება, თანხის შეტანა, თანხის გატანა და ტრანზაქციის ისტორიის ნახვა.

მომხმარებლის ანგარიშის მონაცემები ინახება CSV ფაილში, სადაც თითოეულ მწკრივს გააჩნია ანგარიშის ნომრის, სახელისა და ბალანსის ველები.

პროგრამა მომხმარებელს სთხოვს შეიყვანოს ანგარიშის ნომერი საკუთარ ანგარიშზე წვდომისთვის.
შემდეგ მას შეუძლია აირჩიოს ძირითადი მენიუდან რომელი საბანკო ოპერაციის შესრულება სურს.
ყოველი ტრანზაქცია ინახება შესაბამის ფაილში, ცალ-ცალკე თითეული ანგარიშისთვის მისი განხორციელების დროის, ტიპის და თანხის მითითებით.

ვალიდაციები:
- ნებისმიერი ოპერაციის შესრულებამდე პროგრამა ამოწმებს, არის თუ არა მითითებული ანგარიშის ნომერი მომხმარებლის მონაცემების ლექსიკონში
- როდესაც მომხმარებელს სთხოვენ შეიყვანოს თავისი არჩევანი მთავარ მენიუში, პროგრამა ამოწმებს, რომ მისი არჩევანი მოქმედი დიაპაზონის ფარგლებშია (1-5)
- როდესაც ხდება თანხის გატანა, პროგრამა ამოწმებს, აქვს თუ არა მომხმარებელს საკმარისი თანხა ანგარიშზე

'''


import csv
from datetime import datetime

# ფუნქცია, რომლის საშუალებითაც მონაცემები წაიკითხება CSV ფაილიდან და შეინახება ლექსიკონში
def read_user_data(file_name):
    users = {}
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # გამოვტოვოთ header
        for row in reader:
            account_number, name, balance = row
            users[account_number] = {'name': name, 'balance': float(balance), 'transaction_history': []}
    return users

# ფუნქცია, რომელიც წერს მონაცემებს ლექსიკონიდან CSV ფაილში
def write_user_data(user_data, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['account_number', 'name', 'balance'])
        for account_number, user_info in user_data.items():
            writer.writerow([account_number, user_info['name'], user_info['balance']])

# ფუნქცია, რომელიც ამოწმებს ბალანსს კონკრეტული ანგარიშისთვის
def check_balance(user_data, account_number):
    if account_number in user_data:
        return user_data[account_number]['balance']
    else:
        return None  # ანგარიშის ნომერი არ არსებობს

# ფუნქცია კონკრეტულ ანგარიშზე თანხის შესატანად
def deposit(user_data, account_number, amount):
    if account_number in user_data:
        user_data[account_number]['balance'] += amount
        user_data[account_number]['transaction_history'].append((datetime.now(), 'Deposit', amount))
        write_user_data(user_data, 'users.csv')
        save_transaction_history(user_data, account_number) # ტრანზაქციას ინახავს შესაბამის ტრანზაქციის ისტორიის ფაილში
        return True  # თანხის შეტანა წარმატებით განხორციელდა
    else:
        return False  # ანგარიშის ნომერი არ არსებობს

# ფუნქცია კონკრეტული ანგარიშიდან თანხის გასატანად
def withdraw(user_data, account_number, amount):
    if account_number in user_data:
        if user_data[account_number]['balance'] >= amount:
            user_data[account_number]['balance'] -= amount
            user_data[account_number]['transaction_history'].append((datetime.now(), 'Withdrawal', amount))
            write_user_data(user_data, 'users.csv')  # ანახლებს მონაცემებს ფაილში
            save_transaction_history(user_data, account_number) # ტრანზაქციას ინახავს შესაბამის ტრანზაქციის ისტორიის ფაილში
            return True  # თანხის გატანა წარმატებით განხორციელდა
        else:
            print("Not enough money on account.")
            return False  # ანგარიშზე არასაკმარისი თანხაა
    else:
        return False  # ანგარიშის ნომერი არ არსებობს

# ფუნქცია, რომელიც გვიჩვენებს ტრანზაქციის ისტორიას
def show_transaction_history(user_data, account_number):
    if account_number in user_data:
        print("Transaction History:")
        for transaction in user_data[account_number]['transaction_history']:
            date_time, transaction_type, amount = transaction
            print(f"{date_time.strftime('%Y-%m-%d %H:%M:%S')} - {transaction_type}: ₾{amount:.2f}")
    else:
        print("Account not found.")

# ფუნქცია, რომელიც ინახავს განხორციელებულ ტრანზაქციებს შესაბამის ფაილში account_number-ის მიხედვით
def save_transaction_history(user_data, account_number):
    filename = f"transaction_history_{account_number}.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        for transaction in user_data[account_number]['transaction_history']:
            date_time, transaction_type, amount = transaction
            file.write(f"{date_time.strftime('%Y-%m-%d %H:%M:%S')} - {transaction_type}: ₾{amount:.2f}\n")

# ბანკომატის მთავარი მენიუს გამოტანა
def main_menu():
    print("\nWelcome to the ATM!")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Show Transaction History")
    print("5. Exit")

# ფუნქცია, რომელიც ამოწმებს არსებობს თუ არა მომხმარებელი მითითებული ანგარიშის ნომრით
def account_exists(user_data, account_number):
    return account_number in user_data


def main():
    # კითხულობს მომხმარებლის მონაცემებს CSV ფაილიდან
    user_data = read_user_data('users.csv')
    
    # სთხოვს მომხმარებელს შეიყვანოს ანგარიშის ნომერი
    while True:
        account_number = input("Enter your account number: ")
        if not account_exists(user_data, account_number):
            print("Account not found.")
        else:
            break
    
    while True:
        main_menu()
        choice = input("Please enter your choice (1-5): ")  # მომხმარებელს სთხოვს აირჩიოს რომელი ოპერაციის შესრულება სურს
        if choice == '1':
            # ბალანსის შემოწმება
            balance = check_balance(user_data, account_number)
            if balance is not None:
                print(f"\nYour balance: ₾{balance:.2f}")
            else:
                print("Account not found.")
        elif choice == '2':
            # თანხის შეტანა
            amount = float(input("Enter the amount to deposit: "))
            if deposit(user_data, account_number, amount):
                print("Deposit successful.")
            else:
                print("Failed to deposit.")
        elif choice == '3':
            # თანხის გატანა
            amount = float(input("Enter the amount to withdraw: "))
            if withdraw(user_data, account_number, amount):
                print("Withdrawal successful.")
            else:
                print("Failed to withdraw.")
        elif choice == '4':
            # ტრანზაქციის ისტორიის ჩვენება
            show_transaction_history(user_data, account_number)
        elif choice == '5':
            # პროგრამიდან გამოსვლა
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
            
main()