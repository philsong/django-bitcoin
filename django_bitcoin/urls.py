try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('django_bitcoin.views',
    url(r'^qrcode/(?P<key>.+)$','qrcode_view',name='qrcode'),
)
