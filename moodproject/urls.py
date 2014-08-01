from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'moodproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'mood.views.home', name = 'home'),
    url(r'^search/$', 'mood.views.search', name = 'search'),
    url(r'^search_results/', 'mood.views.search_results', name = 'search_results'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^user/logout/$', 'django.contrib.auth.views.logout', name='user_logout'),
    url(r'^register/', 'mood.views.register', name ='register'),
    # url(r'^index/', 'mood.views.index', name ='index'),
    url(r'^profile', 'mood.views.profile', name = 'profile'),

)
