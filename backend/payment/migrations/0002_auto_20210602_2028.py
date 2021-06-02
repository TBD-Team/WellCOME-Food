# Generated by Django 3.2.3 on 2021-06-02 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gru',
            old_name='bill_file',
            new_name='receipt',
        ),
        migrations.AddField(
            model_name='gru',
            name='code',
            field=models.CharField(default=None, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gru',
            name='expiration_time',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=19),
        ),
    ]
