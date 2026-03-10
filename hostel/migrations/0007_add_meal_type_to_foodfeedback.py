# Generated manually to add meal_type field to FoodFeedback
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0006_add_snacks_to_weeklymenu'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodfeedback',
            name='meal_type',
            field=models.CharField(max_length=10, choices=[
                ('breakfast', 'Breakfast'),
                ('lunch', 'Lunch'),
                ('snacks', 'Snacks'),
                ('dinner', 'Dinner'),
            ], default='breakfast'),
            preserve_default=False,
        ),
    ]
