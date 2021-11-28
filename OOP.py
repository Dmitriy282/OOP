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
        self.nRot = self.r // gcdVal
        # отримати відношення радіусів
        self.k = r/float(R)
        # встановити колір
        self.t.color(*col)
        # зберігати поточний кут
        self.a = 0