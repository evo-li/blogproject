"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count
import multiprocessing

# bind = '127.0.0.1:8001'
bind = 'unix:/tmp/iterate.site.socket'
workers = multiprocessing.cpu_count() * 2 + 1
# daemon = True
pidfile = '/run/gunicorn.pid'
loglevel = 'info'
errorlog = '/home/evo/sites/iterate.site/blogproject/logfiles/gunicorn_error.log'
accesslog = '/home/evo/sites/iterate.site/blogproject/logfiles/gunicorn_access.log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
