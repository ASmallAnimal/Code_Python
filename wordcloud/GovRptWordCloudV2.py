#GovRptWordCloudV2.py
import jieba
import wordcloud
f=open("D:/txt/乡村振兴.txt","r",encoding="ANSI")
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=" ".join(ls)
w=wordcloud.WordCloud(font_path="msyh.ttc", width=1000,\
    height=700, background_color="white",max_words=20\
    )
w.generate(txt)
w.to_file("D:/png/GovRptV2.png")
