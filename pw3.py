import re

class Main:
    # File contents will be stored there.
    contents                = None
    # Variable for calculating the average rating
    average: float          = 0.0
    # To count the average we need to know the total number of ratings
    total: int              = 0
    # Are we using regex or not?
    isRegex: bool           = False
    # Available types
    types: dict[str, str]   = None
    # Smallest values
    smallest                = {"Name": None,"Value": None}
    # Biggest values
    highest                 = {"Name": None,"Value": None}
    def __init__(self, file_name: str):
        # Reading the file.
        with open(file_name, "r") as f:
            self.contents = f.read().split("\n")
            # Closing the file.
            # Because we already stored our content in the variable.
            f.close()
    # Function with using regex.
    def withRegex(self):
        self.isRegex = True
        return self
    # Function without using regex.
    def withoutRegex(self):
        self.isRegex = False
        return self
    def setTypes(self, types: dict[str, str]):
        self.types = types
    # Resetting values
    def _reset(self):
        self.average  = 0.0
        self.total    = 0
        self.smallest = {"Name": None,"Value": None}
        self.highest  = {"Name": None,"Value": None}
    def doPerType(self, type: str):
        # Reseting global variables to avoid conflicts
        self._reset()
        # Without the regex
        if not self.isRegex:
            # Skipping the first line
            for line in self.contents[1:]:
                line = line.split(",")
                # Skipping empty lines
                if line == [""]:
                    continue
                # Extracing some values
                # The name of Cereal
                name        = str(line[0])
                # Last element of the array
                rating      = float(line[-1])
                # Cereal type
                cereal_type = str(line[2])
                # Skipping the type if it doesn't match the "type" variable
                if type.lower() != cereal_type.lower():
                    continue
                # Finding smallest one
                if self.smallest["Value"] is None:
                    # If the smallest value is None, setting the first value to compare with
                    self.smallest["Value"] = rating
                    self.smallest["Name"]  = name
                else:
                    if rating < self.smallest["Value"]:
                        self.smallest["Value"]   = rating
                        self.smallest["Name"]    = name
                # Finding highest one
                if self.highest["Value"] is None:
                     # If the highest value is None, setting the first value to compare with
                    self.highest["Value"] = rating
                    self.highest["Name"]  = name
                else:
                    if rating > self.highest["Value"]:
                        self.highest["Value"]   = rating
                        self.highest["Name"]    = name
                # Counting the total
                self.total = self.total + 1
                # Counting the average
                self.average = self.average + rating
            # LOOP END
            print("Cereal type: %s" % self.types[type])
            print("The lowest cereals rating value: %.2f     Cereals name: %s" % (float(self.smallest["Value"]), self.smallest["Name"]))
            print("The average cereals rating value: %.2f" % (float(self.average) / self.total))
            print("The highest cereals rating value: %.2f    Cereals name: %s" % (float(self.highest["Value"]), self.highest["Name"]))
        # With the Regex
        else:
            # Skipping the first line
            for line in self.contents[1:]:
                # Skipping empty lines
                if line == "":
                    continue
                # Extracing some values using regex
                # Getting the first value
                name = re.search("^(.*?),", line).group(1)
                # Getting the last value
                rating = re.search(".*,(.*?)$", line).group(1)
                # Getting cereal type
                cereal_type = re.search("(" + "|".join(self.types) + ")", line).group(1)
                # Skipping the type if it doesn't match the "type" variable
                if type.lower() != cereal_type.lower():
                    continue
                # Finding smallest one
                if self.smallest["Value"] is None:
                    # If the smallest value is None, setting the first value to compare with
                    self.smallest["Value"] = rating
                    self.smallest["Name"]  = name
                else:
                    if rating < self.smallest["Value"]:
                        self.smallest["Value"]   = rating
                        self.smallest["Name"]    = name
                # Finding highest one
                if self.highest["Value"] is None:
                     # If the highest value is None, setting the first value to compare with
                    self.highest["Value"] = rating
                    self.highest["Name"]  = name
                else:
                    if rating > self.highest["Value"]:
                        self.highest["Value"]   = rating
                        self.highest["Name"]    = name
                # Counting the total
                self.total = self.total + 1
                # Counting the average
                self.average = self.average + float(rating)
            # LOOP END
            print("Cereal type: %s" % self.types[type])
            print("The lowest cereals rating value: %.2f     Cereals name: %s" % (float(self.smallest["Value"]), self.smallest["Name"]))
            print("The average cereals rating value: %.2f" % (float(self.average) / self.total))
            print("The highest cereals rating value: %.2f    Cereals name: %s" % (float(self.highest["Value"]), self.highest["Name"]))
               
    def print(self):
        # Checking if types are declared
        if self.types is None:
            print("Cannot continue without declared types.")
            return
        for type in self.types:
            self.doPerType(type)
            
available_types = {
    "C": "Cold",
    "H": "Hot"
}

# Declaring the class and passing the file name in the parameter
main        = Main("cereals.csv")
# Setting types
main.setTypes(available_types)
# With regex
print("*With regex")
withRegex   = main.withRegex().print()
# Without rehex
print("*Without regex")
withoutRegex   = main.withoutRegex().print()