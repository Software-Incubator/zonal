# Generated by Django 2.1.4 on 2018-12-24 18:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20181223_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventcoordinatormodel',
            name='img_url',
        ),
        migrations.AddField(
            model_name='eventcoordinatormodel',
            name='image',
            field=models.ImageField(default='d', upload_to='images/events/coordinators/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='color',
            field=models.CharField(default='s', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventregistrationmodel',
            name='faculty_gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default='M', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventcoordinatormodel',
            name='phn_no',
            field=models.CharField(default='333333', max_length=10, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 10', regex='^.{10}$')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventparticipantmodel',
            name='aadhar_no',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 16', regex='^.{16}$')]),
        ),
        migrations.AlterField(
            model_name='eventparticipantmodel',
            name='branch',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='eventparticipantmodel',
            name='fathers_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='eventparticipantmodel',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=10),
        ),
        migrations.AlterField(
            model_name='eventparticipantmodel',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='eventparticipantmodel',
            name='phn_no',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 10', regex='^.{10}$')]),
        ),
        migrations.AlterField(
            model_name='eventparticipantmodel',
            name='university_roll',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='eventparticipantmodel',
            name='year',
            field=models.IntegerField(choices=[(1, '1st'), (2, '2nd'), (3, '3rd'), (4, '4th'), (5, '5th')], default=0),
        ),
        migrations.AlterField(
            model_name='eventregistrationmodel',
            name='faculty_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='eventregistrationmodel',
            name='faculty_phn_no',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 10', regex='^.{10}$')]),
        ),
    ]