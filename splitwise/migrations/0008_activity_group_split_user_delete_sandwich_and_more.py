# Generated by Django 4.1.6 on 2023-02-08 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('splitwise', '0007_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('split_category', models.CharField(choices=[('EQUAL', 'EQUALLY'), ('UNEQUAL', 'UNEQUALLY'), ('PERCENT', 'BY PERCENTAGES')], default='EQUAL', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Split',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='splitwise.activity')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('phone_no', models.CharField(max_length=11, unique=True)),
                ('default_current', models.CharField(choices=[('INR', 'INDIA'), ('EURO', 'GERMANY'), ('DLR', 'DOLLAR')], default='INR', max_length=5)),
                ('group', models.ManyToManyField(to='splitwise.group')),
            ],
        ),
        migrations.DeleteModel(
            name='Sandwich',
        ),
        migrations.DeleteModel(
            name='Topping',
        ),
        migrations.AddField(
            model_name='split',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='splitwise.user'),
        ),
        migrations.AddField(
            model_name='activity',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='splitwise.user'),
        ),
        migrations.AddField(
            model_name='activity',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='splitwise.group'),
        ),
    ]
