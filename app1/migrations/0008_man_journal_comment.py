# Generated by Django 4.1.7 on 2023-10-05 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_mjournal_date_alter_mjournal_difference_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='man_Journal_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300)),
                ('proj', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.pricelist')),
            ],
        ),
    ]
