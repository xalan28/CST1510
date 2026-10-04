"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

over_limit_count = 0   # how many records came back OVER LIMIT this session
while True:

    hostname = input("Hostname: ") 
    if hostname == "quit":
       break 
used_gb = float(input("Used GB: "))     
total_gb = float(input("Total GB: "))     


# ================================================================== PROCESS


difference = total_gb - used_gb 
percent = (used_gb / total_gb) * 100 if total_gb != 0 else 0  #crashes if total_gb is 0

if percent >= 100:
    status = "OVER LIMIT"
    over_limit_count += 1
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"
 
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {hostname}")
print("=" * 34)
print(f"  Used        : {used_gb:>10.2f}")
print(f"  Total       : {total_gb:>10.2f}")
print(f"  Free        : {difference:>10.2f}")
print(f"  Percent     : {percent:>10.2f} %")
print(f"  Status      : {status:>10}")


print("=" * 34)
print(f"Records over limit this session: {over_limit_count}")
#============================================================== OUTPUT
