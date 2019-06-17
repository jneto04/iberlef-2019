#! *-* encoding: utf-8 *-*
import re,random,math,datetime,argparse,os

class Entity():
   def __init__(self,name="NONE",categ='NONE'):
      self.name = name
      self.categ = categ
   def setName (self,name):
      self.name = name
   def getName(self):
      return self.name
   def setCategory(self,categ):
      self.categ = categ
   def getCategory(self):
      return self.categ
   def __str__(self):
      return "%s/%s"%(self.name,self.categ)
   def __eq__(self, other):
      if isinstance(other, Entity):
          return self.name == other.getName() and self.categ == other.getCategory()
      return False

class Relation():
   def __init__(self,arg1=None,rel=None,arg2=None):
      if type(arg1)==Entity and type(arg2)==Entity:
         self.arg1 = arg1
         self.rel = rel
         self.arg2 = arg2
      elif type(arg1)==str and type(arg2)==str:
         self.arg1 = Entity(name=arg1)
         self.rel = rel
         self.arg2 = Entity(name=arg2)
      elif (type(arg1)==tuple or type(arg1)==list)  and (type(arg2)==tuple or type(arg2)==list):
         self.arg1 = Entity(name=arg1[0],categ=arg1[1])
         self.rel = rel
         self.arg2 = Entity(name=arg2[0],categ=arg2[1])
   def getArg1(self):
         return self.arg1
   def getArg2(self):
         return self.arg2
   def getRel(self):
         return self.rel
   def toTriple(self):
         return (self.arg1.getName(),self.rel,self.arg2.getName()) 
   def toQuintuple(self):
         return (self.arg1.getName(),self.arg1.getCategory(),self.rel,self.arg2.getName(),self.arg2.getCategory()) 
   def __str__(self):
      return "(%s,%s,%s)"%(str(self.arg1),self.rel,str(self.arg2))
   def __eq__(self, other):
      if isinstance(other, Relation):
          return self.arg1 == other.getArg1() and self.rel == other.getRel() and self.arg2 == other.getArg2()
      return False
   def __hash__(self):
      return hash(self.rel)


class Match:
   def __init__(self,match=None, numtokensmatched=0, l1=0, l2=0):
      self.match = match
      self.matched = numtokensmatched
      self.l1 = l1
      self.l2 = l2
   def getMatch(self):
     return self.match
   def getNumTokensMatched(self):
      return self.matched
   def getLengthR1(self):
      return self.l1
   def getLengthR2(self):
      return self.l2
   def __str__(self):
      return "(%i,%i,%i)"%(self.matched,self.l1,self.l2)
   def __iter__(self):
      return (self.matched,self.l1,self.l2)





def normalize(text):
   text = text.lower()
   text = re.sub(" da "," de a ",text)
   text = re.sub(" do "," de o ",text)
   text = re.sub(" dos "," de os ",text)
   text = re.sub(" das "," de as ",text)
   text = re.sub(" na "," en a ",text)
   text = re.sub(" no "," en o ",text)
   text = re.sub(" nos "," en os ",text)
   text = re.sub(" nas "," en as ",text)
   text = re.sub("á","a",text)
   text = re.sub(" pela "," por a ",text)
   text = re.sub(" pelo "," por o ",text)
   text = re.sub(" pelos "," por os ",text)
   text = re.sub(" pelas "," por as ",text)
   text = re.sub("é","e",text)
   text = re.sub("ç","c",text)
   text = re.sub("í","i",text)
   text = re.sub("ó","o",text)
   text = re.sub("ú","u",text)
   text = re.sub("ê","e",text)
   text = re.sub("ô","o",text)
   text = re.sub("à","a a",text)
   text = re.sub("ã","a",text)
   text = re.sub("õ","o",text)
   text = re.sub("ü","u",text)
   text = re.sub("\((?! )","( ",text)
   text = re.sub("\r","",text)
   text = re.sub("[^a-zA-z \n()0-9]","",text)
   text = re.sub("  ","",text)
   return text


def countPartialMatchTest2(rel1,rel2):
#   if len(rel1)!=len(rel2):
#       raise Exception("The relations "+str(rel1)+" and "+str(rel2)+" have different sizes.")
   r1 = map(str.split, map(normalize,rel1.toTriple()))
   r2 = map(str.split, map(normalize,rel2.toTriple()))
   matched = sum([len([word for word in r1[i] if word in r2[i]]) for i in range(len(r1))])
   length1 = sum([len(elem) for elem in r1])
   length2 = sum([len(elem) for elem in r2])
   return (matched,length1,length2)

def countPartialMatchTest1(rel1,rel2):
#   if len(rel1)!=len(rel2):
#       raise Exception("The relations "+str(rel1)+" and "+str(rel2)+" have different sizes.")
   r1 = normalize(rel1.getRel()).split()
   r2 = normalize(rel2.getRel()).split()
   length1 = len(r1)
   length2 = len(r2)
   if rel1.getArg1()==rel2.getArg1() and rel1.getArg2()==rel2.getArg2():
      matched = len([word for word in r1 if word in r2])
      return (matched,length1,length2)
   return (0,length1,length2)
 


def scoreMatch(rel,match,countFunction):
     matchValue = countFunction(rel,match)
     tokensMatched = matchValue[0]
     lengthR1 = matchValue[1]
     lengthR2 = matchValue[2]
     return (2*tokensMatched-(lengthR1+lengthR2)) - abs(lengthR1-lengthR2)
#     return (float(2*tokensMatched)/(lengthR1+lengthR2))-abs(lengthR1-lengthR2)

def findPartialMatchTest2(outputs, gold, aux):
   target = gold[:]
   target.extend(aux)
   partial = dict()
   for rel in outputs:
      valueMatch = lambda x: scoreMatch(rel,x,countPartialMatchTest2)
      bestMatch = max(target,key=valueMatch)
      valueMatch= countPartialMatchTest2(rel,bestMatch)
      answer = Match(bestMatch,valueMatch[0],valueMatch[1],valueMatch[2])
      partial.update([(rel,answer)])
#      gold.remove(bestMatch)
#   return [(rel,partial[rel]) for rel in outputs]
   return partial

def findPartialMatchTest1(outputs, gold,aux):
   target = gold[:]
   target.extend(aux)
   partial = dict()
   for rel in outputs:
      valueMatch = lambda x: scoreMatch(rel,x,countPartialMatchTest1)
      bestMatch = max(target,key=valueMatch)
      valueMatch= countPartialMatchTest1(rel,bestMatch)
      answer = Match(bestMatch,valueMatch[0],valueMatch[1],valueMatch[2])
      partial.update([(rel,answer)])
   return partial
      


def precisionExact(outputs,gold,aux,match):
   exact = [rel for rel in outputs if match[rel].getMatch() not in aux and match[rel].getNumTokensMatched() == match[rel].getLengthR1() == match[rel].getLengthR2()]
   if len([rel for rel in outputs if match[rel].getMatch() not in aux]) == 0:
      return 0
   return float(len(exact))/len([rel for rel in outputs if match[rel].getMatch() not in aux])


def precisionPartial(outputs,gold,aux,match):
#   match = findPartialMatch(outputs,gold)
#   exact = [rel for rel in outputs if match[rel]['tokensMatched'] == match[rel]['lengthr1'] == match[rel]['lengthr2']]
   exact = [rel for rel in outputs if match[rel].getMatch() not in aux and match[rel].getNumTokensMatched() == match[rel].getLengthR1() == match[rel].getLengthR2()]
   nonexact = [rel for rel in outputs if match[rel].getMatch() not in aux and rel not in exact]
   RPC = [0.5*(float(match[rel].getNumTokensMatched())/match[rel].getLengthR1()) for rel in nonexact if match[rel].getLengthR1()!=0]
   if len([rel for rel in outputs if match[rel].getMatch() not in aux])==0:
      return 0
   return (float(len(exact))+sum(RPC))/len([rel for rel in outputs if match[rel].getMatch() not in aux])



def recallExact(outputs,gold,aux,match):
#  match = findPartialMatch(outputs,gold)
   exact = [rel for rel in outputs if match[rel].getMatch() not in aux and match[rel].getNumTokensMatched() == match[rel].getLengthR1() == match[rel].getLengthR2()]
   return float(len(exact))/len(gold)


def recallPartial(outputs,gold,aux,match):
#   match = findPartialMatch(outputs,gold)
   exact = [rel for rel in outputs if match[rel].getMatch() not in aux and match[rel].getNumTokensMatched() == match[rel].getLengthR1() == match[rel].getLengthR2()]
   nonexact = [rel for rel in outputs if match[rel].getMatch() not in aux and rel not in exact]
   RPC = [0.5*(float(match[rel].getNumTokensMatched())/match[rel].getLengthR2()) for rel in nonexact]
   return (float(len(exact))+sum(RPC))/len(gold)

def F1(prec, rec):
   if prec+rec == 0:
      return 0
   return (2*prec*rec)/(prec + rec)




def main():
   #Load parameters
   parser = argparse.ArgumentParser()
   parser.add_argument('--input', type=str, default="./data/train.txt",
     help="Path to the  directory containing output tsv files for all systems being evaluated.")
   parser.add_argument('--test', type=str, default="2",
     help="Which test for Task 2 is being evaluated (1 or 2, default=2).")
   parser.add_argument('--golden', type=str, default="./IberLEFTask2-Test2.gold.tsv",
     help="Path to the tsv with the golden standard for the task.")
   parser.add_argument('--output', type=str, default="./IberLEFTask2Test2Result.csv",
     help="Path to the evaluation output file in csv.")
   parser.add_argument('--aux', type=str, default="",
     help="Path to the evaluation output file in csv.")
   FLAGS = parser.parse_args()


   goldenExtractions = [line.split('\t') for line in open(FLAGS.golden).read().split("\n") if line!='']
   goldenExtractions.pop(0) #remove the header line of the tsv
   gold = [Relation((arg1,cat1),rel,(arg2,cat2)) for _,_,_,arg1,cat1,rel,arg2,cat2 in goldenExtractions]
   aux=list()
   if FLAGS.aux !="":
      for filename in FLAGS.aux.split(","):
         if filename!="":
            fRel = [Relation((arg1,cat1),rel,(arg2,cat2)) for _,_,_,arg1,cat1,rel,arg2,cat2 in [line.split('\t') for line in open(filename).read().split("\n") if line!='']]
            if Relation(("ARGUMENT_1","ARGUMENT_1_CATEGORY"),"RELATION",("ARGUMENT_2","ARGUMENT_2_CATEGORY")) in fRel:
               fRel.remove(Relation(("ARGUMENT_1","ARGUMENT_1_CATEGORY"),"RELATION",("ARGUMENT_2","ARGUMENT_2_CATEGORY")))
            aux.extend(fRel)
      
   output = open(FLAGS.output,"w")
   output.write("SYSTEM,PREC_EXACT,REC_EXACT,F1_EXACT,PREC_PARTIAL,REC_PARTIAL,F1_PARTIAL\n")
   for filename in os.listdir(FLAGS.input):
      print filename
      sysOutputs = re.sub("\r","",open(os.path.join(FLAGS.input,filename)).read()).split("\n")
      sysRelations = [line.split("\t") for line in sysOutputs if line!=""]
      if sysRelations[0]==["SENTENCE_ID","RELATION_ID","SENTENCE","ARGUMENT_1","ARGUMENT_1_CATEGORY","RELATION","ARGUMENT_2","ARGUMENT_2_CATEGORY"]:
        sysRelations.pop(0)
      try:
         rels = [Relation((arg1,cat1),rel,(arg2,cat2)) for _,_,_,arg1,cat1,rel,arg2,cat2 in sysRelations]
      except:
         rels = [Relation((rel[3],rel[4]),rel[5],(rel[6],rel[7])) for rel in sysRelations if len(rel)==8]
         #output.write("%s,-,-,-,-,-,-\n"%(filename)
         #continue
      if FLAGS.test == "2":
         match = findPartialMatchTest2(rels,gold,aux)   
      elif FLAGS.test == "1":
          match = findPartialMatchTest1(rels,gold,aux)   
      else:
          raise Exception("--test flag must only assume values 1 or 2")
      
#      print rels[0],match[rels[0]].getMatch(),match[rels[0]].getNumTokensMatched()
      precExact =  precisionExact(rels,gold,aux,match)
      precPart = precisionPartial(rels,gold,aux,match)
      recExact =  recallExact(rels,gold,aux,match)
      recPart = recallPartial(rels,gold,aux,match)
      f1Exact = F1(precExact,recExact)
      f1Part = F1(precPart,recPart)
      output.write("%s,%f,%f,%f,%f,%f,%f\n"%(filename,precExact,recExact,f1Exact,precPart,recPart,f1Part))
   output.close()

if __name__ == "__main__":
   main()

