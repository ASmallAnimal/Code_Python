import jieba
import wordcloud
txt="美丽胜于丑陋。\
显式胜于隐式。\
简单胜于复杂。\
复杂胜于复杂。\
扁平比嵌套更好。\
稀疏胜于密集。\
可读性很重要。\
特殊情况还不足以打破规则。\
尽管实用性胜过纯度。\
错误绝不能默默传递。\
除非明确地保持沉默。 它。\
面对模棱两可的想法，拒绝猜测的诱惑。\
应该有一种-最好只有一种-显而易见的方法。\
尽管除非您是荷兰人，否则一开始这种方式可能并不明显。\
现在总比没有好。\
尽管从来没有比现在“正确”好。\
如果实现难以解释，那是个坏主意。\
如果实现易于解释，则可能是个好主意。"
w = wordcloud.WordCloud(width=1000,font_path="msyh.ttc",height=700)
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("D:/png/Character.png")