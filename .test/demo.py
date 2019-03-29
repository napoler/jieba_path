# from jieba_path import jieba_path as Jpath
from jieba_path import Jpath
jpath = Jpath()


jpath.jieba_path('./data/', 'txt')

jpath.file_to_one('./data/', 'jieba', 'jiebaend')
