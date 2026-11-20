# Practical 7: Fuzzy String Matching Ratios (Short phrases)
# Sample strings:
# s1 = "I like Soft Computing"
# s2 = "I like Hard Computing"
from fuzzywuzzy import fuzz

s1 = "I like Soft Computing"
s2 = "I like Hard Computing"

print("String 1:", s1)
print("String 2:", s2)
print("FuzzyWuzzy Ratio:", fuzz.ratio(s1, s2))
print("FuzzyWuzzy Partial Ratio:", fuzz.partial_ratio(s1, s2))
print("FuzzyWuzzy Token Sort Ratio:", fuzz.token_sort_ratio(s1, s2))
print("FuzzyWuzzy Token Set Ratio:", fuzz.token_set_ratio(s1, s2))
print("FuzzyWuzzy WRatio:", fuzz.WRatio(s1, s2))
