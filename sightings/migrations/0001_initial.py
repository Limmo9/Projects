# Generated by Django 2.2.7 on 2019-12-08 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(help_text='Latitude of squirrels')),
                ('longitude', models.FloatField(help_text='Longitude of squirrels')),
                ('unique_squirrel_id', models.CharField(help_text='Id of squirrels', max_length=100)),
                ('shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='AM', help_text='AM/PM of sighting', max_length=2)),
                ('date', models.DateField(help_text='Date')),
                ('age', models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile'), ('Other', 'Other')], default='Juvenile', help_text='Type of squirrel', max_length=10)),
                ('primary_fur_color', models.CharField(choices=[('Gray', 'Gary'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black'), ('Other', 'Other')], default='Cinnamon', help_text='Color of squirrels', max_length=10)),
                ('location', models.CharField(choices=[('Ground Plane', 'Ground Plane'), ('Above Plane', 'Above Plane'), ('Other', 'Other')], default='Ground Plane', help_text='Location of first appearance', max_length=15)),
                ('specific_location', models.CharField(help_text='Location description', max_length=256)),
                ('running', models.BooleanField(default=False, help_text='Whether the squirrel was running')),
                ('chasing', models.BooleanField(default=False, help_text='Whether the squirrel was chasing')),
                ('climbing', models.BooleanField(default=False, help_text='Whether the squirrel was climbing')),
                ('eating', models.BooleanField(default=False, help_text='Whether the squirrel was eating')),
                ('foraging', models.BooleanField(default=False, help_text='Whether the squirrel was foraging')),
                ('other_activities', models.CharField(help_text='Other activies', max_length=256)),
                ('kuks', models.BooleanField(default=False, help_text='Whether the squirrel was heard kukking')),
                ('quaas', models.BooleanField(default=False, help_text='Whether the squirrel was heard quaaing')),
                ('moans', models.BooleanField(default=False, help_text='Whether the squirrel was heard moaning')),
                ('tail_flags', models.BooleanField(default=False, help_text='Whether the squirrel was seen flagging its tail')),
                ('tail_twitches', models.BooleanField(default=False, help_text='Whether the squirrel was seen twitching its tail')),
                ('approaches', models.BooleanField(default=False, help_text='Whether the squirrel was seen approaching to human')),
                ('indifferent', models.BooleanField(default=False, help_text='Whether the squirrel was indifferent to human presence')),
                ('runs_from', models.BooleanField(default=False, help_text='Whether the squirrel was seen running from humans')),
            ],
        ),
    ]
