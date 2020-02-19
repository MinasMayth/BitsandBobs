word = str( input("Give me a word, and I'll tell you if it's a palindrome: "))

backwards_word = word[::-1]

if str (word) == str (backwards_word):
    print ("Your word is a palindrome!")
else:
    print ("Your word isn't a palindrome.")
