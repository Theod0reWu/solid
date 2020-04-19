from math import radians, cos, sin
class matrix:
    def __init__(self, points = 0):
        c = [0,0,0,1]
        self.data = [c[:] for i in range(points)]
        self.id = False
    def printOut(self):
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
        self.data[3][0] = a
        self.data[3][1] = b
        self.data[3][2] = c
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
            m[2][2] = cos(rad)
            m[2][1] = -1*sin(rad)
            m[1][2] = sin(rad)
            m[1][1] = cos(rad)
        elif axis==("y"):
            m[0][0] = cos(rad)
            m[0][2] = -1 * sin(rad)
            m[2][0] = sin(rad)
            m[2][2] = cos(rad)
        elif axis==("z"):
            m[1][1] = cos(rad)
            m[1][0] = -sin(rad)
            m[0][1] = sin(rad)
            m[0][0] = cos(rad)
        else:
            print ("wrong input given to rotate: invalid axis")
            raise ValueError
    def mult(self, m): #m is [4x4] original = m*orginal
        for p in range(len(self.data)):
            new = [0,0,0,0]
            ori = self.data[p]
            #print("ori", ori)
            for i in range(4):
                f = m.data
                #print("f",f)
                new[i] = f[0][i]*ori[0] + f[1][i]*ori[1] + f[2][i]*ori[2] + f[3][i]*ori[3]
            #print (new)
            self.data[p] = new
    def pmult(self, m): #m is [4x4] original = m*orginal
        for p in range(len(m.data)):
            new = [0,0,0,0]
            ori = m.data[p]
            #print("ori", ori)
            for i in range(4):
                f = self.data
                #print("f",f)
                new[i] = f[0][i]*ori[0] + f[1][i]*ori[1] + f[2][i]*ori[2] + f[3][i]*ori[3]
            #print (new)
            self.data[p] = new
    def addLine(self,x1,y1,z1,x2,y2,z2):
        self.data.append([x1,y1,z1,1])
        self.data.append([x2,y2,z2,1])
    def addPoint(self,x1,y1,z1):
        self.data.append([x1,y1,z1,1])
    def toScreen(self, screen):
        l = 0
        while l < len(self.data):
            screen.line(self.data[l][0],self.data[l][1], self.data[l+1][0], self.data[l+1][1],[255,255,255])
            l+=2
    #auto-mult, only for the master trfm matrix
    def mtrns(self, a = 0, b = 0, c = 0):
        e = matrix()
        e.trns(a,b,c)
        self.mult(e)
    def mscale(self, a = 1, b = 1, c = 1):
        e = matrix()
        e.scale(a,b,c)
        self.mult(e)
    def mrotate(self, axis, deg):
        e = matrix()
        e.rotate(axis,deg)
        self.mult(e)
    
    def pmtrns(self, a = 0, b = 0, c = 0):
        e = matrix()
        e.trns(a,b,c)
        self.pmult(e)
    def pmscale(self, a = 1, b = 1, c = 1):
        e = matrix()
        e.scale(a,b,c)
        self.pmult(e)
    def pmrotate(self, axis, deg):
        e = matrix()
        e.rotate(axis,deg)
        self.pmult(e)
        
