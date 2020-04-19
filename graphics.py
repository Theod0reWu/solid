class Screen:
    DEFAULT = [0,0,0]
    def __init__(self, h, w):
        self.pixels = [[Screen.DEFAULT[:] for i in range(w)] for i in range(h)]
        self.height = h
        self.width = w
    def clear(self):
        for h in self.height:
            for w in self.width:
                self.pixels[h][w] = Screen.DEFAULT[:]
    def toFile(self,file):
        enter = "P6\n{} {}\n255\n".format(self.height, self.width)
        with open(file+".ppm", "wb") as f:
            f.write(enter.encode())
            for h in range(self.height):
                for w in range(self.width):
                    c = self.pixels[h][w]
                    f.write(bytes(c))
    def toFileAscii(self,file):
        enter = "P3\n{} {}\n255\n".format(self.height, self.width)
        for i in self.pixels:
            row = ""
            for p in i:
                row += p.getColor() + " "
            enter += row + "\n"
        with open(file+".ppm", "w+") as f:
            f.write(enter)
    def printIt(self):
        enter = "P3\n{} {}\n255\n".format(self.height, self.width)
        for i in self.pixels:
            row = ""
            for p in i:
                row += p.getColor() + " "
            enter += row + "\n"
        print(enter)
    def allPix(self, funct): #funct is a function that takes in a pixel and modifies it
        for h in self.height:
            for w in self.width:
                funct(self.pixels[h][w])
    def allPixCoord(self, funct):
        for h in range(self.height):
            for w in range(self.width):
                funct(w,h,self.pixels[w][h])
    def plot(self,w, h,color):
        #print(h,w)
        try:
            self.pixels[int(h)][int(w)] = color[:]
        except IndexError:
            print("ERROR:",h,w)
    def _Q1(self,x1,y1,x2,y2,color):
        a = y2 - y1
        b = -(x2-x1)
        d = 2*a + b
        while x1 < x2:
            self.plot(x1,y1,color)
            if d > 0:
                y1 += 1
                d += 2*b
            x1+=1
            d+=2*a
    def _Q2(self,x1,y1,x2,y2,color):
        a = y2 - y1
        b = -(x2-x1)
        d = a + 2*b
        while y1 < y2:
            self.plot(x1,y1,color)
            if d < 0:
                x1+=1
                d+=2*a
            y1 += 1
            d += 2*b
    def _Q3(self,x1,y1,x2,y2,color):
        #print("Q3")
        a = y2 - y1
        b = -(x2-x1)
        d = a - 2*b
        #print(a,b,d)
        while y1 > y2:
            self.plot(x1,y1,color)
            if d > 0:
                x1+=1
                d+=2*a
            y1 -= 1
            d -= 2*b
    def _Q4(self,x1,y1,x2,y2,color):
        #print("q4")
        a = y2 - y1
        b = -(x2-x1)
        d = 2*a - b
        while x1 < x2:
            #print("({},{})".format(x1,y1))
            #print(d)
            self.plot(x1,y1,color)
            if d < 0:
                y1 -= 1
                d -= 2*b
            x1+=1
            d+=2*a
    def line(self,x1,y1,x2,y2,color):
        c = [[x1,y1], [x2,y2]]
        c.sort()

        x1,x2 = c[0][0],c[1][0]
        y1,y2 = c[0][1],c[1][1]

        #print("({},{}) ({},{})".format(x1,y1,x2,y2))
        m = 2
        if (x2 != x1):
            m = (y2-y1)/(x2-x1)
        #print(m)
        if (m <= 1 and m > 0):
            self._Q1(x1,y1,x2,y2,color)
        elif(m > 1):
            self._Q2(x1,y1,x2,y2,color)
        elif(m < -1):
            self._Q3(x1,y1,x2,y2,color)
        else:
            self._Q4(x1,y1,x2,y2,color)

from math import radians, cos, sin
class Matrix:
    def __init__(self, points = 0):
        c = [0,0,0,1]
        self.data = [c[:] for i in range(points)]
        self.id = False
    def print(self):
        one,two,three, four = "","","", ""
        for i in self.data:
            one+=str(i[0]) + " "
            two+=str(i[1]) + " "
            three+=str(i[2]) + " "
            four+=str(i[3]) + " "
        print(one+"\n"+two+"\n"+three + "\n"+four)
    def ident(self):#convert to an identity matrix
        self.data = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]][::-1]
        self.id = True
    def trns(self, a = 0, b = 0, c = 0):
        self.ident()
        self.data[0][3] = a
        self.data[1][3] = b
        self.data[2][3] = c
    def scale(self, a = 1, b = 1, c = 1):
        self.ident()
        self.data[0][0] = a
        self.data[1][1] = b
        self.data[2][2] = c
    def rotate(self, axis, deg):
        self.ident()
        rad = radians(deg)
        m = self.data
        if axis == ("x"):
            m[1][1] = cos(rad)
            m[1][2] = -sin(rad)
            m[2][1] = sin(rad)
            m[2][2] = cos(rad)
        elif axis==("y"):
            m[2][2] = cos(rad)
            m[2][0] = -sin(rad)
            m[0][2] = sin(rad)
            m[0][0] = cos(rad)
        elif axis==("z"):
            m[0][0] = cos(rad)
            m[0][1] = -sin(rad)
            m[1][0] = sin(rad)
            m[1][1] = cos(rad)
        else:
            print ("wrong input given to rotate: invalid axis")
            raise ValueError
    def mult(self, m): #m is [4x4] original = m*orginal
        for p in range(len(self.data)):
            new = [0,0,0,0]
            ori = self.data[p]
            for i in range(4):
                f = m.data[i]
                new[i] = f[0]*ori[0] + f[1]*ori[1] + f[2]*ori[2] + f[3]*ori[3]
            self.data[p] = new
    def addLine(self,x1,y1,z1,x2,y2,z2):
        self.data.append([x1,y1,z1,1])
        self.data.append([x2,y2,z2,1])
    def toScreen(self, screen):
        l = 0
        while l < len(self.data):
            screen.line(self.data[l][0],self.data[l][1], self.data[l+1][0], self.data[l+1][1],[255,255,255])
            l+=2
pic = Screen(500,500)
lines = Matrix(0)
lines.addLine(0,0,0,250,0,0)
lines.addLine(0,0,0,0,250,0)
lines.addLine(0,250,0,250,250,0)
lines.addLine(250,0,0,250,250,0)
lines.addLine(0,0,0,0,0,-250)
lines.addLine(0,0,-250,250,0,-250)
lines.addLine(250,0,-250,250,0,0)
lines.addLine(0,0,-250,0,250,-250)
lines.addLine(0,250,-250,0,250,0)
lines.addLine(250,250,0,250,250,-250)
lines.addLine(250,0,-250,250,250,-250)
lines.addLine(0,250,-250,250,250,-250)
move = Matrix()
move.trns(170,125,0)
scale = Matrix()
scale.scale(.1,.1,1)
r=Matrix()
r.rotate("x",-30)
s = Matrix()
s.rotate("y",30)

#lines.mult(scale)
lines.mult(r)
lines.mult(s)
lines.mult(move)
lines.print()
#lines.addLine(0,0,0,0,0,0)
lines.toScreen(pic)
pic.toFile("pic")

