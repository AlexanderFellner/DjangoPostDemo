from django.urls import path
from .views import list_post,detail_post,create_post,update_post,delete_post
urlpatterns = [
    path('',list_post),
    path('update/<post_id>',update_post),
    path('delete/<post_id>',delete_post),
    path('postform',create_post),
    path('<post_id>/',detail_post),
    
]
