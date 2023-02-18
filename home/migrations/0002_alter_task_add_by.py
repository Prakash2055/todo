# Generated by Django 4.1.2 on 2022-11-02 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='add_by',
            field=models.ForeignKey(db_constraint=False, default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]