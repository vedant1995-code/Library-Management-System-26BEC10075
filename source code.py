record = ["Siddesh","26BCE10178","Concepts of Physics (Vol. 1 and 2) by H.C. Verma"]
p1 = "asdfghjkl123456789" 
a = input("Admin or Student: ")
al = a.lower()
access_allowed = False
if al == "admin":
	attempts = 3
	while attempts > 0:
	       p = input("Enter the password: ")
	       if p == p1:
	           access_allowed = True
	           break
	       else:
	       	attempts -= 1
	       	if attempts > 0:
	       	   print(f"Incorrect password. You have {attempts} attempts left")
	       	else:
	       	   	print("Incorrect password. 3 failed attempts. System terminating...")
	if access_allowed:
				    e = input("Do you want to check the records (yes/no): ")
				    if e.lower() == "yes":
				    	print("\n--- Borrowing Records ---")
				    	print(record if record else "No records found.")
				    	exit()
				    elif e.lower() == "no":
				    	print("Exiting system. Goodbye!")
				    else:
				    		print("Invalid choice.")
elif al == "student":
	print("You can search for a book.")
	access_allowed = True 
else:
	print("Invalid role entered. Please choose 'Admin' or 'Student'.")
if access_allowed:
	literature="""'
1.Pride and Prejudice by Jane Austen
2. Animal Farm by George Orwell
3.Harry Potter and the Sorcerer's Stone by J.K. Rowling
4.To Kill a Mockingbird by Harper Lee
5.The Great Gatsby by F. Scott Fitzgerald
"""
	physics="""
1.The Feynman Lectures on Physics by Richard P. Feynman
2.Robert B. Leighton, and Matthew Sands
3.Fundamentals of Physics by David Halliday, Robert Resnick, and Jearl Walker
4.University Physics with Modern Physics by Roger A
5. Concepts of Physics (Vol. 1 and 2) by H.C. Verma
6.Engineering Physics by M.N. Avadhanulu and P.G. Kshirsagar"""
	cse="""
1.Introduction to Algorithms by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein (known as CLRS) [0.9]
2.Clean Code: A Handbook of Agile Software Craftsmanship by Robert C. Martin ("Uncle Bob") [0.3]
3.Design Patterns: Elements of Reusable Object-Oriented Software by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides (the Gang of Four or GoF) [0.10, 0.13]
4.The Pragmatic Programmer by Andrew Hunt and David Thomas [0.4, 0.15]
5.Code Complete: A Practical Handbook of Software Construction by Steve McConnell [0.4, 0.15]"""
	print("""
We currently have the following category of books:-
1. Literature
2. Physics
3. Cse""")
	print("YOU CAN GET ANY AVAILABLE BOOK WITH YOU FOR 14 DAYS")
	i=input('what category of book you want')
	il=i.lower()
	if il=="literature":
		print(literature)
		print("press the serial number of the book to see")
		s=int(input("Enter the serial number of the book you want"))
		if s==1:
			print("Pride and Prejudice by Jane Austen")
		elif s==2:
			print("Animal Farm by George Orwell")
		elif s==3:
			print("Harry Potter and the Sorcerer's Stone by J.K. Rowling")
		elif s==4:
			print("To Kill a Mockingbird by Harper Lee")
		elif s==5:
			print("The Great Gatsby by F. Scott Fitzgerald")
		else:
			print("Enter a valid serial number")
	elif il=="physics":
		print("physics")
		print("press the serial number of the book to see")
		s=int(input("Enter the serial number of the book you want"))
		if s==1:
			print("The Feynman Lectures on Physics by Richard P. Feynman")
		elif s==2:
			print("Robert B. Leighton, and Matthew Sands")
		elif s==3:
			print("Fundamentals of Physics by David Halliday, Robert Resnick, and Jearl Walker")
		elif s==4:
			print("University Physics with Modern Physics by Roger A")
		elif s==5:
			print("Concepts of Physics (Vol. 1 and 2) by H.C. Verma")
		elif s==6:
			print("Engineering Physics by M.N. Avadhanulu and P.G. Kshirsagar")
		else:
			print("Enter a valid serial number")
	elif il=="cse":
		print(cse)
		print("press the serial number of the book to see")
		s=int(input("Enter the serial number of the book you want"))
		if s==1:
			print("Introduction to Algorithms by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein (known as CLRS) [0.9]")
		elif s==2:
			print("""Clean Code: A Handbook of Agile Software Craftsmanship by Robert C. Martin ("Uncle Bob") [0.3]""")
		elif s==3:
			print("Design Patterns: Elements of Reusable Object-Oriented Software by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides (the Gang of Four or GoF) [0.10, 0.13]")
		elif s==4:
			print("The Pragmatic Programmer by Andrew Hunt and David Thomas [0.4, 0.15]")
		elif s==5:
			print("Code Complete: A Practical Handbook of Software Construction by Steve McConnell [0.4, 0.15]")
		else:
			print("Enter valid serial number")
	r=input("Do you want to get this book (yes/no)")
	rl=r.lower()
	if rl=="yes":
		n=input("Enter your name ")
		reg=input("Enter your registration number ")
		b=input("Enter the book name which you want ")
		record.append(n)
		record.append(reg)
		record.append(b)
	elif rl=="no":
		print("----- Thanks for visiting -----")	
	else:
		print("Enter a valid input")
