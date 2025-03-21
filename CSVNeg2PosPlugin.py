import sys
import numpy



class CSVNeg2PosPlugin:
   def input(self, filename):
      self.myfile = filename

   def run(self):
      filestuff = open(self.myfile, 'r')
      self.firstline = filestuff.readline()
      lines = []
      for line in filestuff:
         lines.append(line.strip().split(','))

      self.m = len(lines)
      self.bacteria = self.firstline.split(',')
      if (self.bacteria.count('\"\"') != 0):
         self.bacteria.remove('\"\"')
      self.n = len(self.bacteria)
      self.ADJ = numpy.zeros([self.m, self.n])
      i = 0
      for i in range(self.m):
            contents = lines[i].split(',')
            for j in range(self.n):
               value = float(contents[j+1])
               self.ADJ[i][j] = value
            i += 1

   def output(self, filename):
      filestuff2 = open(filename, 'w')
      for i in range(len(self.keep)):
         filestuff2.write(self.firstline[i])
         if (i != len(self.keep)-1):
             filestuff2.write(',')
         else:
             filestuff2.write('\n')
            
      for i in range(self.m):
         filestuff2.write(self.samples[i]+',')
         for j in range(self.n):
            filestuff2.write(str(abs(float(self.ADJ[i][j]))))
            if (j < self.n-1):
               filestuff2.write(",")
            else:
               filestuff2.write("\n")



