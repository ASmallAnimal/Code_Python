'''
class new_class():
    variable_1=100
    @classmethod
    def function(cls):   #cls是类的简称，使用类函数
        print(cls.variable_1)
print(new_class.variable_1)
'''

class new_class():
    variable_1='abc'
    def function(self):   #self是要实例化
        print('类的属性是'+self.variable_1)
a=new_class()
a.function()