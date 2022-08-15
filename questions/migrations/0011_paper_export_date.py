# Generated by Django 4.0.3 on 2022-08-15 16:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_remove_paper_created_at_remove_paper_question_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='export_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
