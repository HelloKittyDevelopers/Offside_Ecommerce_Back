# Generated by Django 5.0.6 on 2024-06-26 21:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id_category', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id_image', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id_order_item', models.AutoField(primary_key=True, serialize=False)),
                ('order_quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderState',
            fields=[
                ('id_order_state', models.AutoField(primary_key=True, serialize=False)),
                ('order_state', models.CharField(max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderUser',
            fields=[
                ('id_order', models.AutoField(primary_key=True, serialize=False)),
                ('date_order', models.DateField(auto_now_add=True)),
                ('shipping_price', models.FloatField()),
                ('total_payment', models.FloatField()),
                ('address', models.CharField(max_length=80)),
                ('taxes', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id_product', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=4000)),
                ('price', models.IntegerField()),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id_review', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('comment', models.CharField(max_length=250, null=True)),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id_size', models.AutoField(primary_key=True, serialize=False)),
                ('size', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id_stock', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id_type', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddConstraint(
            model_name='category',
            constraint=models.UniqueConstraint(fields=('id_category',), name='category_id_category_un'),
        ),
        migrations.AddField(
            model_name='orderuser',
            name='order_state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.orderstate'),
        ),
        migrations.AddField(
            model_name='orderuser',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.orderuser'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product'),
        ),
        migrations.AddField(
            model_name='image',
            name='product_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='category_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product'),
        ),
        migrations.AddField(
            model_name='productsize',
            name='product_size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product'),
        ),
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='api.product'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productsize',
            name='size_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.size'),
        ),
        migrations.AddField(
            model_name='stock',
            name='product_size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.productsize'),
        ),
        migrations.AddField(
            model_name='product',
            name='type_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.type'),
        ),
        migrations.AddConstraint(
            model_name='orderitem',
            constraint=models.UniqueConstraint(fields=('product', 'order_user'), name='unique_order_item'),
        ),
        migrations.AddConstraint(
            model_name='productcategory',
            constraint=models.UniqueConstraint(fields=('category_product_id', 'product_category_id'), name='productcategory_16_pk'),
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('product', 'user'), name='unique_review'),
        ),
        migrations.AddConstraint(
            model_name='productsize',
            constraint=models.UniqueConstraint(fields=('product_size_id', 'size_product_id'), name='productsize_pk'),
        ),
        migrations.AddConstraint(
            model_name='stock',
            constraint=models.UniqueConstraint(fields=('product_size_id',), name='stock_unique'),
        ),
    ]
