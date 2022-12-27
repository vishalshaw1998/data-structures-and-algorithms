# When an object is initialized the object is passed on to a member
# function called __init__ in which we can set the class attributes

class FamilyMember:
    def __init__(self, name) -> None:
        self.name = name

    def printFamilyMember(self):
        print(self.name)


familyMember1 = FamilyMember("Vishal")
familyMember2 = FamilyMember("Neha")
familyMember3 = FamilyMember("Chanda")
familyMember4 = FamilyMember("Bikash")

familyMember1.printFamilyMember()
familyMember2.printFamilyMember()
familyMember3.printFamilyMember()
familyMember4.printFamilyMember()
