class Question:
    def GenerateInput(self, data):
        """
        :type data: str
        :return type: str
        """
        lookUpDict = {"*": "*",
                      " ": "0",
                      "&": "1", "'": "11", "(": "111",
                      "A": "2", "B": "22", "C": "222",
                      "D": "3", "E": "33", "F": "333",
                      "G": "4", "H": "44", "I": "444",
                      "J": "5", "K": "55", "L": "555",
                      "M": "6", "N": "66", "O": "666",
                      "P": "7", "Q": "77", "R": "777", "S": "7777",
                      "T": "8", "U": "88", "V": "888",
                      "W": "9", "X": "99", "Y": "999", "Z": "9999"}

        # Handle empty input
        if not data:
            return "#"

        # Handle first input as a "*"
        if data[0] == "*":
            finalStr = "*"
        else:
            finalStr = lookUpDict[data[0].upper()]

        # Store input that is not in the old phone pad
        notInDict = []

        for ele in data[1::]:
            try:
                if ele == "*":
                    finalStr += "*"
                else:
                    ele = ele.upper()
                    if finalStr[-1] in lookUpDict[ele]:
                        finalStr += " " + lookUpDict[ele]
                    else:
                        finalStr += lookUpDict[ele]
            except:
                if ele not in notInDict:
                    notInDict.append(ele)
        if notInDict:
            print("{} character is not in the old phone pad. Therefore it is being removed from the output string.".format(notInDict))
            print("")
        return finalStr + "#"


p1 = Question()
print("This is a python program to convert from alphabet character and some symbol into telephone keypad code. Below are the possible convertion. Character that are unable to convert will taken out of the output.")
print("")
print("* ==> *")
print(" (space) ==> 0")
print("& ==> 1  ' ==> 11  ( ==> 111")
print("A ==> 2  B ==> 22  C ==> 222")
print("D ==> 3  E ==> 33  F ==> 333")
print("G ==> 4  H ==> 44  I ==> 444")
print("J ==> 5  K ==> 55  L ==> 555")
print("M ==> 6  N ==> 66  O ==> 666")
print("P ==> 7  Q ==> 77  R ==> 777  S ==> 7777")
print("T ==> 8  U ==> 88  V ==> 888")
print("W ==> 9  X ==> 99  Y ==> 999  Z ==> 9999")
print("")
x = input("Enter the character: ")
print("")
print("Result ==> {}".format(p1.GenerateInput(x)))
