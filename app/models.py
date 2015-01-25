from django.db import models

class UserAccount(models.Model):
    ''' '''

    GENDER_MALE = 0
    GENDER_FEMALE = 1

    STATUS_UNVERIFIED   = 0
    STATUS_VERIFIED     = 1

    uid         = models.AutoField(primary_key = True)
    first_name  = models.CharField(max_length = 30, default = '', blank = True)
    last_name   = models.CharField(max_length = 30, default = '', blank = True)
    password    = models.CharField(max_length = 128, default = '')
    birthday    = models.DateField()
    email       = models.EmailField(max_length = 30, default = '', unique = True)
    photo       = models.FileField(upload_to =  '%Y%m%d')
    gender      = models.SmallIntegerField(choices = ((GENDER_MALE, 'Male'), \
                                                        (GENDER_FEMALE, 'Female'),), \
                                            default = GENDER_MALE)

    status      = models.SmallIntegerField(choices = ((STATUS_UNVERIFIED, 'unverified'), (STATUS_VERIFIED, 'verified')), \
                                            default = STATUS_UNVERIFIED, blank = True)

    login_at    = models.DateTimeField(blank = True, default = '1900-01-01 00:00:00')
    created_at  = models.DateTimeField(auto_now_add = True, db_index = True)
    updated_at  = models.DateTimeField(auto_now = True)


class Balance(models.Model):
    ''' '''
    user_account    = models.ForeignKey('UserAccount')
    amount          = models.DecimalField(max_digits = 5, decimal_places = 2, blank = True, default = 0)
