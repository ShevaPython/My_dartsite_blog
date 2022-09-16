from django import template
from blog.models import Post, Tag

register = template.Library()


@register.inclusion_tag('blog/popular_posts_tpl.html')
def get_popular_post(cnt=3):
    posts = Post.objects.order_by('-view')[:cnt]
    return {'posts': posts, 'cnt': cnt}


@register.inclusion_tag('blog/popular_tags_posts_tpl.html')
def get_popular_tags():
    tags = Tag.objects.all()
    return {'tags': tags}
