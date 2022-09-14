class Solution:
    def OldPhonePad(self, data):
        """
        :type data: str
        :return type: str
        """
        lookUpTable = [[" "],
                       ["&", "'", "("], ["A", "B", "C"], ["D", "E", "F"],
                       ["G", "H", "I"], ["J", "K", "L"], ["M", "N", "O"],
                       ["P", "Q", "R", "S"], ["T", "U", "V"], ["W", "X", "Y", "Z"]]

        # Handle empty input
        if data[0] == "#":
            return ""

        # Handle none "#" ending input
        if data[-1] != "#":
            data += "#"

        previous = data[0]
        count = 0
        finalStr = ""
        pointer = 1

        while pointer < len(data):
            if data[pointer] == "*" and previous == "*":
                finalStr = finalStr[:-1:]
            elif data[pointer] == "*":
                previous = data[pointer+1]
                count = 0
                pointer += 1
            elif data[pointer] == previous:
                count += 1
                previous = data[pointer]
            else:
                if previous != " " and previous != "*":
                    finalStr += lookUpTable[int(previous)][count]
                count = 0
                previous = data[pointer]
            pointer += 1

        return finalStr


p1 = Solution()

print(p1.OldPhonePad("222 2 22"))
print(p1.OldPhonePad("33#"))
print(p1.OldPhonePad("227*#"))
print(p1.OldPhonePad("4433555 555666#"))
print(p1.OldPhonePad("8 88777444666*664#"))
print(p1.OldPhonePad("4433555999*555666#"))
print(p1.OldPhonePad("4433555 555666***********#"))
print(p1.OldPhonePad("*****4433555999*****55566609666777555304433555 555666#"))

"""
p2 = ["33#", "227*#", "4433555 555666#", "8 88777444666*664#",
      "4433555 555666********#", "#", "*********#",
      "*4433555 555666#",
      "*****4433555999*****4433555 555666096667775553#"]

for ele in p2:
    print(p1.OldPhonePad(ele))
"""
