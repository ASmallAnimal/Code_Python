import wordcloud
w=wordcloud.WordCloud()
c=wordcloud.WordCloud(font_path="msyh.ttc")
txt = open("D:/txt/threekingdoms.txt","r",encoding="utf-8").read()
w.generate("WordCloud by Python")
c.generate(txt)
w.to_file("D:/png/pyoutfile.png")
w.to_file("D:/png/pyoutfile.png")
'''
1.Configure object parameters
2.load word cloud objects
3.and output word cloud files
'''