#encoding=utf-8
import jieba
import jieba.analyse


content = open('sodacleaned.txt', 'rb').read()

print "Input：", content

tags = jieba.analyse.extract_tags(content, 10)

print "Output："
print ",".join(tags)