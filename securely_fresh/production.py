from .settings import *

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES =  {
    'heroku': dj_database_url.config(),
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('aws_rds_name'),
        'USER': os.environ.get('aws_rds_user'),
        'PASSWORD': os.environ.get('aws_rds_pass'),
        'HOST': os.environ.get('aws_rds_port'),
        'PORT': ''
    }
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']
