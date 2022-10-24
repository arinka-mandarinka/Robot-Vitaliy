import shutil
import os

from progress_bar import ProgressBar
from robot import RobotV, RobotVita, RobotVitaliy

def print_page(title, text):
    width = shutil.get_terminal_size().columns
    text = title.upper() + '\n\n' + str(text)
    for line in (text + '\n\nPress Enter to continue...').split('\n'):
        print(line.center(width))
    input()
    os.system('cls')

if __name__ == '__main__':
    ProgressBar(prefix='Создание робота:')
    robotV = RobotV()
    print_page('Характеристики робота после создания:', robotV)
    
    ProgressBar(prefix='Обучение робота:')
    robotVita = RobotVita(robotV)
    print_page('Характеристики робота после первичного обучения:', robotVita)
    
    ProgressBar(prefix='Эксплуатация робота:')
    robotVitaliy = RobotVitaliy(robotVita)
    print_page('Характеристики робота после эксплуатации:', robotVitaliy)