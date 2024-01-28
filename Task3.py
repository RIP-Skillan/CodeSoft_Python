import random 
import string 
characters=string.ascii_letters + string.digits  
l=int(input("\nEnter the Lenght of password: "))
password=''.join(random.choice(characters) for i in range(l)) 
print("Generated Password:",password,"\n")