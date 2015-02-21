from django import template
from fps_glavni.models import PoliticalParty

register = template.Library()

@register.inclusion_tag('tags/navigation.html')
def main_navigation():
    parties_all = PoliticalParty.objects.all().order_by('name')
    data = { 'parties_all': parties_all}
    return data