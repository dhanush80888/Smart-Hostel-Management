# Generated manually to add snacks column to WeeklyMenu
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0005_weeklymenu_foodfeedback_foodpoll_polloption_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='weeklymenu',
            name='snacks',
            field=models.TextField(blank=True, default='', help_text='Optional snacks for the day'),
        ),
    ]
