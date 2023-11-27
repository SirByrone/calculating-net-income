import getpass
from decimal import Decimal, ROUND_HALF_UP

def authenticate_user():
     with open('user_data.txt', 'r') as f:
        lines = f.readlines()

username = input("Enter username: ")
password = getpass.getpass("Enter password: ")
valid_credentials = False
 


def process_employees(num_employees):
    employee_records = []

    for i in range(num_employees):
        name = input("Enter the name of employee {}: ".format(i+1))
        gross_income = float(input("Enter the gross income of employee {}: ".format(i+1)))

        # Calculate PAYE (30% of gross income) and round to 1 decimal place
        paye = Decimal(str(gross_income * 0.3)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

        # Calculate net income and round to 1 decimal place
        net_income = Decimal(str(gross_income - gross_income * 0.3)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

        employee_records.append({
            "Serial Number": i+1,
            "Name": name,
            "Gross Income": round(gross_income, 1),
            "PAYE": float(paye),
            "Net Income": float(net_income)
        })

    # Write results to a text file in tabular format
    with open('employee_data.txt', 'w') as f:
        f.write("{:<15} {:<25} {:<15} {:<15} {:<15}\n".format("Serial Number", "Name", "Gross Income", "PAYE", "Net Income"))
        for record in employee_records:
            f.write("{:<15} {:<25} {:<15} {:<15} {:<15}\n".format(
                record["Serial Number"], record["Name"], record["Gross Income"], record["PAYE"], record["Net Income"]))

    print("Employee data has been written to employee_data.txt.")

def main():
    authenticated = False
    while not authenticated:
        authenticated = authenticate_user()
        if not authenticated:
            retry = input("Authentication failed. Do you want to retry? (yes/no): ").lower()
            if retry != 'yes':
                print("Exiting program.")
                return

    num_employees = int(input("Enter the number of employees to process: "))
    process_employees(num_employees)

if __name__ == "__main__":
    main()