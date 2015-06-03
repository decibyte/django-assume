from django.conf.urls import patterns


urlpatterns = patterns('',

    url(r'^auth/user/(\d+)/assume/$', 'assume.views.assume_user', name='assume_user'),

)
