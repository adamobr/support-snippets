import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sys


# Data for plotting
def create_graph(_x, _y, _title, _metric, _filename):
  matplotlib.rc('figure', figsize=(100, 10))

  y = _y[2:]
  x = _x

  x_array = []
  y_array = []

  #x_array.append('start')
  for item in x:
    if item <> '': x_array.append(item[-5:]);
  for item in y:
    if item <> '': y_array.append(int(item));

  #print x_array
  #print y_array
  #print x_array
  #print y_array
  fig, ax = plt.subplots()
  ax.plot(x_array, y_array)

  ax.set(xlabel='Time (s)', ylabel=_metric,title=_title)
  ax.grid()

  fig.savefig(_filename.replace('/','_'))
  plt.close(fig)


xx = []
yy = []
linecount = 0
for line in sys.stdin:
  newline =  line.replace('\n','');
  if 'Timestamps' in newline:
    xx = newline[11:]
    xx = xx.split(';')
  else:
    yy = newline.split(';')
    if len(xx) > 1:
      print 'Generating ' + str(yy[:1])
      try:
        create_graph(xx,yy,'Test',str(yy[:1][0]), str(yy[:1][0]).replace('.','_'))
      except:
       print 'Error generating ' + str(yy[:1])
