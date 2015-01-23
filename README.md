配置项

修改 setting.py

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
    STATICFILES_DIRS = ('media/uploads',)

    TIME_ZONE = 'Australia/Sydney'

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
    
    # 连表
    Person.objects.select_related('living__province').get(firstname=u"张",lastname=u"三")
    

4) form

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
    
