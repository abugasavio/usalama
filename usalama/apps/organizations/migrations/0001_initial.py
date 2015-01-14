# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields
import django.utils.timezone
from django.conf import settings
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=75)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('author', models.ForeignKey(related_name='organization_create', verbose_name='author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('updated_by', models.ForeignKey(related_name='organization_update', verbose_name='last updated by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user', models.OneToOneField(related_name='organization', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrganizationDriver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('author', models.ForeignKey(related_name='organizationdriver_create', verbose_name='author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('organization', models.ForeignKey(related_name='driver', to='organizations.Organization')),
                ('updated_by', models.ForeignKey(related_name='organizationdriver_update', verbose_name='last updated by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrganizationVehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('registration_number', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('engine_number', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=10, choices=[(b'white', b'White'), (b'silver', b'Silver'), (b'black', b'Black'), (b'grey', b'Grey'), (b'blue', b'Blue'), (b'red', b'Red'), (b'brown', b'Brown'), (b'green', b'Green'), (b'other', b'Other')])),
                ('author', models.ForeignKey(related_name='organizationvehicle_create', verbose_name='author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VehicleMake',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('name', models.CharField(max_length=30)),
                ('author', models.ForeignKey(related_name='vehiclemake_create', verbose_name='author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('updated_by', models.ForeignKey(related_name='vehiclemake_update', verbose_name='last updated by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='organizationvehicle',
            name='make',
            field=models.ForeignKey(related_name='OrganizationVehicle', to='organizations.VehicleMake'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organizationvehicle',
            name='organization',
            field=models.ForeignKey(related_name='organization_vehicle', to='organizations.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organizationvehicle',
            name='updated_by',
            field=models.ForeignKey(related_name='organizationvehicle_update', verbose_name='last updated by', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
