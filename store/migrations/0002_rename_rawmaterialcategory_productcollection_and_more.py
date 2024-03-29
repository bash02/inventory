# Generated by Django 4.2.6 on 2023-11-04 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RawMaterialCategory',
            new_name='ProductCollection',
        ),
        migrations.RenameModel(
            old_name='ProductCategory',
            new_name='RawMaterialCollection',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='productcollection',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='rawmaterial',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='rawmaterialcollection',
            options={'ordering': ['title']},
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='rawmaterial',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='collection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.productcollection'),
        ),
        migrations.AddField(
            model_name='rawmaterial',
            name='collection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rawmaterials', to='store.rawmaterialcollection'),
        ),
    ]
