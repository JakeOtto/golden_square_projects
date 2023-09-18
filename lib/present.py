#present class
class Present:
    def __init__(self):
        self.contents = None

    def wrap(self, contents):
        if self.contents is not None:
            raise Exception("A contents has already been wrapped.")
        self.contents = contents

    def unwrap(self):
        if self.contents is None:
            raise Exception("No contents have been wrapped.")
        return self.contents
    

# new_present = Present()
# new_present.wrap("hats")
# new_present.wrap("more hats")
# # print (new_present.unwrap())

# # new_present.unwrap