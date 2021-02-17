import re

pattern='^a..u$'
testString="anju"
testString2="anand"
result1=re.match(pattern,testString)
result2=re.match(pattern,testString2)
print("Pattern matching with ",testString,":",result1)
print("Pattern matching with ",testString2,":",result2)

#Patterns
#[abc]
#[a-z]
#[0-5]
#. single char
#^ starts
#$ ends with
# * zero or more occurence  ma*n --- mn,man,maaan,woman
# + one or more occurences ma+n -- man,maan,woman
# ? zero or one occurence ma?n  mn, man,woman
# a{2,3} n,m  -- "abc daat" "anand"
# | or a|e

