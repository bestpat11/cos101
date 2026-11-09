# Title: Student Weekly Expense Calculator

def calculate_weekly_expenses():
    print("=== Student Weekly Expense Calculator ===")
    
    # Input collection
    name = input("Student name: ")
    
    # Remove commas to handle formatted inputs like "1,000" safely
    daily_transport = float(input("Daily transport cost: ").replace(",", ""))
    daily_feeding = float(input("Daily feeding cost: ").replace(",", ""))
    days_on_campus = int(input("Days on campus: "))
    other_expenses = float(input("Other weekly expenses: ").replace(",", ""))
    
    # Processing calculations
    transport_total = daily_transport * days_on_campus
    feeding_total = daily_feeding * days_on_campus
    weekly_total = transport_total + feeding_total + other_expenses
    
    # Displaying summary output formatted to two decimal places
    print("\nWEEKLY EXPENSE SUMMARY")
    print(f"Student: {name}")
    print(f"Transport total: NGN {transport_total:,.2f}")
    print(f"Feeding total: NGN {feeding_total:,.2f}")
    print(f"Other expenses: NGN {other_expenses:,.2f}")
    print(f"Weekly total: NGN {weekly_total:,.2f}")

if __name__ == "__main__":
    calculate_weekly_expenses()
