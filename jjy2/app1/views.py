from django.shortcuts import render, HttpResponse, redirect, reverse
from app1 import models
from django.http import JsonResponse
import json
from django.views import View


def indexjson(request):
    user_dict = {'username': 'wuluo你好', 'age': 18, 'password': '123'}
    list1 = [11, 22, 33, 44]
    # 先转换json格式的字符串
    # 如果字符串里面有中文会报错,将ensure_ascii参数的值设置为False
    json_str = json.dumps(user_dict, ensure_ascii=False)
    return HttpResponse(json_str)
    # return HttpResponse(json_str)
    # return JsonResponse(user_dict, json_dumps_params={'ensure_ascii': False})
    # return JsonResponse(list1, safe=False)


def file(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        file_obj = request.FILES.get('file')
        print(file_obj.name)
        # with open(file_obj.name, 'wb') as f:
        #     for line in file_obj:
        #         f.write(line)

    print(request.path)
    print(request.path_info)
    print(request.get_full_path())
    return render(request, 'form.html')


class Login6(View):
    def get(self, request):
        return render(request, 'form.html')

    def post(self, request):
        return HttpResponse('post方法')


def test6(request):
    n = 123
    f = 11.11
    s = 'hello world'
    b = True
    list1 = ['a', 'b', 'c']
    tuple1 = (111, 222, 333, 444)
    dict1 = {'username': 'wuluo', 'age': 18, 'hobby': ['sing', 'dance', {'info': 'test'}]}
    set1 = {'jjh', 'xxx', 'bbb'}

    def func():
        return '你好'

    def func_none():
        pass

    class Myclass():
        def get_self(self):
            return 'self'

        @staticmethod
        def get_func():
            return 'func'

        @classmethod
        def get_class(cls):
            return 'cls'

    obj = Myclass()
    return render(request, 'test.html', locals())





def home(request):
    print(reverse('ooo', args=(1, 2)))
    print(reverse('xxx', kwargs={'year': 1234, 'month': 22}))
    # print(reverse('ooo', args=(1, )))
    return render(request, 'home.html')


def test(request, year1, q):
    print(year1, q)
    return HttpResponse('testadd')


#
# def testadd(request, year):
#     print(year)
#     return HttpResponse('testadd')

def testadd(request, year, month):
    print(year, month)
    return HttpResponse('testadd')


# Create your views here.
def index(request):
    # return render(request,'jjy.html')
    # return redirect('https://www.baidu.com/')
    return redirect('/home/')


# def home(request,xxx,d):
#     print(xxx)
#     print(d)
#     return HttpResponse('home')


def login(request):
    print('jjy is logining')
    print(request)
    print(request.method, ':request method')
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        print(request.POST, "post method")
        print(request.POST.get('hobby'))
        print(request.POST.getlist('hobby'))
        print(request.POST.getlist('hobby')[0])
        username = request.POST.get('username')
        password = int(request.POST.get('password'))
        # res 是一个列表
        res = models.User.objects.filter(username=username).first()
        res = models.User.objects.create
        print(res, "    date from database ")
        if password == res.password:
            return HttpResponse('登录成功')
        return HttpResponse('密码错误')
        # res1 = models.User.objects
        # print(res1)
        # print(res)
        # print(res.password)
        # print(res.password)
    # return HttpResponse('提交成功')


def regist(request):
    if request.method == 'POST':
        username = request.POST.get('username1')
        password = request.POST.get('password')
        data = models.User.objects.create(username=username, password=password)
        print(data, data.username, data.password)
        return HttpResponse('注册成功')
    return render(request, 'regist.html')


def userlist(request):
    data = models.User.objects.all()
    print(data)
    # return render(request,'userlist.html',{"data":data})
    return render(request, 'userlist.html', locals())


def edit(request):
    # 获取url问号后面的参数
    print(request.GET, "    edit data")
    edit_id = request.GET.get('user_id')
    print(edit_id)
    print(request.GET)
    # 查询当前用户想要编辑的数据对象
    edit_obj = models.User.objects.filter(id=edit_id).first()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password, "  new edit")
        hobby = request.POST.get('hobby')
        info = request.POST.get('info')
        # 修改方式一:将filter查询出来的列表中的所有对象全部更新
        # models.User.objects.filter(id=edit_id).update(username=username, hobby=hobby, info=info)
        # 修改方式二:首先拿到需要修改的数据,然后再通过对象名.属性的方式进行赋值
        edit_obj.username = username
        edit_obj.password = password
        edit_obj.hobby = hobby
        edit_obj.info = info
        edit_obj.save()
        return redirect('/userlist/')
    return render(request, 'edit.html', locals())


def delete(request):
    # 获取用户想要删除的数据id
    delete_id = request.GET.get('user_id')
    # 直接去数据库中找到对应的数据删除即可
    # models.User.objects.filter(id=delete_id).first().delete()
    models.User.objects.filter(id=delete_id).delete()
    # 批量删除,将filter拿到的所有对象全部删除
    return redirect('/userlist/')
