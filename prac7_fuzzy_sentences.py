from fuzzywuzzy import fuzz
from fuzzywuzzy import process

print("-----------------------------")
s1 = "I love learning Python programming"
s2 = "Python programming is my favourite subject"

print("String 1:", s1)
print("String 2:", s2)
print("FuzzyWuzzy Ratio:", fuzz.ratio(s1, s2))
print("FuzzyWuzzy Partial Ratio:", fuzz.partial_ratio(s1, s2))
print("FuzzyWuzzy Token Sort Ratio:", fuzz.token_sort_ratio(s1, s2))
print("FuzzyWuzzy Token Set Ratio:", fuzz.token_set_ratio(s1, s2))
print("FuzzyWuzzy WRatio:", fuzz.WRatio(s1, s2))
print("-----------------------------")
