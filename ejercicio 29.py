print("Enter the following 3 shortcuts:\n\n1-word wrap\n2-close the sidebar\n3-create a new file")
shortcut1 = str(input("\nEnter the first shortcut here: "))
shortcut2 = str(input("Enter the second shortcut here: "))
shortcut3 = str(input("Enter the third shortcut here: "))

if shortcut1.upper() == "ALT + Z"  and shortcut2.upper() == "CTRL + B" and shortcut3.upper() == "CTRL + N":
    print("Congratulations, your answers are correct")
else:
    print("Sorry, some of your answers are wrong...")