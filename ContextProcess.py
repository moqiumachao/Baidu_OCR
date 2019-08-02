import numpy as np
import math

class ContextProcess:
    def __init__(self,recognize_result):
        self.recognize_result = recognize_result

    def basic_get_string(self):
        lines = self.recognize_result['words_result']  # list数据，字典集合
        context = ""
        for i, line in enumerate(lines):
            words = line["words"]
            context = context +"\n" + words
        return context
    def location_get_string(self):
        lines = self.recognize_result['words_result']  # list数据，字典集合
        context = ""
        top = 0
        height = 0
        for i, line in enumerate(lines):
            words = line["words"]
            location = line['location']
            temp_top = location['top']
            temp_height = location['height']
            if top*height>0 and abs(temp_top-top)>height:
                context = context +"\n" + words
            else:
                context = context + words
            top = temp_top
            height = temp_height
        return context
    def location_save_txt(self,filename):
        context = self.location_get_string()
        fw = open(filename, "a+", encoding="utf-8")
        fw.write(context)
        fw.close()
    def basic_save_txt(self,filename):
        context = self.basic_get_string()
        fw = open(filename, "a+", encoding="utf-8")
        fw.write(context)
        fw.close()







