# Create a class Employee that will take a full name as argument, as well as a set of none,
# one or more keywords. Each instance should have a name and a
# lastname attributes plus one more attribute for each of the keywords, if any.

class Employee:
    def __init__(self, fullname, **kwargs):
        self.firstname = fullname.split(" ")[0]
        self.lastname = fullname.split(" ")[1]
        for key, val in kwargs.items():
            setattr(self, key, val)