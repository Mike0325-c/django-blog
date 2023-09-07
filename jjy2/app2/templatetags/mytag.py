from django import template
register = template.Library()


# 自定义过滤器
@register.filter(name='hello')
def my_sum(v1, v2):
    return v1+v2


# 自定义标签(可以有多个参数)
@register.simple_tag(name='plus')
def test(a, b, c, d):
    return '%s-%s-%s-%s' % (a, b, c, d)


# 自定义inclusion_tag
@register.inclusion_tag('left_menu.html')
def left(n):
    data = ['第{}项'.format(i) for i in range(n)]
    return locals()  # 将data传递给left_menu.html
    # 第二种
    # return {'data1': data}