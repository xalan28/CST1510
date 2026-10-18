"""
RECORD CHECK  -  my version
===========================

Name  : ALan
Lane  :  AI     (delete two)
Date  : 18/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def check_record(value, limit):
    """Work out the difference, percent and status."""
    difference = value - limit
    percent = value / limit * 100
    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"
    return difference, percent, status


def print_report(label, difference, percent, status):
    """Print one line of results."""
    print(label, difference, percent, status)


records = [
    {"label": "Server A", "value": 72, "limit": 80},
    {"label": "Server B", "value": 95, "limit": 90},
    {"label": "Server C", "value": 40, "limit": 75},
]

for r in records:
    difference, percent, status = check_record(r["value"], r["limit"])
    print_report(r["label"], difference, percent, status)
