from django.db import migrations

from .. import utils


Project = utils.get_project_model()
ProjectAdmin = utils.get_projectadmin_model()
Tenant = utils.get_tenant_model()
Tenancy = utils.get_tenancy_model()
User = utils.get_user_model()


def create_initial_project(apps, schema_editor):
    if Project.objects.all().first() is None:
        Project.objects.create(name='Initial project')


def create_initial_tenant(apps, schema_editor):
    tenant = Tenant.objects.all().first()
    if tenant is None:
        tenant = Tenant.objects.create(name='Initial tenant')
        project = Project.objects.all().first()
        Tenancy.objects.create(project=project, tenant=tenant)


def create_initial_user(apps, schema_editor):
    user = User.objects.all().first()
    if user is None:
        user = User.objects.create(
            username='user@example.com',
            email='user@example.com',
            first_name='intial',
            last_name='user',
            is_active=True,
            is_superuser=True,
            is_staff=True
        )
        user.set_password('123456')
        user.save()
        project = Project.objects.all().first()
        ProjectAdmin.objects.create(project=project, user=user)


class Migration(migrations.Migration):

    dependencies = [
        ('iamheadless_projects', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_project, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(create_initial_tenant, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(create_initial_user, reverse_code=migrations.RunPython.noop),
    ]
