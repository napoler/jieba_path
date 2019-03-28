#jieba path
结巴分词目录快速处理

## 安装
```
pip install jieba_path
```


## 使用
批量处理文件


```

from jieba_path import Jpath
jpath = Jpath()
#处理目录下的txt所有文件
jpath.jieba_path('./data/', 'txt')
#单个文件处理
jpath.jieba_file('./data/001.txt')

#获取目录下的txt文件列表
jpath.file_List('./data/', 'txt')

```