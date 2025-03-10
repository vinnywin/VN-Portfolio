
inputTestScore = input("Enter test score: ")
testScore = int(inputTestScore)
inputClassRank = input("Enter class rank: ")
classRank = int(inputClassRank)
if testScore >= 90:
  if classRank >= 25:
    print("Accept")
  else:
    print("Reject")
else:
  if testScore >= 80:
    if classRank >= 50:
      print("Accept")
    else:
      print("Reject")
  else:
    if testScore >= 70:
      if classRank >= 75:
        print("Accept")
      else:
        print("Reject")
    else:
      print("Reject")
print("20250310_NguyenViet_3-2")