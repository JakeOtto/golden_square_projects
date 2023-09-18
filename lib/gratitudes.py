#gratitudes file

class Gratitudes:
    def __init__(self):
        self.gratitudes = []

    def add(self, gratitude):
        self.gratitudes.append(gratitude)

    def format(self):
        formatted = "Be grateful for: "
        formatted += ", ".join(self.gratitudes)
        return formatted
    

# new_gratitude = Gratitudes()
# new_gratitude.add("pizza")
# new_gratitude.format()
# print (new_gratitude.format())