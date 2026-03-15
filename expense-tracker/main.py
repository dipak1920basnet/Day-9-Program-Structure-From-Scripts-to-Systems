from report import print_summary
from expense_manager import add_expense, total_expense, average_expense
def main():
    expense = {}
    expense = add_expense(expense,"Food",300)
    total = total_expense(expense)
    average = average_expense(total, len(expense))
    print_summary(total, average)

if __name__ == "__main__":
    main()
