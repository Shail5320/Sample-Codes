import string
import random

print("=============================================================")
print("\t\tWelcome to Basic Password Manager !!")
print("=============================================================")

website = input("Enter the Website's Name : ")
s1 = string.ascii_uppercase
s2 = string.ascii_lowercase 
s3 = string.digits
s4 = string.punctuation
choose = None
go_save = None
while choose != "sp" or "cg":
    choose = input("Do you want to enter a Specific Password[SP] or Computer Generated Password[CG] : ").lower()
    if choose == "cg":
        plen = int(input("Enter required Password's length : \n"))
        l = []
        l.extend(list(s1))   
        l.extend(list(s2))
        l.extend(list(s3))
        l.extend(list(s4))
        random.shuffle(l)
        passw = ("".join(l[0:plen]))
        break
    elif choose == "sp":
        passw = input(f"Kindly enter the Password for {website} : \n")
        break
    else:
        print("Kindly Enter a Valid Choice [CG/SP]\n")

with open ("Password File.txt", 'a') as f:
    f.write(f'''Website's Name : {website}
Website's Password : {passw}\n\n''')
print("Password successfully Saved !")

print("=============================================================")
print("\tThanks for Basic Password Manager !!")
print("=============================================================")
