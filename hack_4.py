"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    if len(s) < 3:
        return s
    else:
        return s[1:-1]

print(fn_hack_4("fooziman"))
print(fn_hack_4("barziman"))
print(fn_hack_4("qux"))