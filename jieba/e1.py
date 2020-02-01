#common functions in jieba
import jieba
print(jieba.lcut("中国是一个伟大的国家"))  #precision mode
print(jieba.lcut("中国是一个伟大的国家", cut_all = True)) #full mode
print(jieba.lcut_for_search("中国人民共和国是伟大的"))  #search mode
jieba.add_word("蟒蛇语言") #add a word to the dict
