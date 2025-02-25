"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    output_list = []
    for i, item in enumerate(s):
        if isinstance(item, dict):
            for key, value in item.items():
                output_list.append({str(i * 2 + 1): str(i * 2 + 2)})
        elif isinstance(item, tuple):
            output_list.append((str(i * 2 + 1), str(i * 2 + 2)))
    return output_list

print(fn_hack_10([{"a": "b"}, ("c", "d"), {"e": "f"}]))
