"""
RECORD CHECK - my version
=========================

Name  : Alan
Lane  : AI
Date  : 10/10/26

Run it: python record_check_excellent.py
"""

# =================================================================== FUNCTIONS
# 1. Functions used by the Record Check report.

def status_of(percent):
    """Return the status for a given percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the difference and percentage for a record."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print a formatted report for one record."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Value       : {value:10.2f}")
    print(f"  Limit       : {limit:10.2f}")
    print(f"  Difference  : {difference:10.2f}")
    print(f"  Percent     : {percent:10.2f}%")
    print(f"  Status      : {status}")
    print("=" * 34)


# ==================================================================== INPUT
# 2. Ask for values repeatedly. Type "quit" as the label to stop.

over_limit_count = 0

while True:
    label = input("Enter name/hostname (or 'quit' to stop): ")

    if label.lower() == "quit":
        break

    value = float(input("Enter value used: "))
    limit = float(input("Enter total limit: "))

    # ================================================================ PROCESS
    # 3. Calculate the difference, percentage, and status.

    difference, percent = check(value, limit)
    status = status_of(percent)

    # ================================================================= OUTPUT
    # 4. Print the report using the report function.

    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
        over_limit_count = over_limit_count + 1


# Print the total once, after the loop ends.
print()
print(f"Records OVER LIMIT: {over_limit_count}")
