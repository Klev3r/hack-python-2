"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    vowel_map = {
        'a': '@',
        'e': '3',
        'i': '¡',
        'o': '0',
        'u': 'v'
    }

    result = list(s) 


    if result:  
        result[0] = result[0].upper()
        result[-1] = result[-1].upper()

    
    for i in range(len(result)):
        char = result[i].lower()  
        if char in vowel_map:
            result[i] = vowel_map[char]

    return "".join(result) 


print(fn_hack_3("fooziman"))
print(fn_hack_3("barziman"))
print(fn_hack_3("3q"))
print(fn_hack_3("qu"))
print(fn_hack_3("qux"))