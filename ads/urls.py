from django.urls import path
from . import views

urlpatterns = [
    path('', views.ad_list, name='ad_list'),
    path('ads/create/', views.create_ad, name='create_ad'),
    path('ads/<int:ad_id>/', views.ad_detail, name='ad_detail'),
    path('ads/<int:ad_id>/edit/', views.edit_ad, name='edit_ad'),        # редактирование
    path('ads/<int:ad_id>/delete/', views.delete_ad, name='delete_ad'),  # удаление
    path('ads/<int:ad_id>/propose/', views.create_exchange_proposal, name='create_exchange_proposal'),\
    path('proposals/', views.exchange_proposals, name='exchange_proposals'),
    path('proposals/<int:proposal_id>/update/', views.update_proposal_status, name='update_proposal_status'),
]