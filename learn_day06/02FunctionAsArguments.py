def shout(text):
    return str(text).upper()


def greetings(func, text):
    print("Hello ", func(text))


greetings(shout, "this is another test")