'''
PyQt5 中有多种方法可以刷新组件，下面介绍其中一些常用的方法：

1. update()：可以用于强制重新绘制组件

```python
widget.update()  # 刷新组件
```

2. repaint()：与 update() 类似，也可以用于重新绘制组件

```python
widget.repaint()  # 刷新组件
```

3. setWindowTitle()：可以用于修改窗口的标题，从而实现刷新效果

```python
widget.setWindowTitle("New Title")  # 修改窗口的标题
```

4. setText()：可以用于修改标签等组件的文本内容，从而实现刷新效果

```python
label.setText("New Text")  # 修改标签的文本内容
```

5. clear()：可以用于清空文本框等组件的内容

```python
textEdit.clear()  # 清空文本框的内容
```

6. updateGeometry()：可以用于更新组件的几何信息，从而实现
'''