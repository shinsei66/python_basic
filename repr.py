

class test():

    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return "the class to show: {}".format(self.message)

if __name__ == '__main__':
    t = test('Hello world.')
    print(t)