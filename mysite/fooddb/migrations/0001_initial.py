# Generated by Django 2.2.6 on 2019-10-24 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=200)),
                ('nutriscore', models.IntegerField(default=0)),
                ('picture_url', models.CharField(default='none', max_length=200)),
                ('off_url', models.CharField(default='none', max_length=200)),
                ('sugar_100g', models.IntegerField(default=0)),
                ('salt_100g', models.IntegerField(default=0)),
                ('carbohydrates_100g', models.IntegerField(default=0)),
                ('sodium_100g', models.IntegerField(default=0)),
                ('saturated_fat_100g', models.IntegerField(default=0)),
                ('proteins_100g', models.IntegerField(default=0)),
                ('fat_100g', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Food_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fooddb.Category')),
                ('food_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fooddb.Food')),
            ],
        ),
    ]
