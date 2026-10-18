from colorama import just_fix_windows_console, Fore, Style
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


if __name__ == '__main__':
    just_fix_windows_console()
    figures = [Rectangle(17, 17, 'синий'), Circle(17, 'зелёный'),
               Square(17, 'красный')]
    for figure in figures:
        print(figure)
    print(Fore.GREEN + 'Внешний пакет colorama вызван.' + Style.RESET_ALL)
