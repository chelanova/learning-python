import csv
from datetime import datetime

class ExpenseTracker:
    def __init__(self, filename = "expense.csv"):
        self.filename = filename
        self.ensure_file_exists()
        
    def ensure_file_exists(self):
        try:
            with open(self.filename, 'x', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Date', 'Category', 'Description', 'Amount'])  # ✅ Hapus spasi
        except FileExistsError:
            pass
        
    def add_expense(self, category, description, amount):
        try:
            with open(self.filename, 'a', newline='') as f:
                writer = csv.writer(f)
                date = datetime.now().strftime("%Y-%m-%d")
                writer.writerow([date, category, description, amount])
            return f"Expense added: Rp{amount:,.0f}"
        except Exception as e:
            return f"Error: {e}"
        
    def view_expenses(self):
        try:
            with open(self.filename, 'r') as f:
                reader = csv.DictReader(f)
                expenses = list(reader)
                
                if not expenses:
                    print("No expenses recorded yet.")
                    return
                
                print("\n" + "="*70)
                print(f"{'Date':<12} {'Category':<15} {'Description':<20} {'Amount':>10}")
                print("="*70)
                
                total = 0
                for expense in expenses:
                    amount = float(expense['Amount'])
                    total += amount
                    print(f"{expense['Date']:<12} {expense['Category']:<15} "
                          f"{expense['Description']:<20} Rp{amount:>10,.0f}")
                print("="*70)
                print(f"{'TOTAL':<47} Rp{total:>10,.0f}")
                print("="*70 + "\n")
                
        except FileNotFoundError:
            print("No expenses file found.")
        except Exception as e:
            print(f"Error reading expenses: {e}")
    
    def get_summary_by_category(self):
        try:
            with open(self.filename, 'r') as f:
                reader = csv.DictReader(f)
                expenses = list(reader)
                
                if not expenses:
                    print("No expenses to summarize!")
                    return
                
                categories = {}
                for expense in expenses:
                    category = expense['Category']
                    amount = float(expense['Amount'])
                    categories[category] = categories.get(category, 0) + amount
                    
                print("\n" + "="*50)
                print("EXPENSE SUMMARY BY CATEGORY")
                print("="*50)
                
                total = 0
                for category, amount in sorted(categories.items(), key=lambda x: x[1], reverse=True):
                    print(f"{category:<30} Rp{amount:>15,.0f}")
                    total += amount
                    
                print("="*50)
                print(f"{'TOTAL':<30} Rp{total:>15,.0f}")
                print("="*50 + "\n")
                
        except Exception as e:
            print(f"Error: {e}")
                
                
def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\n=== EXPENSE TRACKER ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary by Category")
        print("4. Exit")
        
        choice = input("\nChoose option (1-4): ").strip()
        
        if choice == '1':
            category = input("Category (Food/Transport/Shopping/Bills/Other): ").strip()
            description = input("Description: ").strip()
            
            try:
                amount = float(input("Amount (Rp): ").strip())
                print(tracker.add_expense(category, description, amount))
                
            except ValueError:
                print("Invalid amount!")
                
        elif choice == '2':
            tracker.view_expenses()
            
        elif choice == '3':
            tracker.get_summary_by_category()
            
        elif choice == "4":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice!")
            
if __name__ == "__main__":
    main()