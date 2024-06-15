from django.urls import  path
from course_app.views import my_view
from category import views

urlpatterns = [
    path('cat_view/',views.cat_view,name='cat_view'),
    path('get_submenu/',views.get_submenu,name='get_submenu'),
    path('get_subsubmenu/', views.get_subsubmenu, name='get_subsubmenu'),
    path('my_view/',my_view,name="my_view"),
    # path('course_interest/',course_interest,name="course_interest"),

]
