from django.db import models

# Create your models here.

class Comments(models.Model):
    pno = models.ForeignKey('ProblemInfo', models.DO_NOTHING, db_column='Pno')  # Field name made lowercase.
    maker = models.ForeignKey('UserInfo', models.DO_NOTHING)
    comm = models.CharField(max_length=300, blank=True, null=True)
    comm_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Comments'


class ProblemContent(models.Model):
    pno = models.ForeignKey('ProblemInfo', models.DO_NOTHING, db_column='Pno')  # Field name made lowercase.
    problem_explain = models.CharField(max_length=5000)
    answer = models.CharField(max_length=30)
    ans_explain = models.CharField(max_length=5000)

    class Meta:
        managed = False
        db_table = 'Problem_content'


class ProblemInfo(models.Model):
    pno = models.IntegerField(db_column='Pno', primary_key=True)  # Field name made lowercase.
    sub = models.ForeignKey('Subjects', models.DO_NOTHING, db_column='Sub_id')  # Field name made lowercase.
    maker = models.ForeignKey('UserInfo', models.DO_NOTHING)
    plike = models.IntegerField(db_column='Plike', blank=True, null=True)  # Field name made lowercase.
    pstate = models.IntegerField(db_column='Pstate', blank=True, null=True)  # Field name made lowercase.
    ptime = models.DateTimeField(db_column='Ptime', blank=True, null=True)  # Field name made lowercase.
    trycnt = models.IntegerField(db_column='TryCnt', blank=True, null=True)  # Field name made lowercase.
    accnt = models.IntegerField(db_column='AcCnt', blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'Problem_info'


class Subjects(models.Model):
    sid = models.IntegerField(db_column='Sid', primary_key=True)  # Field name made lowercase.
    sname = models.CharField(db_column='Sname', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Subjects'


class UserInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    pwd = models.CharField(max_length=30)
    upoint = models.IntegerField(db_column='Upoint', blank=True, null=True)  # Field name made lowercase.
    uname = models.CharField(db_column='Uname', max_length=30)  # Field name made lowercase.
    email = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User_info'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'