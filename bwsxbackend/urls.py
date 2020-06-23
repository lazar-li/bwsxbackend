from django.urls import path,include
import xadmin
from django.views.static import serve
from bwsxbackend.settings import MEDIA_ROOT

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/',include('extra_apps.DjangoUeditor.urls' )),
    #文件
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
]