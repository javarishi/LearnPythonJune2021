message = "hello"

def greeting():
    language = "English"
    global message
    message = "Hola!"
    print(message)
    print(language)

def say_hello():
    print("Say Hello :" , message)

greeting()
say_hello()

