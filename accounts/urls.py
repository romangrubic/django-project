from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile, user_orders, edit_profile, inbox, message_detail, create_message
from accounts import url_reset
from . import views

urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^registration/$', registration, name="registration"),
    url(r'^profile/(?P<id>\d+)/$', user_profile, name="profile"),
    url(r'^orders/$', user_orders, name="orders"),
    url(r'^password-reset/', include(url_reset)),
    url(r'^profile/(?P<id>\d+)/edit/$', edit_profile, name="edit_profile"),
    url(r'^inbox/$', inbox, name="inbox"),
    url(r'^(?P<pk>\d+)/$', message_detail, name='message_detail'),
    url(r'^newMessage/$', create_message, name='create_message'),
]
