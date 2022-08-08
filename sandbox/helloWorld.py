class HelloWorld:
    def __init__(self):
        self.message = 'Hello World!'

    def say_hello(self):
        print(self.message)


if __name__ == '__main__':
    hello_world = HelloWorld()
    hello_world.say_hello()
