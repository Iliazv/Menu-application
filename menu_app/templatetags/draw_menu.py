from django import template
from menu_app.models import Menu


register = template.Library()

@register.inclusion_tag('menu_app/menu_template.html', takes_context=True)
def draw_menu(context, name):
    request = context['request']
    current_path = request.path

    try:
        menu = Menu.objects.get(title=name)
        menu_items = menu.items.all()
    except Menu.DoesNotExist:
        return None

    def build_tree(parent=None):
        """Функция для рендеринга древовидной структуры меню"""
        children = menu_items.filter(parent=parent)
        tree = []
        for child in children:
            is_active = False
            if child.url:
                item_url = '/' + child.url.strip('/') + '/'
                is_active = (item_url == current_path)
            child_children = build_tree(parent=child)
            child_active = any(c.get('active') or c.get('expanded') for c in child_children)
            expanded = is_active or child_active
            tree.append({
                'item': child,
                'children': child_children,
                'active': is_active,
                'expanded': expanded,
            })
        return tree
    
    menu_tree = build_tree()
    return {'menu_tree': menu_tree, 'context': context}