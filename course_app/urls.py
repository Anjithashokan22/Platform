from django.urls import path
from . import views
from category.views import get_menu,get_submenu,get_subsubmenu

urlpatterns =[
    path('index/',views.index,name='index'),
    path('my_view/',views.my_view,name="my_view"),
    # path('course_interest/',views.course_interest,name="course_interest"),
    path('get_menu/', get_menu, name='get_menu'),
    path('get_submenu/',get_submenu,name='get_submenu'),
    path('get_subsubmenu/', get_subsubmenu, name='get_subsubmenu'),
    # path('course_detail/<int:course_id>/', views.course_detail, name='course_detail'),
    path('course_detail/<int:course_id>/', views.course_detail, name='course_detail'),

]
