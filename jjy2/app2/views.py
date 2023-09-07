from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('app2')


import datetime
from django.utils.safestring import mark_safe
def test(request):
    h = '<h1>hahaha</h1>'
    res = mark_safe(h)
    n = 123
    f = 11.11
    s = 'hello world'
    b = False
    c = True
    lll = []
    list1 = ['a', 'b', 'c', 'd']
    tuple1 = (111, 222, 333, 444)
    dict1 = {'username': 'wuluo', 'age': 18, 'hobby': ['sing', 'dance', {'info': 'test'}]}
    set1 = {'jjh', 'xxx', 'bbb'}
    file_size = 1231231
    current_time = datetime.datetime.now()
    info = '据央视新闻，9月16日下午，位于湖南长沙市区内的中国电信大楼发生火灾，现场浓烟滚滚，数十层楼体燃烧剧烈。消防救援人员赶到现场后很快将火势控制，目前大楼明火已被扑灭。据了解，事发电信大楼2000年建成，位于长沙市东二环，曾以218米的高度成为长沙首座突破200米的楼宇。具体火灾伤亡情况正在进一步了解中。'
    eng = 'According to CCTV news, on the afternoon of September 16, a fire broke out in the China Telecom Building in Changsha, Hunan Province, with smoke billowing and dozens of floors burning violently. The fire rescuers soon controlled the fire after arriving at the scene. At present, the open fire of the building has been put out. It is understood that the incident telecommunications building was completed in 2000 and located in the East Second Ring Road of Changsha. It was the first building in Changsha to break through 200 meters with a height of 218 meters. The specific fire casualties are being further understood.'

    def func():
        return '你好'

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

def home1(request):
    return render(request, 'homeedit.html')


def login(request):
    return render(request, 'loginedit.html')


def register(request):
    return render(request, 'registeredit.html')
    # return HttpResponse("fefefe")



