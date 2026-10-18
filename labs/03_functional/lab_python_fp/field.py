def field(items, *args):
    assert len(args) > 0
    for item in items:
        if len(args) == 1:
            value = item.get(args[0])
            if value is not None:
                yield value
        else:
            values = {key: item[key] for key in args
                      if item.get(key) is not None}
            if values:
                yield values


if __name__ == '__main__':
    goods = [{'title': 'Ковер', 'price': 2000},
             {'title': 'Диван для отдыха', 'color': 'black'},
             {'title': None, 'price': None}]
    print(list(field(goods, 'title')))
    print(list(field(goods, 'title', 'price')))
