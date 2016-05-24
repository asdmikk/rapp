# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('address_type_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('subject_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('subject_type_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('country', models.CharField(max_length=50, null=True, blank=True)),
                ('county', models.CharField(max_length=100, null=True, blank=True)),
                ('town_village', models.CharField(max_length=100, null=True, blank=True)),
                ('street_address', models.CharField(max_length=100, null=True, blank=True)),
                ('zipcode', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'address',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AddressType',
            fields=[
                ('address_type', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('type_name', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'db_table': 'address_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('subject_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('contact_type_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('value_text', models.TextField(null=True, blank=True)),
                ('orderby', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('subject_type_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('note', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'contact',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ContactType',
            fields=[
                ('contact_type', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('type_name', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'db_table': 'contact_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('subject_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('subject_type_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
            ],
            options={
                'db_table': 'customer',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('device', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('device_type_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('name', models.TextField(null=True, blank=True)),
                ('reg_no', models.CharField(max_length=100, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('model', models.TextField(null=True, blank=True)),
                ('manufacturer', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'device',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('device_type', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('super_type_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('level', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('type_name', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'db_table': 'device_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('person_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('enterprise_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('struct_unit_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('active', models.CharField(max_length=1, null=True, blank=True)),
            ],
            options={
                'db_table': 'employee',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EmployeeRole',
            fields=[
                ('employee_role', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('employee_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('employee_role_type_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('active', models.CharField(max_length=1, null=True, blank=True)),
            ],
            options={
                'db_table': 'employee_role',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EmployeeRoleType',
            fields=[
                ('employee_role_type', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('type_name', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'db_table': 'employee_role_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('enterprise', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('name', models.TextField(null=True, blank=True)),
                ('full_name', models.TextField(null=True, blank=True)),
                ('created_by', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('updated_by', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'enterprise',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EnterprisePersonRelation',
            fields=[
                ('enterprise_person_relation', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('person_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('enterprise_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('ent_per_relation_type_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
            ],
            options={
                'db_table': 'enterprise_person_relation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EntPerRelationType',
            fields=[
                ('ent_per_relation_type', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('type_name', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'db_table': 'ent_per_relation_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('invoice_status_type_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('service_order_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('customer_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('invoice_date', models.DateField(null=True, blank=True)),
                ('due_date', models.DateField(null=True, blank=True)),
                ('price_total', models.DecimalField(max_digits=69, null=True, blank=True, decimal_places=69)),
                ('receiver_name', models.TextField(null=True, blank=True)),
                ('reference_number', models.TextField(null=True, blank=True)),
                ('receiver_accounts', models.TextField(null=True, blank=True)),
                ('payment_date', models.DateField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'invoice',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='InvoiceRow',
            fields=[
                ('invoice_row', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('invoice_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('service_action_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('service_part_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('action_part_description', models.TextField(null=True, blank=True)),
                ('amount', models.DecimalField(max_digits=69, null=True, blank=True, decimal_places=69)),
                ('price_total', models.DecimalField(max_digits=69, null=True, blank=True, decimal_places=69)),
                ('unit_type', models.CharField(max_length=200, null=True, blank=True)),
                ('unit_price', models.DecimalField(max_digits=69, null=True, blank=True, decimal_places=69)),
                ('invoice_row_type', models.DecimalField(max_digits=1, null=True, blank=True, decimal_places=0)),
            ],
            options={
                'db_table': 'invoice_row',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='InvoiceStatusType',
            fields=[
                ('invoice_status_type', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('type_name', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'db_table': 'invoice_status_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('first_name', models.CharField(max_length=100, null=True, blank=True)),
                ('last_name', models.CharField(max_length=100, null=True, blank=True)),
                ('identity_code', models.CharField(max_length=20, null=True, blank=True)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('created_by', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('updated_by', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'person',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ServiceAction',
            fields=[
                ('service_action', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('service_action_status_type_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('service_type_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('service_device_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('service_order_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('service_amount', models.DecimalField(max_digits=69, null=True, blank=True, decimal_places=69)),
                ('price', models.DecimalField(max_digits=69, null=True, blank=True, decimal_places=69)),
                ('price_updated', models.DateTimeField(null=True, blank=True)),
                ('action_description', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
            ],
            options={
                'db_table': 'service_action',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ServiceActionStatusType',
            fields=[
                ('service_action_status_type', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('type_name', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'db_table': 'service_action_status_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ServiceDevice',
            fields=[
                ('service_device', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('service_device_status_type_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('device_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('service_order_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('to_store', models.DateTimeField(null=True, blank=True)),
                ('from_store', models.DateTimeField(null=True, blank=True)),
                ('service_description', models.TextField(null=True, blank=True)),
                ('status_changed', models.DateTimeField(null=True, blank=True)),
                ('store_status', models.DecimalField(max_digits=1, null=True, blank=True, decimal_places=0)),
            ],
            options={
                'db_table': 'service_device',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ServiceDeviceStatusType',
            fields=[
                ('service_device_status_type', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('type_name', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'db_table': 'service_device_status_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ServiceNote',
            fields=[
                ('service_note', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('customer_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('employee_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('service_order_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('service_device_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('note_author_type', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('note', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'service_note',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ServiceOrder',
            fields=[
                ('service_order', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('so_status_type_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('created_by', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('service_request_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('updated_by', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('status_changed', models.DateTimeField(null=True, blank=True)),
                ('status_changed_by', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('price_total', models.DecimalField(max_digits=69, null=True, blank=True, decimal_places=69)),
                ('note', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'service_order',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ServicePart',
            fields=[
                ('service_part', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('service_order_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('service_device_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('part_name', models.TextField(null=True, blank=True)),
                ('serial_no', models.TextField(null=True, blank=True)),
                ('part_count', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('part_price', models.DecimalField(max_digits=69, null=True, blank=True, decimal_places=69)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
            ],
            options={
                'db_table': 'service_part',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('service_request', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('customer_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('created_by', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('service_desc_by_customer', models.TextField(null=True, blank=True)),
                ('service_desc_by_employee', models.TextField(null=True, blank=True)),
                ('service_request_status_type_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
            ],
            options={
                'db_table': 'service_request',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ServiceRequestStatusType',
            fields=[
                ('service_request_status_type', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('type_name', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'db_table': 'service_request_status_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('service_type', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('service_unit_type_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('type_name', models.CharField(max_length=200, null=True, blank=True)),
                ('service_price', models.DecimalField(max_digits=69, null=True, blank=True, decimal_places=69)),
            ],
            options={
                'db_table': 'service_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ServiceUnitType',
            fields=[
                ('service_unit_type', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('type_name', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'db_table': 'service_unit_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SoStatusType',
            fields=[
                ('so_status_type', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('type_name', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'db_table': 'so_status_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='StructUnit',
            fields=[
                ('struct_unit', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('enterprise_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('upper_unit_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('level', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'db_table': 'struct_unit',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SubjectAttribute',
            fields=[
                ('subject_attribute', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('subject_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('subject_attribute_type_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('subject_type_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('orderby', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('value_text', models.TextField(null=True, blank=True)),
                ('value_number', models.DecimalField(max_digits=69, null=True, blank=True, decimal_places=69)),
                ('value_date', models.DateField(null=True, blank=True)),
                ('data_type', models.DecimalField(max_digits=1, null=True, blank=True, decimal_places=0)),
            ],
            options={
                'db_table': 'subject_attribute',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SubjectAttributeType',
            fields=[
                ('subject_attribute_type', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('subject_type_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('type_name', models.CharField(max_length=200, null=True, blank=True)),
                ('data_type', models.DecimalField(max_digits=1, null=True, blank=True, decimal_places=0)),
                ('orderby', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('required', models.CharField(max_length=1, null=True, blank=True)),
                ('multiple_attributes', models.CharField(max_length=1, null=True, blank=True)),
                ('created_by_default', models.CharField(max_length=1, null=True, blank=True)),
            ],
            options={
                'db_table': 'subject_attribute_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SubjectType',
            fields=[
                ('subject_type', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('type_name', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'db_table': 'subject_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('user_account', models.DecimalField(serialize=False, max_digits=10, primary_key=True, decimal_places=0)),
                ('subject_type_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('subject_fk', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('username', models.CharField(max_length=50, null=True, blank=True)),
                ('passw', models.CharField(max_length=300, null=True, blank=True)),
                ('status', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('valid_from', models.DateField(null=True, blank=True)),
                ('valid_to', models.DateField(null=True, blank=True)),
                ('created_by', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('password_never_expires', models.CharField(max_length=1, null=True, blank=True)),
            ],
            options={
                'db_table': 'user_account',
                'managed': True,
            },
        ),
    ]
