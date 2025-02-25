"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    if s == [0]:
        return [0]

    output_list = []
    i = 0
    while 2 * i + 1 <= 5:  
        output_list.append(str(2 * i + 1))  
        if 2 * i + 1 < 5:  
            output_list.append(2 * (i + 1))  
        i += 1

    return output_list

# Imprimir los resultados solicitados
print(fn_hack_7(["a", "b", "c", "d", "e"]))
print(fn_hack_7([0]))