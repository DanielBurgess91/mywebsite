from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mywebsite.views.home', name='home'),
    url(r'^about/', 'mywebsite.views.about', name='about'),
    # url(r'^blog/', include('blog.urls')),

    # zinnia
    url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
