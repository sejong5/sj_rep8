import random, easygui
secret = random.randint(1,99)
guess = 0
tries = 0
easygui.msgbox("I have a secret! It is a number from 1 to 99. I'll give you 6 tries")
while guess != secret and tries < 6:
    guess = easygui.integerbox("Please guess the number ~ (" + str(tries+1) + ")")
    if not guess: break
    if guess < secret:
        easygui.msgbox(str(guess) + " is too low, try again!")
    elif guess > secret:
        easygui.msgbox(str(guess) + " is too high, try more!")
    tries = tries + 1
if guess == secret:
    easygui.msgbox("Wow! You got it! Found my secret, well done!^^")
else:
    easygui.msgbox("Sorry but No more chances.... The number was " + str(secret))
    
