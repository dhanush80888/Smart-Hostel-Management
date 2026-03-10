# Generated manually for WeeklyMenu day ordering fix

from django.db import migrations, models

def update_days(apps, schema_editor):
    WeeklyMenu = apps.get_model('hostel', 'WeeklyMenu')
    updates = {
        'monday': '01-monday',
        'tuesday': '02-tuesday',
        'wednesday': '03-wednesday',
        'thursday': '04-thursday',
        'friday': '05-friday',
        'saturday': '06-saturday',
        'sunday': '07-sunday',
    }
    for old, new in updates.items():
        WeeklyMenu.objects.filter(day=old).update(day=new)

class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0010_announcement_priority_alter_announcement_category'),
    ]

    operations = [
        migrations.RunPython(update_days, reverse_code=migrations.RunPython.noop),
        migrations.AlterField(
            model_name='weeklymenu',
            name='day',
            field=models.CharField(max_length=12, choices=[('01-monday', 'Monday'), ('02-tuesday', 'Tuesday'), ('03-wednesday', 'Wednesday'), ('04-thursday', 'Thursday'), ('05-friday', 'Friday'), ('06-saturday', 'Saturday'), ('07-sunday', 'Sunday')], unique=True),
        ),
    ]