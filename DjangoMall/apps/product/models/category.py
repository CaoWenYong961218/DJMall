from unicodedata import category
from DJMall.utils import DJMallBaseModel
from django.db import models
# Create your models here.

class DJMallProductCategory(DJMallBaseModel):
    """ 商品分类 """
    pass

class DJMallProductBrand(DJMallBaseModel):
    """ 商品品牌 """
    category = models.ForeignKey(DJMallProductCategory, on_delete=models.CASCADE)