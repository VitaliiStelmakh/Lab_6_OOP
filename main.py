import easygui as eg
import xlrd
import xlsxwriter as xlwr
import time

rez=[]
class File:
    
    def __init__(self):
        self.workbook=""
        self.sheet=""

    def get_workbook(self):
        return self.workbook
    def get_sheet(self):
        return self.sheet

    def set_workbook(self, wb):
        self.workbook = wb
    def set_sheet(self, sh):
        self.sheet = sh


    def from_file_to_prog(self):
        book = xlrd.open_workbook(self.get_workbook())
        sheet = book.sheet_by_index(self.get_sheet())
        mass_from_file = [[sheet.cell_value(r, c) for c in range(1,sheet.ncols,1)] for r in range(1,sheet.nrows,1)]
        fin_rez = int(sheet.cell_value(0, 0))
        for i in range(len(mass_from_file)):
            for j in range(len(mass_from_file[0])):
                if mass_from_file[i][j]=='':
                    mass_from_file[i][j]=fin_rez
                mass_from_file[i][j] = int(mass_from_file[i][j])

        return (mass_from_file,fin_rez)

    def prog_to_file(self,s,ms):
        f = open(s,'w')
        for i in range (len(ms)):
            f.write(ms[i])
            f.write("\n\n")
        f.close()


class Algoritm:
    path = []
    path.append([0, 0, 0, 0, 0])
    path.append([0, 0, 0, 0, 0])
    path.append([0, 0, 0, 0, 0])
    path.append([0, 0, 0, 0, 0])
    path.append([0, 0, 0, 0, 0])
    def __init__(self):
        self.mass=[]
        self.final_rez=0

    def get_mass(self):
        return self.mass

    def get_final_rez(self):
        return self.final_rez

    def set_mass(self, ms):
        self.mass = ms

    def set_final_rez(self, fr):
        self.final_rez = fr

    def __str__(self):
        vivod=''
        for i in range(len(self.mass)):
            for j in range(len(self.mass[0])):
                if self.mass[i][j]==self.get_final_rez():
                    vivod += "X" + " "
                else:  vivod += str(self.mass[i][j]) + " "
            vivod += "\n"
        return (vivod)


    def step(self, x, y, sum):
        vivod = ""
        sum+=self.mass[x][y]
        if sum>self.get_final_rez():
            return False
        if x == len(self.mass)-1 and y== len(self.mass[0])-1:
            if(sum!=self.get_final_rez()):
                return False
            self.path[x][y]=True
            for i in range(len(self.mass)):
                for j in range(len(self.mass[0])):
                    if self.path[i][j]==True:
                        vivod+=str(self.mass[i][j]) + " "
                    else: vivod+="-" + " "
                vivod+="\n"
            print(vivod)
            rez.append(vivod)
        self.path[x][y] = True

    #up
        if y > 0 and not(self.path[x][y-1]):
            self.step(x,y-1,sum)

    #down
        if y < 4 and not (self.path[x][y + 1]):
            self.step(x, y + 1, sum)

    #left
        if x > 0 and not (self.path[x-1][y]):
            self.step(x-1, y, sum)

    #right
        if x < 4 and not (self.path[x+1][y]):
            self.step(x+1, y, sum)

        self.path[x][y] = False
        return False


file = File()
a=eg.fileopenbox()
file.set_workbook(a)
file.set_sheet(0)

t = time.time_ns()

alg = Algoritm()
alg.set_mass(file.from_file_to_prog()[0])
alg.set_final_rez(file.from_file_to_prog()[1])
print(alg)

alg.step(0,0,0)

time_alg = time.time_ns() - t
print(f"Час виконання алгоритму = {time_alg/10**9} секунди")

s=eg.filesavebox()+".txt"
file.prog_to_file(s,rez)
