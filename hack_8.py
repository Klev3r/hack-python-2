"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    if not s:
        return []

    output_list = []
    if len(s) % 2 != 0:  
        for i, char in enumerate(reversed(s)):
            output_list.append(f"{char}-{len(s) - i}")
    else:  
        for i in range(len(s), 0, -1):
            output_list.append(str(i))

    return output_list

print(fn_hack_8(["a", "b", "c", "d", "e"]))
print(fn_hack_8(["a", "b", "c"]))
print(fn_hack_8(["a", "b", "c", "d"]))
print(fn_hack_8(["a", "b"]))