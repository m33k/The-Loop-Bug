print("Sa-k passe Boss?!")
while True:
 g = input("Guess the number:")
 guess = int(g)
 if guess < 5: 
  print("Guess again please! ")
  print("A shame, that's too low")
 elif guess > 5:
  print("Guess again please! ")
  print("That is too darn high")
 else:
  print("You got it!")
  print("The game is terminated!")
  exit()
