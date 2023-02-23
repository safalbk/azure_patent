# Generated by Django 4.1.6 on 2023-02-23 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0004_alter_inventorsdatatable_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patentdatatable',
            old_name='Country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='patentdatatable',
            old_name='Cpc_Class',
            new_name='cpc_class',
        ),
        migrations.RenameField(
            model_name='patentdatatable',
            old_name='FilingDate',
            new_name='filingdate',
        ),
        migrations.RenameField(
            model_name='patentdatatable',
            old_name='GrantDate',
            new_name='grantdate',
        ),
        migrations.RenameField(
            model_name='patentdatatable',
            old_name='Patentlang',
            new_name='patentlang',
        ),
        migrations.RenameField(
            model_name='patentdatatable',
            old_name='PatentNumber',
            new_name='patentnumber',
        ),
        migrations.RenameField(
            model_name='patentdatatable',
            old_name='PatentTitle',
            new_name='patenttitle',
        ),
        migrations.RenameField(
            model_name='patentdatatable',
            old_name='PatentxmlLink',
            new_name='patentxmllink',
        ),
    ]