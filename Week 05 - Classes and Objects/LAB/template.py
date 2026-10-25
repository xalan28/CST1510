"""
RECORD CHECK  -  my version
===========================

Name  : Alan
Lane  :  AI      (delete two)
Date  : 24/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

# your class goes here


"""
RECORD CHECK
Name:
Lane: AI / Cyber / IT
Date:
"""


# 1. CLASS

class Record:
    # Class-level running total
    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Store the record's label, value and limit."""
        self.label = label
        self.value = value
        self.limit = limit

        if self.value >= self.limit:
            Record.over_limit_count += 1

    def status(self):
        """Return the status based on the value and limit."""
        if self.value >= self.limit:
            return "OVER LIMIT"
        elif self.value >= 0.9 * self.limit:
            return "WARNING"
        else:
            return "OK"


# 2. CREATE THE DATA FILE

with open("records.txt", "w") as file:
    file.write("Temperature,105,100\n")
    file.write("Battery,95,100\n")
    file.write("Pressure,80,100\n")
    file.write("Engine,120,100\n")
    file.write("Fuel,90,100\n")


# 3. LOAD RECORDS FROM THE FILE

def load_records(path):
    """Read records from a file and return a list of objects."""
    records = []

    with open(path, "r") as file:
        for line in file:
            label, value, limit = line.strip().split(",")

            record = Record(label, float(value), float(limit))
            records.append(record)

    return records


records = load_records("records.txt")


# 4. PRINT THE REPORT

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {record.label}")
    print("=" * 34)

    print(f"  Value:  {record.value}")
    print(f"  Limit:  {record.limit}")
    print(f"  Status: {record.status()}")

    print("=" * 34)


# 5. PRINT THE TOTAL

print()
print(f"Total over-limit records: {Record.over_limit_count}")




