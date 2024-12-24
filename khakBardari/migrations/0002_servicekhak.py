# Generated by Django 4.2.17 on 2024-12-24 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('khakBardari', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceKhak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maghsad', models.CharField(blank=True, max_length=50, null=True)),
                ('mohandes', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('ranande', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='khakBardari.ranande')),
            ],
        ),
    ]