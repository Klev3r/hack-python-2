"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = ""
    for i in range(0, len(s), 2):
        if i + 2 < len(s):
            result += s[i:i+2] + "-"
        else:
            result += s[i:]
            if len(s) % 2 != 0:
                result += "-"
    return result

# Imprimir los resultados solicitados
print(fn_hack_5("fooziman"))
print(fn_hack_5("barziman"))
print(fn_hack_5("qux"))
print(fn_hack_5("eq"))