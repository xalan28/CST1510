"""
RECORD CHECK  -  my version
===========================

Name  : Alan 
Lane  :  AI       
Date  : 25/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

label = input("Enter label: ")   
first = float(input("Enter first value: "))     
second = float(input("Enter second value: "))    


difference = second - first   
percent = (first / second) * 100      


print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"  First Value  : {first:>10.2f}")
print(f"  Second Value : {second:>10.2f}")
print(f"  Difference   : {difference:>+10.2f}")
print(f"  Percentage   : {percent:>10.2f}%")
print(f"  Status       : {'Within range' if first <= second else 'Over limit'}")

print("=" * 34)


