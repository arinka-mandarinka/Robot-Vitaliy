class MoreThanOneRobotException(Exception):
    def __str__(self):
        return '\033[31m{}\033[0m'.format('It is impossible to create another one robot!')

class SingletonRobot(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonRobot, cls).__call__(*args, **kwargs)
            return cls._instances[cls]
        raise MoreThanOneRobotException    

class Robot(metaclass=SingletonRobot):
    def __init__(self):
        super().__init__()
        self._serial_number = 'АА001221-56'
        self._name = '-'
        self._place = '-'
        self._functionality = '-'

    def __str__(self):
        return f'Серийный номер: {self._serial_number}\n' + \
                f'Наименование: {self._name}\n' + \
                f'Место нахождения: {self._place}\n' + \
                f'Функциональность: {self._functionality}'

class RobotV(Robot):
    def __init__(self):
        super().__init__()
        self._name = 'B'
        self._place = 'Завод'

class RobotDecorator(Robot):
    def __init__(self, robot):
        super().__init__()
        self._robot = robot

class RobotVita(RobotDecorator):
    def __init__(self, robot):
        super().__init__(robot)
        self._name = 'Вита'
        self._place = '"ООО Кошмарик"'
        self._functionality = '"постройка домов"\n"постройка сараев"'

class RobotVitaliy(RobotDecorator):
    def __init__(self, robot):
        super().__init__(robot)
        self._name = 'Виталий'
        self._place = '"ООО Кошмарик"'
        self._functionality = robot._functionality + '\n"добавление этажей к постройке"\n"снос верхнего этажа у постройки"'