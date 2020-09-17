
import json
import jieba
import jieba.posseg

ret = open("chencleaned.txt", "r").read()
seglist = jieba.posseg.cut(ret)


hash = {}
for item in seglist: 
    if item in hash:
      hash[item] += 1
    else:
      hash[item] = 1

#json.dump(hash,open("count.json","w"))

fd = open("chenchiattr2.csv","w")
fd.write("word,attribute,count\n")
for k in hash:
  fd.write("%s,%s,%d\n"%(k.encode("big5").split("/")[0],k.encode("big5").split("/")[1],hash[k]))



