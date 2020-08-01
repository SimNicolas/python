import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def introduction():
    intro = "**** Welcome to my dictionary ****".center(50)
    print('\n' + intro)

def translate(word):

    if word in data:
        return data[word]

    elif word.upper() in data:
        return data[word.upper()]

    elif word.title() in data:
        return data[word.title()]

    elif len(get_close_matches(word, data.keys())) > 0:

        #if get_close_matches(word, data.keys())[0].lower() == word:
            #return data[get_close_matches(word, data.keys())[0]]

        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])

        if yn.upper() == "Y":
            return data[get_close_matches(word, data.keys())[0]]

        elif yn.upper() == "N":
            return "The word doesn't exist, Please try again."

        else:
            return "We didn't understand your entry"
    else:
        return "The word doesn't exist. Please try again."


def ask_def():
    while True:
        word = input("     **(To exit program enter the number 9)**\n\nEnter word: ")
        if word == "9":
            break

        output = translate(word)
        if type(output) == list:
            counter = 1
            for item in output:
                print("Def {}: {}".format(counter, item))
                counter += 1

        else:
            print(output)


introduction()
ask_def()


