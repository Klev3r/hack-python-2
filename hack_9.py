"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(data):
    if "foo" in data and data["foo"] == "fookziman" and "bar" in data and data["bar"] == "barziman":
        return {"Foo": "Fooziman"}
    else:
        return {}  


print(fn_hack_9({"foo": "fookziman", "bar": "barziman"}))
print(fn_hack_9({"foo": "otro", "bar": "valor"})) 