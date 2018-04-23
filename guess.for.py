import time
secret = 22
guessed = False

while True:
    for i in range(5):
        guess = int(raw_input("Guess the secret number (between 1 and 30): "))

        if guess == secret:
            print "You guessed it - congratulations! It's number %s :)" % secret
            break
        else:
            print "Sorry, your guess is not correct... Secret number is not {0}".format(guess)

        if not guessed:
            print "I will sleep for 15 s"
            for j in range(15):
                print "Wait for %s" % str(15 - j)
                time.sleep(1)
