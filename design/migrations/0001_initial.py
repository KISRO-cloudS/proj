# Generated by Django 4.1.4 on 2023-02-04 15:35

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About_Us_Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_description', models.TextField(default='about our app', max_length=1000)),
                ('service_title', models.CharField(default='service_name', max_length=100)),
                ('service_description', models.TextField(default='about our service', max_length=300)),
                ('service_title2', models.CharField(default='service_name', max_length=100)),
                ('service_description2', models.TextField(default='about our service', max_length=300)),
                ('service_title3', models.CharField(default='service_name', max_length=100)),
                ('service_description3', models.TextField(default='about our service', max_length=300)),
                ('team_member_name1', models.CharField(default='name', max_length=70)),
                ('team_member_role1', models.CharField(default='role', max_length=100)),
                ('team_member_image1', models.ImageField(default='about_pics/sw.png', upload_to='about_pics')),
                ('team_member_name2', models.CharField(default='name', max_length=70)),
                ('team_member_role2', models.CharField(default='role', max_length=100)),
                ('team_member_image2', models.ImageField(default='about_pics/sw.png', upload_to='about_pics')),
                ('team_member_name3', models.CharField(default='name', max_length=70)),
                ('team_member_role3', models.CharField(default='role', max_length=100)),
                ('team_member_image3', models.ImageField(default='about_pics/sw.png', upload_to='about_pics')),
                ('team_member_name4', models.CharField(default='name', max_length=70)),
                ('team_member_role4', models.CharField(default='role', max_length=100)),
                ('team_member_image4', models.ImageField(default='about_pics/sw.png', upload_to='about_pics')),
            ],
        ),
        migrations.CreateModel(
            name='FollowersCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=1000)),
                ('user', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(default='+', max_length=15)),
                ('message', models.TextField(default='tell us something..', max_length=10000)),
                ('company', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solve_of', models.CharField(choices=[('academic problems', 'academic problems'), ('agricultural problems', 'agricultural problems'), ('adventure problems', 'adventure problems'), ('anxiety problems', 'anxiety problems'), ('business problems', 'business problems'), ('biological problems', 'biological problems'), ('chemical problems', 'chemical problems'), ('ceremonic problems', 'ceremonic problems'), ('confidential problems', 'confidential problems'), ('climentic problems', 'climentic problems'), ('depression problems', 'depression problems'), ('developmental problems', 'developmental problems'), ('boredom problems', 'boredom problems'), ('emotional problems', 'emotional problems'), ('environmental problems', 'environmental problems'), ('fashion and design problems', 'fashion and design problems'), ('financial problems', 'financial problems'), ('friendship problems', 'friendship problems'), ('freedom problems', 'freedom problems'), ('health problems', 'health problems'), ('love and relationship problems', 'love and relationship problems'), ('medical problems', 'medical problems'), ('mental problems', 'mental problems'), ('parental problems', 'parental problems'), ('political problems', 'political problems'), ('religious problems', 'religious problems'), ('research and discovery problems', 'research and discovery problems'), ('stress problems', 'stress problems'), ('shopping problems', 'shopping problems'), ('security problems', 'security problems'), ('self defence problems', 'self defence problems'), ('Self esteem problems', 'Self esteem problems'), ('self care problems', 'self care problems'), ('self control problems', 'self control problems'), ('sports problems', 'sports problems'), ('talental problems', 'talental problems'), ('technological problems', 'technological problems'), ('traditional problems', 'traditional problems'), ('travel problems', 'travel problems'), ('Other problems', 'Other problems')], default='', max_length=1000)),
                ('profile_image', models.ImageField(default='profile_pics/lo.png', upload_to='profile_pics')),
                ('my_slug', models.CharField(default='my slug', max_length=20)),
                ('follow_me_on', models.TextField(default='www.other_sites.com', max_length=300)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='', max_length=1000)),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Single', 'Single'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed'), ('Separated', 'Separated')], default='', max_length=1000)),
                ('talent', models.CharField(default='None', max_length=100)),
                ('street', models.CharField(default='None', max_length=100)),
                ('place_of_birth', models.CharField(default='None', max_length=100)),
                ('country', models.CharField(default='None', max_length=100)),
                ('hobbies', models.CharField(default='None', max_length=100)),
                ('highest_level_of_education', models.CharField(default='None', max_length=100)),
                ('profession', models.CharField(default='None', max_length=100)),
                ('mobile_number', models.CharField(default='None', max_length=100)),
                ('religion', models.CharField(default='None', max_length=100)),
                ('occupation', models.CharField(default='None', max_length=100)),
                ('age', models.PositiveIntegerField(default=0)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('about_me', models.TextField(default='about_me', max_length=200)),
                ('birthday', models.CharField(default='1/1/1999', max_length=10)),
                ('following', models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_on',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.CharField(choices=[('academic problems', 'academic problems'), ('agricultural problems', 'agricultural problems'), ('adventure problems', 'adventure problems'), ('anxiety problems', 'anxiety problems'), ('business problems', 'business problems'), ('biological problems', 'biological problems'), ('chemical problems', 'chemical problems'), ('ceremonic problems', 'ceremonic problems'), ('confidential problems', 'confidential problems'), ('climentic problems', 'climentic problems'), ('depression problems', 'depression problems'), ('developmental problems', 'developmental problems'), ('boredom problems', 'boredom problems'), ('emotional problems', 'emotional problems'), ('environmental problems', 'environmental problems'), ('fashion and design problems', 'fashion and design problems'), ('financial problems', 'financial problems'), ('friendship problems', 'friendship problems'), ('freedom problems', 'freedom problems'), ('health problems', 'health problems'), ('love and relationship problems', 'love and relationship problems'), ('medical problems', 'medical problems'), ('mental problems', 'mental problems'), ('parental problems', 'parental problems'), ('political problems', 'political problems'), ('religious problems', 'religious problems'), ('research and discovery problems', 'research and discovery problems'), ('stress problems', 'stress problems'), ('shopping problems', 'shopping problems'), ('security problems', 'security problems'), ('self defence problems', 'self defence problems'), ('Self esteem problems', 'Self esteem problems'), ('self care problems', 'self care problems'), ('self control problems', 'self control problems'), ('sports problems', 'sports problems'), ('talental problems', 'talental problems'), ('technological problems', 'technological problems'), ('traditional problems', 'traditional problems'), ('travel problems', 'travel problems'), ('Other problems', 'Other problems')], default='', max_length=1000)),
                ('A_brief_Discription', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('clip', models.FileField(default='', upload_to='videos/%Y/%m/%d/')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(default='title', max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poster', to=settings.AUTH_USER_MODEL)),
                ('user_likes', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_preview', models.CharField(blank=True, max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_seen', models.BooleanField(default=False)),
                ('notification_type', models.PositiveSmallIntegerField(choices=[(1, 'Comment')])),
                ('post', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='noti_post', to='design.post')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='noti_from_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='noti_to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Help', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('clip', models.FileField(default='', upload_to='videos/%Y/%m/%d/')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='design.post')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
