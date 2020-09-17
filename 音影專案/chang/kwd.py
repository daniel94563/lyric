#encoding=utf-8
import jieba
import jieba.analyse


content = open('changcleaned.txt', 'rb').read()

print "Input：", content

tags = jieba.analyse.extract_tags(content, 20)

print "Output："
print ",".join(tags)

