# Generated by Django 4.1.2 on 2022-10-13 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_listdata_description_alter_listdata_done_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listdata',
            name='user',
        ),
        migrations.AlterField(
            model_name='listdata',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listdata',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listdata',
            name='done',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='listdata',
            name='title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
