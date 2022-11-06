# Collection-for-python

# Features

A OrderedDict with additional methods.

# Requirements

# Usage

Please create javascript file named "Collection".
And copy &amp; paste [code](https://github.com/PriestessSakuraka/Collection-for-python/blob/main/Collection.py),
then use import to get module.

# Example of usage

```py
coll = Collection()

coll.set("z", {
    "name": "0w0",
    "a": 0
})

coll.set("x", {
    "name": "-w-",
    "a": 1
})

coll.set("c", {
    "name": "0w0`",
    "a": 2
})

rlt = coll.find(lambda v: v["a"] == 0)

print(rlt["name"])
```

# Note
