from django.urls import path

from .views import (
    AddOrderToUserView,
    AddUserPhotoView,
    ChangeEmployeeServiceView,
    ChangeUserServiceView,
    DeleteUserView,
    GetSelfUserView,
    ListUserOrdersView,
    ProfileUpdateView,
    RetrieveDestroyUserView,
    ToAdminView,
    ToEmployeeView,
    ToUserView,
    UserActivateView,
    UserDeactivateView,
    UserListCreateView,
)

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('/orders', ListUserOrdersView.as_view()),
    path('/self', GetSelfUserView.as_view()),
    path('/change_service/<int:pk>', ChangeUserServiceView.as_view()),
    path('/<int:user>/change_employee_service/<int:service>', ChangeEmployeeServiceView.as_view()),
    path('/<int:pk>/activate', UserActivateView.as_view()),
    path('/<int:pk>/deactivate', UserDeactivateView.as_view()),
    path('/<int:pk>/to_admin', ToAdminView.as_view()),
    path('/<int:pk>/to_user', ToUserView.as_view()),
    path('/<int:pk>/to_employee', ToEmployeeView.as_view()),
    path('/new_order', AddOrderToUserView.as_view()),
    path('/profile_update', ProfileUpdateView.as_view()),
    path('/<int:pk>', RetrieveDestroyUserView.as_view()),
    path('/add_photo', AddUserPhotoView.as_view()),
    path('/<int:pk>/delete', DeleteUserView.as_view()),

]