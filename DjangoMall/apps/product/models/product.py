from optparse import Option
from ssl import Options
from django.db import models
from DJMall.utils import DJMallBaseModel
from .category import DJMallProductBrand
# Create your models here.

class DJMallProductSPU(DJMallBaseModel):
    """ 商品SPU """
    brand = models.ForeignKey(
        DJMallProductBrand,
        on_delete=models.CASCADE,
        verbose_name="商品品牌",
    )

class DJMallProductSKU(DJMallBaseModel):
    """ 商品SKU """
    spu = models.ForeignKey(
        DJMallProductSPU,
        on_delete=models.CASCADE,
        verbose_name="商品",
    )
    options = models.ManyToManyField(
        'DJMallProductSPUSpecOption',
        verbose_name='规格值',
    )

class DJMallProductSPUSpec(DJMallBaseModel):
    """ 商品规格选项 """
    spu = models.ForeignKey(
        DJMallProductSPU,
        on_delete=models.CASCADE,
        verbose_name="商品",
    )

class DJMallProductSPUSpecOption(DJMallBaseModel):
    """ 商品规格值 """
    spec = models.ForeignKey(
        DJMallProductSPUSpec,
        on_delete=models.CASCADE,
        verbose_name="规格值",
    )

class DJMallProductSPUCarouse(DJMallBaseModel):
    """ 商品轮播图 """
    spu = models.ForeignKey(
        DJMallProductSPU,
        on_delete=models.CASCADE,
        verbose_name="商品",
    )