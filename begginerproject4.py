#Remove first n characters from a string
def remove_chars(word,n):
    if n > len(word):
        print("Invalid input!")
    else:
        print(f"The original word is {word}")
        return word[n:]



print(remove_chars("Cybertruck" ,1))


















































