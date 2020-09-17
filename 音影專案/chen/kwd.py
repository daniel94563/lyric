#encoding=utf-8
import jieba
import jieba.analyse


content = open('chencleaned.txt', 'rb').read()

print "Input：", content

tags = jieba.analyse.extract_tags(content, 10)

print "Output："
print ",".join(tags)


#陳綺貞關鍵詞