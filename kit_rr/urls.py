from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^wizard','maps.views.wizard',name = 'wizard'),
    url(r'^edit_catastrophe','maps.views.wizard2',name = 'wizard2'),
    url(r'^panel','maps.views.panel',name = 'panel'),
    url(r'^mapa', 'maps.views.mapa', name='mapa'),
    url(r'^home', 'maps.views.home', name='home'),
    url(r'^catastrophes', 'maps.views.list_catastrophes', name='catastrophes'),
    url(r'^edit_cat', 'maps.views.edit_cat', name='edit_cat'),
    url(r'^$', 'maps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
