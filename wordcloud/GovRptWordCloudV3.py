#GovRptWordCloudv2.py
import jieba
import wordcloud
from imageio import imread
mask=imread("D:/png/China.png")
f=open("D:/txt/新时代中国特色社会主义.txt","r",encoding="utf-8")
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=" ".join(ls)
w=wordcloud.WordCloud(font_path="msyh.ttc", mask=mask,\
    width=1000,height=700, background_color="white",max_words=45 \
    )
w.generate(txt)
w.to_file("D:/png/GovRptV2.png")
