def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "V"
            else:
                translation = translation + "v"
        else:
            translation = translation + letter
    return translation


print(translate(input("enter a phrase")))
