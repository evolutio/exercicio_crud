from core import views
from django.conf.urls import url

urlpatterns = [
    url(r'^api/dapau$', views.dapau),
    url(r'^api/login$', views.login),
    url(r'^api/logout$', views.logout),
    url(r'^api/whoami$', views.whoami),

    url(r'^api/add_todo$', views.add_todo),
    url(r'^api/list_todos$', views.list_todos),
    url(r'^api/pais/save$', views.save_pai),
    url(r'^api/pais$', views.list_pais),
    url(r'^api/pais/(?P<pk>\d+)/remove$', views.remove_pai),
    url(r'^api/pais/(?P<pk>\d+)$', views.get_pai),

]
