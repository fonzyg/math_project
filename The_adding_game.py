print("welcome to the adding game")

questions1 = input("what is 1 + 1")
result = 0
if questions1 == "2":
    result1 = result + 1
    print("correct")
else:
    result1 = result + 0


questions2 = input("what is 2 + 2")
if questions2 == "4":
    result2 = result + 1
    print("correct")
else:
    result2 = result + 0

questions3 = input("what is 3 + 3")
if questions3 == "6":
    result3 = result + 1
    print("correct")
else:
    result3 = result + 0

questions4 = input("what is 4 + 4")
if questions4 == "8":
        result4 = result + 1
        print("correct")
else:
        result4 = result + 0


questions5 = input("what is 5 + 5")

if questions5 == "10":
        result5 = result + 1
        print("correct")
else:
        result5 = result + 0

print(result1+result2+result3+result4+result5)