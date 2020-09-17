
import json
import jieba


ret = open("divide7.txt", "r").read()
seglist = jieba.cut(ret, cut_all=False)


hash = {}
for item in seglist: 
    if item in hash:
      hash[item] += 1
    else:
      hash[item] = 1

#json.dump(hash,open("count.json","w"))

fd = open("count.csv","w")
fd.write("word,count\n")
for k in hash:
  fd.write("%s,%d\n"%(k.encode("big5"),hash[k]))