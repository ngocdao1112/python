# http://asteriskdocs.org/en/2nd_Edition/asterisk-book-html-chunk/asterisk-CHP-9-SECT-4.html

import sys
import re
import time
import random

# Read and ignore AGI environment (read until blank line)

env = {}
tests = 0

while 1:
   line = sys.stdin.readline().strip()

   if line == '':
      break
   key,data = line.split(':')
   if key[:4] != 'agi_':
      #skip input that doesn't begin with agi_
      sys.stderr.write("Did not work!\n")
      sys.stderr.flush()
      continue
   key = key.strip()
   data = data.strip()
   if key != '':
      env[key] = data

sys.stderr.write("AGI Environment Dump:\n")
sys.stderr.flush()
for key in env.keys():
   sys.stderr.write(" -- %s = %s\n" % (key, env[key]))
   sys.stderr.flush()
# =====================
def checkresult (params):
   params = params.rstrip()
   if re.search('^200',params):
      result = re.search('result=(\d+)',params)
      if (not result):
         sys.stderr.write("FAIL ('%s')\n" % params)
         sys.stderr.flush()
         return -1
      else:
         result = result.group(1)
         #debug("Result:%s Params:%s" % (result, params))
         sys.stderr.write("PASS (%s)\n" % result)
         sys.stderr.flush()
         return result
   else:
      sys.stderr.write("FAIL (unexpected result '%s')\n" % params)
      sys.stderr.flush()
      return -2
# =====================
def sayit (params):
   sys.stderr.write("STREAM FILE %s \"\"\n" % str(params))
   sys.stderr.flush()
   sys.stdout.write("STREAM FILE %s \"\"\n" % str(params))
   sys.stdout.flush()
   result = sys.stdin.readline().strip()
   checkresult(result)
# =====================
def saynumber (params):
   sys.stderr.write("SAY NUMBER %s \"\"\n" % params)
   sys.stderr.flush()
   sys.stdout.write("SAY NUMBER %s \"\"\n" % params)
   sys.stdout.flush()
   result = sys.stdin.readline().strip()
   checkresult(result)
# =====================
def getnumber (prompt, timelimit, digcount):
   sys.stderr.write("GET DATA %s %d %d\n" % (prompt, timelimit, digcount))
   sys.stderr.flush()
   sys.stdout.write("GET DATA %s %d %d\n" % (prompt, timelimit, digcount))
   sys.stdout.flush()
   result = sys.stdin.readline().strip()
   result = checkresult(result)
   sys.stderr.write("digits are %s\n" % result)
   sys.stderr.flush()
   if result:
      return result
   else:
      result = -1
# =====================
limit=20
digitcount=2
score=0
count=0
ttanswer=5000
# =====================
starttime = time.time()
t = time.time() - starttime
# =====================
sayit("subtraction-game-welcome")
# =====================
while ( t < 180 ):

   big = random.randint(0,limit+1)
   big += 10
   subt= random.randint(0,big)
   ans = big - subt
   count += 1

   #give problem:
   sayit("subtraction-game-next")
   saynumber(big)
   sayit("minus")
   saynumber(subt)
   res = getnumber("equals",ttanswer,digitcount)

   if (int(res) == ans) :
      score+=1
      sayit("subtraction-game-good")
   else :
      sayit("subtraction-game-wrong")
      saynumber(ans)

   t = time.time() - starttime
# =====================
pct = float(score)/float(count)*100
sys.stderr.write("Percentage correct is %d\n" % pct)
sys.stderr.flush()

sayit("subtraction-game-timesup")
saynumber(score)
sayit("subtraction-game-right")
saynumber(count)
sayit("subtraction-game-pct")
saynumber(pct)
# =====================