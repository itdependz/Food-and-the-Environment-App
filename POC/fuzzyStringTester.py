from thefuzz import fuzz

# test thefuzz library

testName = "Rice"
testName2 = "Rice, cooked, NFS"

print("Simple Ratio: ", fuzz.token_sort_ratio(testName, testName2))

