# Baidu_OCR
调用百度接口批量处理图片文字识别


#1、文件说明
  accracy.py与百度文字识别接口进行交互
  base.py 是基础版本的文字识别

  ContextProcess.py用于对识别结果字符串进行处理

  test.py用于批量识别文件夹下的所有图片

#2、使用帮助

  待识别图像放在images文件夹下，识别结果以 [图像名+.txt] 格式存放在result文件夹下。

  可识别图片类型 png 、 jpg 、 jpeg 、 bmp

  其他格式请用gif2png.py 转换后再进行识别


