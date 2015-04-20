ip
curl http://169.254.169.254/latest/meta-data/public-ipv4

配置项

修改 setting.py
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'Australia/Sydney'
    USE_I18N = True
    # USE_L10N = True

    DATE_FORMAT = 'Y-m-d'
    USE_TZ = False
    LOGIN_URL = '/'
    BACKEND_LOGIN_URL = '/backend'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'mydatabase',
            'USER': 'mydatabaseuser',
            'PASSWORD': 'mypassword',
            'HOST': '127.0.0.1',
            'PORT': '3306',
              'OPTIONS': {
                'init_command': 'SET storage_engine=INNODB',
                }
        }
    }

添加模块名到 installed_app, ('apps.user_account',)

ROOT_URLCONF, WSGI_APPLICATION 为 urls.py, wsgi.py对应位置

    MEDIA_ROOT = 'media/uploads'
    MEDIA_URL = '/media/uploads/'
    STATIC_ROOT = ''
    STATIC_URL = '/static/'
    
    STATICFILES_DIRS = ('static',)
    TEMPLATE_DIRS=('templates',)
    MEDIAFILES_DIRS = ('media/uploads',)

    STATIC_URL = '/static/'
    STATIC_ROOT = '/var/www/vportal.static/'
    
    STATICFILES_DIRS = (
        # Put strings here, like "/home/html/static" or "C:/www/django/static".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        '/var/www/vportal/media',
        # '/var/www/vportal.static/',    # Enable this specially for debug server
    )
    
    TMP_FILE_ROOT = '/var/www/vportal.tmp/'
    
    DOC_FILE_ROOT = '/var/www/vportal.doc/'
    
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.7/howto/static-files/
    
    TEMPLATE_DIRS = (
        '/var/www/vportal/templates',
    )


映射上传文件 urls.py

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media/'}),
    (r'^mydata/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$','demo.views.mydata')


常用命令

1) 创建 APP。

     cd apps;
     django-admin startapp user_account

2) 创建表 models

     CREATE DATABASE <dbname> CHARACTER SET utf8;

允许从任何主机访问测试服务器

     python manage.py runserver 0.0.0.0:8000
     python manage.py runserver --settings=mysite.settings.local
     python manage.py runserver 0.0.0.0:8000 --settings=settings

     python manage.py makemigrations --setting=settings 有时不好用需要手动先删除migration
     python manage.py migrate --settings=settings 修改表结构同样重复执行这两条


3) SQL

    User.objects.filter(username__exact=username).update(name=name)  
    Publisher.objects.filter(name__contains="press")
                .filter(pub_date__year=2006)
                .filter(headline__startswith='What')
                .filter(pub_date__gte=datetime.date.today())
                .filter(pub_date__gte=datetime(2005, 1, 30)
                .filter(pub_date__lte='2006-01-01')
                .filter(name__iexact="beatles blog")
                .order_by('-headline')[0:5]
    Poll.objects.get(
        Q(question__startswith='Who'),
        Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
    )
    
    # 连表
    Person.objects.select_related('living__province').get(firstname=u"张",lastname=u"三")
    Blog.objects.filter(entry__authors__name__isnull=True)
    
    b = Blog.objects.get(id=1)
    b.entry_set.filter(headline__contains='Lennon')
    b.entry_set.count()

    # transaction
    from django.db import transaction
    with transaction.atomic():

4) form
    #
    # be careful: all vaule in cleaned_data are string
    #
    def __init__(self, user, *args, **kwargs):
        now = datetime.now().strftime('%Y-%m-%d')
        self.fields['for_sale_date'].initial = now
        self.fields['position'] = forms.ChoiceField(choices=position_choice, required=True)
        
        super(CreateAgreementForm, self).__init__(*args, **kwargs)
        
    def clean_username(self):
        '''验证用户输入的用户名的合法性'''
        username = self.cleaned_data['username']    
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('用户名中只能包含字母、数字和下划线')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('用户名已存在！')
        
    def clean(self):
        if sales_method == str(Agreement.SALES_METHOD_EOI) and (eoi_name == '' or not eoi_file):
            raise forms.ValidationError('Please input EOI Name and upload EOI File')
            
        return self.cleaned_data
        
    def save(self, force_insert=False, force_update=False, commit=True):
        agreement = super(UpdateAgreementForm, self).save(commit=False)
        agreement.save()
        return agreement

    class Meta:
        model = Business
        fields = ['abn', 'acn', ...,]

5) Model
    
    class Agreement(models.Model):
        
        def save(self, *args, **kwargs):
            self.agreement_title = self.agreement_title.lower()
            super(Agreement, self).save(*args, **kwargs)
        
        def __unicode__(self):
            return self.agreement_title
            
        class Meta:
            ordering = ['-updated_at']

6) Tuple, List, Dict

    ";".join(["%s=%s" % (k, v) for k, v in params.items()]) // params can be tuple, list or dict

    
7) String

    ";".join(["%s=%s" % (k, v) for k, v in params.items()]) // params can be tuple, list or dict
    >>> s = 'server=mpilgrim;uid=sa;database=master;pwd=secret'
    >>> s.split(";")    1
    ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
    >>> s.split(";", 1) 2
    ['server=mpilgrim', 'uid=sa;database=master;pwd=secret']

    # sort
    order_notifications = collections.OrderedDict() // sorting by the order that items were inserted
    
    d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}

    # dictionary sorted by key
    OrderedDict(sorted(d.items(), key=lambda t: t[0])) 
    >>> OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
    
    >>> # dictionary sorted by value
    >>> OrderedDict(sorted(d.items(), key=lambda t: t[1]))
    OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])
    
    >>> # dictionary sorted by length of the key string
    >>> OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
    OrderedDict([('pear', 1), ('apple', 4), ('orange', 2), ('banana', 3)])
    
    
8) datetime
    import time
    import datetime

    print "Time in seconds since the epoch: %s" % time.time()    // 1349271346.46
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%I:%S')          // 2015-04-15 10:10:10
    diff_datetime = (datetime.date.today() - datetime.timedelta(365 * 3)).strftime('%Y-%m-%d %H:%I:%S') // 3 years ago
    
9) Template

10) view
    raise Http404('Page does not exist')
