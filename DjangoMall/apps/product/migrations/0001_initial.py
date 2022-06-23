# Generated by Django 3.2.9 on 2022-06-23 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DJMallProductBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='修改时间')),
                ('is_del', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50, verbose_name='分类名称')),
                ('desc', models.CharField(blank=True, default='', max_length=100, verbose_name='分类描述')),
                ('logo', models.ImageField(blank=True, max_length=200, null=True, upload_to='product/brand/logo/', verbose_name='品牌logo')),
                ('sort', models.PositiveIntegerField(default=0, verbose_name='排序')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DJMallProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='修改时间')),
                ('is_del', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50, verbose_name='分类名称')),
                ('desc', models.CharField(blank=True, default='', max_length=100, verbose_name='分类描述')),
                ('icon', models.ImageField(max_length=200, upload_to='product/category/icon/', verbose_name='分类图标')),
                ('pc_img', models.ImageField(max_length=200, upload_to='product/category/pc/img/', verbose_name='首页楼层背景')),
                ('is_nav', models.BooleanField(default=False, verbose_name='是否为导航')),
                ('sort', models.PositiveIntegerField(default=0, verbose_name='排序')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.djmallproductcategory', verbose_name='父级分类')),
            ],
            options={
                'verbose_name': '商品分类',
                'db_table': 'd_product_category',
                'ordering': ['-sort'],
            },
        ),
        migrations.CreateModel(
            name='DJMallProductSPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='修改时间')),
                ('is_del', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=60, verbose_name='商品标题')),
                ('sub_title', models.CharField(max_length=100, verbose_name='商品副标题')),
                ('desc', models.CharField(blank=True, max_length=150, null=True, verbose_name='商品简介')),
                ('main_picture', models.ImageField(max_length=200, upload_to='product/main/prcture/spu/', verbose_name='商品主图')),
                ('stocks', models.PositiveIntegerField(default=0, verbose_name='总库存')),
                ('sales', models.PositiveIntegerField(default=0, verbose_name='总销量')),
                ('content', models.TextField(verbose_name='商品详情')),
                ('is_new', models.BooleanField(default=False, verbose_name='是否新品')),
                ('is_hot', models.BooleanField(default=False, verbose_name='是否热销')),
                ('is_best', models.BooleanField(default=False, verbose_name='是否精品')),
                ('is_shelves', models.BooleanField(default=False, verbose_name='是否促销')),
                ('after_services', models.TextField(blank=True, default='', verbose_name='售后说明')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.djmallproductbrand', verbose_name='商品品牌')),
                ('category', models.ManyToManyField(to='product.DJMallProductCategory', verbose_name='商品分类')),
            ],
            options={
                'verbose_name': '商品SPU',
                'db_table': 'd_product_spu',
                'ordering': ['-add_date'],
            },
        ),
        migrations.CreateModel(
            name='DJMallProductSPUSpec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='修改时间')),
                ('is_del', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50, verbose_name='规格名称')),
                ('spu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.djmallproductspu', verbose_name='商品')),
            ],
            options={
                'verbose_name': '商品规格',
                'db_table': 'd_product_spu_spec',
                'ordering': ['-add_date'],
            },
        ),
        migrations.CreateModel(
            name='DJMallProductSPUSpecOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='修改时间')),
                ('is_del', models.BooleanField(default=False)),
                ('value', models.CharField(max_length=50, verbose_name='规格值')),
                ('spec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.djmallproductspuspec', verbose_name='规格值')),
            ],
            options={
                'verbose_name': '商品规格值',
                'db_table': 'd_product_spu_spec_option',
                'ordering': ['-add_date'],
            },
        ),
        migrations.CreateModel(
            name='DJMallProductSPUCarouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='修改时间')),
                ('is_del', models.BooleanField(default=False)),
                ('img', models.ImageField(max_length=200, upload_to='product/carouse/img/', verbose_name='轮播图')),
                ('img_url', models.CharField(blank=True, default='', max_length=50, verbose_name='外链图片')),
                ('sort', models.PositiveIntegerField(default=0, verbose_name='排序')),
                ('spu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.djmallproductspu', verbose_name='商品')),
            ],
            options={
                'verbose_name': '商品轮播图',
                'db_table': 'd_product_carouse',
                'ordering': ['-sort'],
            },
        ),
        migrations.CreateModel(
            name='DJMallProductSKU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='修改时间')),
                ('is_del', models.BooleanField(default=False)),
                ('main_picture', models.ImageField(max_length=200, upload_to='product/main/prcture/sku/', verbose_name='商品主图')),
                ('bar_code', models.CharField(blank=True, default='', max_length=50, verbose_name='商品条码')),
                ('sell_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='商品售价')),
                ('market_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='市场价/划线价')),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='成本价')),
                ('stocks', models.PositiveIntegerField(default=0, verbose_name='库存')),
                ('sales', models.PositiveIntegerField(default=0, verbose_name='销量')),
                ('sort', models.PositiveIntegerField(default=0, verbose_name='排序')),
                ('options', models.ManyToManyField(to='product.DJMallProductSPUSpecOption', verbose_name='规格值')),
                ('spu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.djmallproductspu', verbose_name='商品')),
            ],
            options={
                'verbose_name': '商品SKU',
                'db_table': 'd_product_sku',
                'ordering': ['-sort'],
            },
        ),
        migrations.AddField(
            model_name='djmallproductbrand',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.djmallproductcategory'),
        ),
    ]