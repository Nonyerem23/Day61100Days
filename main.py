
import datetime, time, os
from replit import db

def addTweet():
  tweet = input("Enter your tweet: ")
  timestamp = datetime.datetime.now()
  key = f"mes{timestamp}"
  db[key] = tweet
  print("Tweet added successfully!")
  time.sleep(1)
  os.system("clear")

def viewTweets():
  matches = db.prefix("mes")
  matches = matches[::-1]
  counter = 0
  for i in matches:
    print(db[i])
    print()
    time.sleep(0.3)
    counter+=1
    if(counter%10==0):
      carryOn = input("Next 10?: ")
      if(carryOn.lower()=="no"):
        break
    time.sleep(1)
    os.system("clear")

while True:
  print("Tweeter")
  menu = input("1: Add Tweet\n2: View Tweets\n> ")
  if menu == "1":
    addTweet()

  else:
    viewTweets()
