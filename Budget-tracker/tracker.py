Terry Cajuste
# tracker.py
import data  # connects to data.py

# ---------------------------
# Function 1: View All Expenses
# ---------------------------
def view_all_expenses():
    """Display all recorded expenses in a formatted list."""
    if len(data.categories) == 0:
        print("No expenses recorded yet.")
        return

    print("\nAll Expenses:")
    print("-" * 40)

    for i in range(len(data.categories)):
        print(f"{i+1}. {data.categories[i]} - ${data.amounts[i]:.2f} - {data.descriptions[i]}")

    print("-" * 40)


# ---------------------------
# Function 2: Summary Report
# ---------------------------
def summary_report():
    """Show total spent, count, average, and most frequent category."""
    if len(data.amounts) == 0:
        print("No expenses to summarize.")
        return

    total = sum(data.amounts)
    count = len(data.amounts)
    average = total / count

    # Find the most frequent category
    most_frequent = max(set(data.categories), key=data.categories.count)

    print("\nSummary Report:")
    print("-" * 40)
    print(f"Total Spent: ${total:.2f}")
    print(f"Number of Expenses: {count}")
    print(f"Average Expense: ${average:.2f}")
    print(f"Most Frequent Category: {most_frequent}")
    print("-" * 40)
