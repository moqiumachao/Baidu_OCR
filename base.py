from aip import AipOcr
from ContextProcess import ContextProcess
import os

APP_ID = "16823719"
API_KEY = "25Ayyb3Ibh7Gdq6qll20YvPi"
SECRET_KEY = "ffxXOgKnxcVqFLB6z62BMByMURCqu8fT"
class BaiduImg():
    def __init__(self, img_path):
        self.img_path = img_path  # 传入图片地址

    """ 读取图片 """

    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def img_ocr(self):
        client = AipOcr(APP_ID,API_KEY,SECRET_KEY)
        image = self.get_file_content(self.img_path)

        """ 调用通用文字识别, 图片参数为本地图片 """
        client.basicGeneral(image)
        """ 如果有可选参数 """
        options = {}
        options["language_type"] = "CHN_ENG"#中英文混合
        options["detect_direction"] = "true"#检测图像朝向
        options["detect_language"] = "true"#检测语言
        options["probability"] = "true"#返回置信度
        """ 带参数调用通用文字识别, 图片参数为本地图片 """
        bendi = client.basicGeneral(image, options)
        return bendi


