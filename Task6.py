''' Write a Python program that accepts a paragraph from the user and uses Regular Expressions (re) to extract:
* Email addresses
* 10-digit phone numbers
* URLs
* Numbers
'''

import re
pattern1=r"[a-zA-Z0-9]+@[a-zA-Z]+\.(?:com|edu|net|org)"
pattern2=r"[6-9]\d{9}"
pattern3=r"https?://(?:www\.)?[a-zA-Z0-9]+\.(?:com|edu|net|org)"
pattern4=r"\d+"

user=input("Enter a para: ")

email=re.findall(pattern1,user)
phone=re.findall(pattern2,user)
url=re.findall(pattern3,user)
numbers=re.findall(pattern4,user)

for i in phone:
    numbers.remove(i)

if email!=[]:
    print("\nEmail addressses:")
    print(* email,sep="\n")
if phone!=[]:
    print("\n10-digit phone numbers:")    
    print(* phone,sep="\n")
if url!=[]:
    print("\nURLs:")
    print(* url,sep="\n")
if numbers!=[]:
    print("\nNumbers:")
    print(* numbers,sep="\n")