import random




def dice(ans):
	if ans == "y":
		
		x = random.randint(1,6)
		if x == 1:
			print("************")
			print("*          *")
			print("*    O     *")
			print("*          *")
			print("************")

		elif x == 2:
			print("************")
			print("*    O     *")
			print("*          *")
			print("*    O     *")
			print("************")

		elif x == 3:
			print("************")
			print("*   O      *")
			print("*     O    *")
			print("*       O  *")
			print("************")

		elif x == 4:
			print("************")
			print("*  O    O  *")
			print("*          *")
			print("*  O    O  *")
			print("************")

		elif x == 5:
			print("************")
			print("*  O    O  *")
			print("*    O     *")
			print("*  O    O  *")
			print("************")

		elif x == 6:
			print("************")
			print("*  O    O  *")
			print("*  O    O  *")
			print("*  O    O  *")
			print("************")

		ans = input("Try again?, Y or N: \n").lower()

		if ans == "n":
			print("THANK YOU FOR PLAYING")

		elif ans == "y":
			dice(ans)	
		else:
			print("nnn")
			print("Press Y to try again and N to stop!")
			print("_"*35)
			ans = input("Try again?, Y or N: \n").lower()
			dice(ans)

	elif ans == "n":
		print("THANK YOU FOR PLAYING")

	else:
		print("Press Y to try again and N to stop!")
		print("_"*35)
		ans = input("Try again?, Y or N: \n").lower()
		dice(ans)

ans = "y"
dice(ans)
