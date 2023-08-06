import random
l=[1,2,3,4,5,6,7,8,9]
def start():
	try :
	       print("you want to play first?\n1.yes    2.no")
	       n=int(input("Enter your choice as 1 or 2  : "))
	       if(n==1 or n==2):
	       		if(n==1):
	       			choosing()
	       		if(n==2):		
	       			display(5,2)
	       else:
	       	print("Enter a valid option in 1 or 2 only")
	       	start()  
	except SystemExit:
		exit()
	except :
		print("You not entered in number format\nplease enter in the number format")
		start()
def comp():
	a=random.randint(1,9)
	display(a,2)
def choosing():
		try:
		   a=int(input("\nwhich box you want to choose : "))
		   if a>0 and a<10:
		   	display(a,1)
		   else :
		   	print("\nPlease enter the box number in valid given rangeof 1 to 9 only")
		   	choosing()
		except SystemExit:
		 	exit()	 	
		except :
		   print("\nYou are entering some characters\nDo enter only in number format")
		   choosing()   		   		   		   
def display(i,j):
   if(l[i-1]=='$' or l[i-1]=='@'):
   	if(j==1):
   		print("\nThat box is taken already \nplease enter another option")
   		choosing()
   	if(j==2):
   	    comp()
   if(j==1):
   	l[i-1]="$"
   if(j==2):
   	print("\nComputer choosen box  is ",i)
   	l[i-1]="@"
   print("*************************")
   print("|       |       |       |")
   print("|  ",l[0],"  |  ",l[1],"  |  ",l[2],"  |") 
   print("|       |       |       |")
   print("*************************")
   print("|       |       |       |") 
   print("|  ",l[3],"  |  ",l[4],"  |  ",l[5],"  |") 
   print("|       |       |       |")
   print("*************************")
   print("|       |       |       |")
   print("|  ",l[6],"  |  ",l[7],"  |  ",l[8],"  |") 
   print("|       |       |       |")
   print("*************************")
   check(j)
def check(j):
     if((l[0]==l[1]==l[2]=='$' ) or (l[0]==l[4]==l[8]=='$') or (l[0]==l[3]==l[6]=='$') or (l[1]==l[4]==l[7]=='$') or (l[2]==l[5]==l[8]=='$')or (l[2]==l[4]==l[6]=='$')or (l[3]==l[4]==l[5]=='$') or (l[6]==l[7]==l[8]=='$' )):
          print("\n\n\nYou won the match\n\n ")
          quit()
     if((l[0]==l[1]==l[2]=='@' ) or (l[0]==l[4]==l[8]=='@') or (l[0]==l[3]==l[6]=='@') or (l[1]==l[4]==l[7]=='@') or (l[2]==l[5]==l[8]=='@')or (l[2]==l[4]==l[6]=='@')or (l[3]==l[4]==l[5]=='@') or (l[6]==l[7]==l[8]=='@' )):
          print("\n\n\nComputer won the game \n\n")
          quit()
     if(all([isinstance(val, str) for val in l])):
          print("\n\n\nMatch is draw\n\n")
          quit()
     if(j==1):
       	comp()
     if(j==2):
       	choosing()	
print("lets start the game ")
print("\nComputer symbol is \"@\"")
print("\nYour symbol is \"$\"\n\n")
start()
