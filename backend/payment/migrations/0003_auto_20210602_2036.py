# Generated by Django 3.2.3 on 2021-06-02 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20210602_2028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credit',
            name='approved',
        ),
        migrations.AddField(
            model_name='credit',
            name='status',
            field=models.CharField(choices=[('AN', 'InAnalysis'), ('AP', 'Approved'), ('DN', 'Denied')], default='AN', max_length=2),
        ),
    ]
