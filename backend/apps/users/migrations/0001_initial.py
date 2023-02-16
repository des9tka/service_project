# Generated by Django 4.1.5 on 2023-02-10 11:31

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^(?=.*\\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\\w\\s])[^\\s]{8,20}$', ['Password demands: 8-20 chars', 'contains a number(0-9)', 'contains at least one UpperCase latter', 'contains at least one LowerCase latter', 'contains at least one SpecialChar latter.'])])),
                ('is_active', models.BooleanField(default=False)),
                ('is_employee', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('service', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='services.servicemodel')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'auth_user',
            },
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Z]{2,30}$', ['Name and surname demands: contain 2-30 letters.'])])),
                ('surname', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Z]{2,30}$', ['Name and surname demands: contain 2-30 letters.'])])),
                ('age', models.IntegerField(validators=[django.core.validators.RegexValidator('^(1[4-9] |[2-9]\\d)$', ['For 14+ y.o. users.'])])),
                ('phone', models.BigIntegerField(validators=[django.core.validators.RegexValidator('^[\\+]?[(]?[0-9]{3}[)]?[-\\s\\.]?[0-9]{3}[-\\s\\.]?[0-9]{4,6}$', ['Invalid phone number.'])])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profiles',
            },
        ),
    ]