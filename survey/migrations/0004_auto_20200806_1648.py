# Generated by Django 3.1 on 2020-08-06 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20200805_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyresponse',
            name='answerbool',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='answershort',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='templatequestion',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='survey.templatequestion'),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='templatequestionchoice',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='survey.templatequestionchoice'),
        ),
        migrations.AlterField(
            model_name='templatequestion',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='templatequestionchoice',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
    ]
