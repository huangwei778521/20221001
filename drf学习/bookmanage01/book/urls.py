from django.conf.urls import url

from book import views

urlpatterns = [
    # url(r"^login/$",views.BookInfoView.as_view()),
    url(r"^books/$", views.BookInfoView.as_view()),
    url(r"^books/(?P<id>\d+)/$", views.BookInfoIDView.as_view()),
]
