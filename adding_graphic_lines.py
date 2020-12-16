import re

s = "abc123AUG|GAC|UGAasdfg789"
pattern = "AUG\|(.*?)\|UGA"

substring = re.search(pattern, s).group(2)
print(substring)
#OUTPUT
#GAC
