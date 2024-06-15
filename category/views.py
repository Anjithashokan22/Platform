# Create your views here.
from django.shortcuts import render
from .models import Menu,SubMenu,SubSubMenu
from django.http import JsonResponse

name='category'
def get_menu(request):
    menu_data = list(Menu.objects.all().values()) 
    return JsonResponse({'menus':menu_data})

def get_submenu(request):
    menu_name = request.GET.get('menu')
    menu = Menu.objects.get(name=menu_name)
    submenus = SubMenu.objects.filter(menu=menu)
    submenu_data = [{'name': submenu.name} for submenu in submenus]
    return JsonResponse({'submenus': submenu_data})


def get_subsubmenu(request):
    submenu_name = request.GET.get('submenu')
    submenu = SubMenu.objects.get(name=submenu_name)
    subsubmenus = SubSubMenu.objects.filter(submenu=submenu)
    subsubmenu_data = [{'name': subsubmenu.name} for subsubmenu in subsubmenus]
    return JsonResponse({'subsubmenus': subsubmenu_data})

def cat_view(request):
    menu_structure = {
    'Technology': [
        {'name': 'Emerging Technologies', 'subsubmenus': ['test1', 'test2', 'test3', 'test4', 'test5']},
        {'name': 'Tools & Software', 'subsubmenus': []},  # Add subsubmenus if any
        # Add other submenus and their subsubmenus
    ],
    'Design': [
        {'name': 'Fashion Designing', 'subsubmenus': []},
        {'name': 'Architecture', 'subsubmenus': []},
        {'name': 'Interior Design', 'subsubmenus': []},
        # Add other submenus and their subsubmenus
    ],
    # Add other menus
}
# Populate database with menu and submenu data
    for menu_name, submenus in menu_structure.items():
        menu, created = Menu.objects.get_or_create(name=menu_name)
        for submenu_data in submenus:
            submenu, created = SubMenu.objects.get_or_create(name=submenu_data['name'], menu=menu)
            for subsubmenu_name in submenu_data['subsubmenus']:
                SubSubMenu.objects.get_or_create(name=subsubmenu_name, submenu=submenu)

    # Render the page with menus data
    menus = Menu.objects.all()
    return render(request, 'test1.html', {'menus': menus})
