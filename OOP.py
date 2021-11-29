import sys, random, argparse
import numpy as np
import math
import turtle
import random
from PIL import Image
from datetime import datetime
from math import gcd


class Spiro:
    def __init__(self,xc,yc,col,R,r,l):
        # створити власну черепаху
        self.t = turtle.Turtle()
        # встановити форму курсору
        self.t.shape('turtle')
        # встановити крок у градусах
        self.step = 5
        # встановити прапор завершення малювання
        self.drawingComplete = False
        # встановити параметри
        self.setparams(xc,yc,col,R,r,l)
        # ініціювати малювання
        self.restart()

    def setparams(self,xc,yc,col,R,r,l):
        self.xc = xc
        self.yc = yc
        self.R = int(R)
        self.r = int(r)
        self.l = l
        self.col = col
        # приведіть r/R до найменшої форми шляхом поділу за допомогою GCD
        gcdValue = gcd(self.r,self.R)
        self.nRot = self.r // gcdValue
        # отримати відношення радіусів
        self.k = r/float(R)
        # встановити колір
        self.t.color(*col)
        # зберігати поточний кут
        self.a = 0

        # перезапустіть малювання
    def restart(self):
            #встановити прапор
            self.drawingComplete = False
            #показати черепаху
            self.t.showturtle()
            #перейти до першої точки
            self.t.up()
            R,k,l = self.R,self.k,self.l
            a = 0.0
            x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
            y = R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k))
            self.t.setpos(self.xc + x, self.yc + y)
            self.t.down()

        # намалюйте все
    def draw(self):
        # намалюйте решту точок
            R, k, l = self.R, self.k, self.l
            for i in range(0,360*self.nRot + 1,self.step):
                a = math.radians(i)
                x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
                y = R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k))
                self.t.setpos(self.xc + x, self.yc + y)
        # готово - сховати черепаху
            self.t.hideturtle()

        # оновлення за один крок
    def update(self):
        # пропустити, якщо зроблено
            if self.drawingComplete:
                return
            # кут збільшення
            self.a += self.step
            # крок малювання
            R,k,l = self.R,self.k,self.l
            # встановити кут
            a = math.radians(self.a)
            x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
            y = R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k))
            self.t.setpos(self.xc + x, self.yc + y)
             # перевірити, чи завершено малювання, і встановити прапор
            if self.a >=360*self.nRot:
                self.drawingComplete = True
                # готово - сховати черепаху
                self.t.hideturtle()

        # очистити все
    def clear(self):
            self.t.clear()
# Клас для анімації спірографів
class SpiriAnimator:
    # конструктор
    def __init__(self,N):
        # значення таймера в мілісекундах
        self.restart = 1
        self.deltaT = 10
        # отримати розміри вікна
        self.width = turtle.window_width()
        self.height = turtle.window_height()
        # створюйте об'єкти spiro
        self.spiros = []
        for i in range(N):
            # генерувати випадкові параметри
            rparams = self.genRandomParams()
            # встановити параметри spiro
            spiro = Spiro(*rparams)
            self.spiros.append(spiro)
        # таймер виклику
        turtle.ontimer(self.update,self.deltaT)
        # перезапустіть креслення sprio
        def restart(self):
            for spiro in self.spiros:
                # очистити
                spiro.clear()
                # генерувати випадкові параметри
                rparams = self.getRandomsParams()
                # встановити параметри spiro
                spiro.setparams(*rparams)
                # перезапустіть малювання
                spiro.restart()

        # генерувати випадкові параметри
    def genRandomParams(self):
            width, height = self.width, self.height
            R = random.randint(50, min(width, height)//2)
            r = random.randint(10, 9*R//10)
            l = random.uniform(0.1, 0.9)
            xc = random.randint(-width//2, width//2)
            yc = random.randint(-height//2, height//2)
            col = (random.random(),
               random.random(),
               random.random())
            return (xc, yc, col, R, r, l)
    def update(self):
         # оновити всі spiros
            nComplete = 0
            for spiro in self.spiros:
                # оновлення
                spiro.update()
                # кількість виконаних
                if spiro.drawingComplete:
                    nComplete+=1
                # якщо всі spiros завершені, перезапустіть

        # увімкнути/вимкнути черепаху
    def toggleTurtles(self):
            for spyro in self.spiros:
                if spiro.t.isvisible():
                    spiro.t.hideturtle()
                else:
                    spiro.t.showturtle()




# зберегти spiro до зображення
def saveDrawing():
    # сховай черепаху
    turtle.hideturtle()
    # створити унікальне ім'я файлу
    dateStr = (datetime.now()).strftime("%d%b%Y-%H%M%S")
    fileName = 'spiro-' + dateStr
    print('збереження малюнка до %s.eps/png' % fileName)
    # отримати tkinter canvas
    canvas = turtle.getcanvas()
    # зберегти зображення постципту
    canvas.postscript(file = fileName + '.eps')
    # використовуйте PIL для перетворення в PNG
    img = Image.open(fileName+'.eps')
    img.save(fileName + '.png', 'png')
    # показати черепаху
    turtle.showturtle()

# функція main().
def main():
    # використовуйте sys.argv, якщо потрібно
    print('генерування спірограф...')
    # створити парсер
    descStr = """Ця програма малює спірографи за допомогою модуля Turtle.
        При запуску без аргументів ця програма малює випадкові спірографи.

        термінологія:
        R: радіус зовнішнього кола.
        r: радіус внутрішнього кола.
        l: відношення відстані отвору до r.
        """
    parser = argparse.ArgumentParser(description=descStr)
    # додати очікувані аргументи
    parser.add_argument( '--sparams' , nargs = 3 , dest = 'sparams' , required = False ,
                        help = "Три аргументи в sparams: R, r, l.")

    # розбір аргументів
    args = parser.parse_args()
    # встановити на 80% ширини екрана
    turtle.setup(width=0.8)
    # встановити форму курсору
    turtle.shape('turtle')

    # встановити назву
    turtle.title("Spinographs")
    # додати обробник ключа для збереження зображень
    turtle.onkey(saveDrawing(),"s")
    # почніть слухати
    turtle.listen()

    # приховати основний курсор черепахи
    turtle.hideturtle()
    # перевіряє аргументи та малює
    if args.sparams:
        params = [float(x) for x in args.sparams]
        # намалювати спірограф із заданими параметрами
        # чорний за замовчуванням
        col = (0.0, 0.0, 0.0)
        spiro = Spiro(0, 0, col, *params)
        spiro.draw()
    else:
        # створити об'єкт аніматора
        spiroAnim = SpiriAnimator(4)
        # додати обробник клавіш, щоб перемикати курсор черепахи
        turtle.onkey(spiroAnim.toggleTurtles,'t')
        # додати обробник ключа, щоб перезапустити анімацію
        turtle.onkey(spiroAnim.restart,'space')
    # почніть основний цикл черепахи
    turtle.mainloop()
# виклик основний
if __name__ == '__main__':
    main()
