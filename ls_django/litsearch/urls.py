from django.urls import path

from . import views

#app_name = 'litsearch'

urlpatterns = [
    # ex: /litsearch/
    path('', views.index, name='index'),
    # ex: /litsearch/<int:lit_item_id>/
    # the 'name' as called by the {% url %} template tag
    path('<int:lit_item_id>/', views.details, name='details'),
]