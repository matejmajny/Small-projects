print("Well so welcome to little quiz about me")
print("Why i made this?: https://bit.ly/3OtaXYj")
print("")
score = 0

#name

name = input("What is my name? ")
if name == "Matej":
  print("Yep thats right")
  score += 1
else:
  print("Wrong answer, but lets continue")


#live
print("")

live = input("In what country i live? ")
if live == "Slovakia":
  print("Yep thats right")
  score += 1 
else:
  print("Wrong answer, but lets continue")


#website
print("")

website = input("What is my Nicepage web URL? ")
if website == "https://matejmajny.github.io":
  print("Yep thats right")
  score += 1
else:
  print("Wrong answer, but lets continue")

print("")

website2 = input("What is my brizy page url? ")
if website2 == "https://matejmajny.tk":
  print("Yep thats right")
  score += 1
else:
  print("Wrong answer, but lets continue")

#Cool
print("")

cool = input("Am i cool? Yes/No ")
if cool == "Yes":
  print("Yep thats right im cool af")
  score += 1
elif cool == "No":
  print("DAMN I AM COOL STOP LYING")
else:
  print("I told you to use just Yes or No, well you lost 1 point")
  score -= 1

  #pre-finnal

score2 = str(score)
if score < 2:
  pass1 = "Bad"
else:
  pass1 = "Well"


#finnal
print("")
print("")
print("")

print("Your score is: " + score2)
print("You passed:" + pass1)

print("")
print("")
input('Press ENTER to exit')
