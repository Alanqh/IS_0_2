# Generated by Django 4.2 on 2023-05-13 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("customer", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("register", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="servicerecord",
            name="car",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="register.car"
            ),
        ),
        migrations.AddField(
            model_name="servicerecord",
            name="service_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="customer.servicetype"
            ),
        ),
        migrations.AddField(
            model_name="servicerecord",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
