"""
You can modify the functions as you wish or add new ones.
The only important thing is that you take an input value as a string and return an output value as a string.

"""
def translate_function(user_sentence):

    return "diabetes_turkish"

def main():

    # The input sentence is saved as 'user_sentence' here.
    user_sentence = "hi dexter can you translate to turkish do you have diabetes"

    # This is an example. You can completely change the function name, input variables, etc.
    translation = translate_function(user_sentence)

    # returns the translation as a string
    return translation

if __name__ == "__main__":
    print(main())