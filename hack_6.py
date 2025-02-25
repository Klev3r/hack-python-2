"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    if not s:
        return ["0"]

    output_list = []
    for i, _ in enumerate(s):
        output_list.append(str(2 * i + 1))
        if i < len(s) - 1:
            output_list.append("-")

    return output_list

# Imprimir los resultados solicitados
print(fn_hack_6(["a", "b", "c", "d", "e"]))
print(fn_hack_6([]))
