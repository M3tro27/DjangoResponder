from django.contrib import admin
from django.urls import path

from . import views

# List of URIs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # Members
    path('member/list', views.MemberListView.as_view(), name='member_list'),
    path('member/create', views.MemberCreateView.as_view(), name='membercreate'),
    path('member/update/<pk>', views.MemberUpdateView.as_view(), name='memberupdate'),
    path('member/delete/<pk>', views.MemberDeleteView.as_view(), name='memberdelete'),
    # Unit
    path('unit/detail', views.UnitDetailView.as_view(), name='unitdetail'),
    path('unit/create', views.UnitCreateView.as_view(), name='unitcreate'),
    path('unit/update/<pk>', views.UnitUpdateView.as_view(), name='unit_update'),
    path('unit/delete/<pk>', views.UnitDeleteView.as_view(), name='unit_delete'),
    # Machinery
    path('machinery/list', views.MachineryListView.as_view(), name='machinery_list'),
    path('machinery/create', views.MachineryCreateView.as_view(), name='machinery_create'),
    path('machinery/update/<pk>', views.MachineryUpdateView.as_view(), name='machinery_update'),
    path('machinery/delete/<pk>', views.MachineryDeleteView.as_view(), name='machinery_delete'),
    # Equipment
    path('equipment/list', views.EquipmentListView.as_view(), name='equipment_list'),
    path('equipment/create', views.EquipmentCreateView.as_view(), name='equipment_create'),
    path('equipment/update/<pk>', views.EquipmentUpdateView.as_view(), name='equipment_update'),
    path('equipment/delete/<pk>', views.EquipmentDeleteView.as_view(), name='equipment_delete'),
    # Call
    path('call/list', views.CallListView.as_view(), name='call_list'),
    path('call/create', views.CallCreateView.as_view(), name='call_create'),
    path('call/update/<pk>', views.CallUpdateView.as_view(), name='call_update'),
    path('call/delete/<pk>', views.CallDeleteView.as_view(), name='call_delete'),
    # Call initialization
    path('call-initialization/', views.receive_call_initialization, name='call_initialization'),
]
