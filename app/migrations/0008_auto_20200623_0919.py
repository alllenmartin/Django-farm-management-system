# Generated by Django 3.0.7 on 2020-06-23 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0007_auto_20200623_0858'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheme_number', models.CharField(blank=True, max_length=100)),
                ('farm_name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Schemes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheme_name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='farms',
            name='user',
        ),
        migrations.DeleteModel(
            name='Scheme',
        ),
        migrations.DeleteModel(
            name='Farms',
        ),
        migrations.AddField(
            model_name='farm',
            name='scheme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Schemes'),
        ),
        migrations.AddField(
            model_name='farm',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]