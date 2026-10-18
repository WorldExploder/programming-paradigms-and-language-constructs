class Unique:
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = []

    def __iter__(self):
        return self

    def __next__(self):
        for item in self.items:
            key = item.casefold() if self.ignore_case and isinstance(item, str) else item
            if key not in self.seen:
                self.seen.append(key)
                return item
        raise StopIteration


if __name__ == '__main__':
    print(list(Unique([1, 1, 2, 3, 2])))
    print(list(Unique(x for x in ['a', 'A', 'b', 'B'])))
    print(list(Unique(['a', 'A', 'b', 'B'], ignore_case=True)))
