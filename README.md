# 中文「四角号码」数据与工具

> 四角号码，汉语词典常用检字方法之一，用最多5个阿拉伯数字来对汉字进行归类。

四角号码最重要的特定之一是字型相似的字具有相同或者相似的编码。比如 `门` 和 `闫` 比较相似，它们都编码成了 `37001`。`闩` 和它们两个也比较接近，被编码成 `37101`

**这种特性可以被深度学习模型用来作为字的特征之一：字形的特征。**

## 使用
```bash
python ./query.py 民
```

输出

```text
77747
```

## 从原始数据生成
### 数据来源
数据来自于 [资料共享——最全的《四角号码检字表》chm](http://bbs.unispim.com/forum.php?mod=viewthread&tid=31674)

### chmlib 将 CHM 文件 提取成 HTML
TODO

### 解析
```bash
pytohn ./parse.py
```

## 致谢
四角号码数据来自于 [wangyanhan](http://bbs.unispim.com/home.php?mod=space&uid=59433) AT [资料共享——最全的《四角号码检字表》chm](http://bbs.unispim.com/forum.php?mod=viewthread&tid=31674)

