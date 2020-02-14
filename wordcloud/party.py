import jieba
import wordcloud
from imageio import imread
mask=imread("D:/png/China.png")
f=open("D:/txt/不忘初心.txt","r",encoding="ANSI")
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=" ".join(ls)
w=wordcloud.WordCloud(font_path="msyh.ttc", mask=mask,\
    width=1000,height=700, background_color="white",max_words=36\
    )
w.generate(txt)
w.to_file("D:/png/不忘初心.png")
