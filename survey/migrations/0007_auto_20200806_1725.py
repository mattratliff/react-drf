# Generated by Django 3.1 on 2020-08-06 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_delete_templatequestioncontrolheader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templatequestionchoice',
            name='controlchoice',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='survey.templatequestionchoice'),
        ),
    ]
