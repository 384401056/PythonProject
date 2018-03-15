from django.shortcuts import render
import time
# Create your views here.


from django.views.decorators.cache import cache_page

"""缓存使用的方式，在settings文件中设置"""
#方式一：
@cache_page(10) # 使用页面缓存 10为缓存时间，单位是秒
def index(request):
    # 此页面中的时间，在10秒后才会刷新，现实了页面的缓存。
    return render(request, 'Cache/index.html',{'time': time.time()})

# 方式二：直接在配置URL的地方，进行缓存的设置。
# from django.views.decorators.cache import cache_page
#
# urlpatterns = [
#     url(r'^foo/([0-9]{1,2})/$', cache_page(60 * 15)(my_view)),# 对于匹配的正则，不同的url会单独进行缓存。
# ]

# 模版局部缓存
def index2(request):
    return render(request, 'Cache/index2.html', {'time1': time.time(),'time2':time.time()})