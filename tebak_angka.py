import random
import math
# Mengambil Masukan
lower = int(input("Enter Lower bound:- "))

# Mengambil Masukan
upper = int(input("Enter Upper bound:- "))

# menghasilkan angka acak antara lower & upper
x = random.randint(lower, upper)
print("\n\tYou've only ", 
	round(math.log(upper - lower + 1, 2)),
	" chances to guess the integer!\n")

# Menginisialisasi jumlah tebakan.
count = 0

# untuk perhitungan jumlah tebakan minimum pada rentang lower & upper
while count < math.log(upper - lower + 1, 2):
	count += 1

	# mengambil nomor tebakan sebagai masukan
	guess = int(input("Guess a number:- "))

	# Pengujian kondisi
	if x == guess:
		print("Congratulations you did it in ",
			count, " try")
		# Setelah ditebak, loop akan putus
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")

# Jika menebak lebih dari tebakan yang diminta,
# menunjukkan output ini.
if count >= math.log(upper - lower + 1, 2):
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")