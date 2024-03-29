from django.views.generic import RedirectView
from django.conf.urls import url, include
from . import views
from logactivity.views import MyHistoryList

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='tickets/')),
    url(r'^tickets/', views.ticket_search, name='ticket_search'),
    url(r'^customers/', views.customer_search, name='customer_search'),
    url(r'^ticket/(?P<pk>\d+)/$', views.ticket_detail, name='ticket_detail'),
    url(r'^loaners/$', views.loaner_tickets, name='loaner_tickets'),
    url(r'^customer/(?P<pk>\d+)/$', views.customer_detail, name='customer_detail'),
    url(r'^comment/(?P<pk>\d+)/$', views.comment_detail, name='comment_detail'),
    url(r'^csrs/$', views.csr_list, name='csr_list'),
    url(r'^csr/(?P<csr>\D+)/$', views.csr_detail, name='csr_detail'),
    url(r'^myhistory/$', MyHistoryList.as_view(template_name='myhistory.html'), name='my_history'),
]
