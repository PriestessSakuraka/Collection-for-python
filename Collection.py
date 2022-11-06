from collections import OrderedDict

class Collection(OrderedDict):

    def __init__(self, dict = []):
        super().__init__(dict)

    def set(self, key, value):
        self[key] = value

    def find(self, fn = None):
        args_len = len(fn.__code__.co_varnames[:fn.__code__.co_argcount])

        for k, v in self.items():
            if args_len == 1:
                if fn(v): return v
            if args_len == 2:
                if fn(v, k): return v
            if args_len == 3:
                if fn(v, k, self): return v
