global counter
counter = 0
def wordcounter(string):
  global counter
  for i in range(len(string)):
    if string[i] == " ":
      counter += 1
  counter += 1
  return counter

string = input(str("Your message: "))
wordcounter(string)
print(f"Your message has {counter} words.")