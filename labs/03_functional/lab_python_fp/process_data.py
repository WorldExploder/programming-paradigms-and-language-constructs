import json
import sys
if __package__:
    from .field import field
    from .unique import Unique
    from .gen_random import gen_random
    from .print_result import print_result
    from .cm_timer import cm_timer_1
else:
    from field import field
    from unique import Unique
    from gen_random import gen_random
    from print_result import print_result
    from cm_timer import cm_timer_1


@print_result
def f1(arg):
    return sorted(Unique(field(arg, 'job-name'), ignore_case=True), key=str.casefold)


@print_result
def f2(arg):
    return list(filter(lambda name: name.casefold().startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda name: name + ' с опытом Python', arg))


@print_result
def f4(arg):
    return [f'{name}, зарплата {salary} руб.'
            for name, salary in zip(arg, gen_random(len(arg), 100000, 200000))]


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Запуск: python -m lab_python_fp.process_data data_light.json')
    with open(sys.argv[1], encoding='utf-8') as file:
        data = json.load(file)
    with cm_timer_1():
        f4(f3(f2(f1(data))))
