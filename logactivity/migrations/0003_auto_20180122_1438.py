# Generated by Django 2.0 on 2018-01-22 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logactivity', '0002_auto_20180122_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
