# Migration to add date field to FoodFeedback model
from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0007_add_meal_type_to_foodfeedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodfeedback',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
