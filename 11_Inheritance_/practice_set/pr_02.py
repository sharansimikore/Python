#Create a class pets from class animals and furthure create a class dog from pets. Add a method bark to a class dog


class animals:
    pass

class pets(animals):
    pass

class dog(pets):
    pass

    @staticmethod
    def bark():
        print("The dog barks BOW BOW")

a = dog()
a.bark()
