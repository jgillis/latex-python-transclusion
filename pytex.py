import glob
import subprocess
import os

for f in glob.glob("pytex_*.py"):
  logfilename = f[:-3]+'.log'
  logfile = file(logfilename,'w')
  p = subprocess.Popen(['python',f],stdout=logfile)
  p.wait()
  
  logfile = file(logfilename,'r')
  
  outfile = False
  for l in logfile.readlines():
    if l.startswith('pytex snippet::'):
      num=l[len('pytex snippet::'):].rstrip()
      outfile = file(f[:-3]+'_' + num + '.log','w')
    else:
      if outfile:
        outfile.write(l)
  os.remove(logfilename)
    
