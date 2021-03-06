# Generated by Django 2.1.3 on 2018-11-27 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detective',
            fields=[
                ('Name', models.CharField(max_length=50)),
                ('Father_Name', models.CharField(max_length=50)),
                ('Date_Of_Birth', models.DateField()),
                ('Designation', models.CharField(max_length=50)),
                ('Email_Id', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Police_Officer',
            fields=[
                ('Name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Father_Name', models.CharField(max_length=50)),
                ('Date_Of_Birth', models.DateField()),
                ('Designation', models.CharField(max_length=50)),
                ('Email_Id', models.EmailField(max_length=100)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Police_Station',
            fields=[
                ('Name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Zone', models.CharField(max_length=50)),
                ('District', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='police_officer',
            name='Station_Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Law_And_Order.Police_Station'),
        ),
    ]
