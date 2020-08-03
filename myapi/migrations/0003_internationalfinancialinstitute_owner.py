# Generated by Django 3.0.8 on 2020-08-02 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapi', '0002_auto_20200730_0623'),
    ]

    operations = [
        migrations.AddField(
            model_name='internationalfinancialinstitute',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ifis', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]