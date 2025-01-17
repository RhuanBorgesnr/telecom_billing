# Generated by Django 4.2.16 on 2024-11-08 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('start', 'START'), ('end', 'END')], max_length=10)),
                ('timestamp', models.DateTimeField()),
                ('call_id', models.CharField(max_length=50, unique=True)),
                ('source', models.CharField(blank=True, max_length=11, null=True)),
                ('destination', models.CharField(blank=True, max_length=11, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=11)),
                ('period', models.DateField()),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('call_records', models.ManyToManyField(related_name='bills', to='calls.callrecord')),
            ],
        ),
    ]
