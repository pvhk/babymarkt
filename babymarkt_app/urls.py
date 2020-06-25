from django.urls import path
from .views import ads
from .views import categories
from .views import home
from .views import users

urlpatterns =  [
    path("", home.index, name="home"),
    path("ads/", ads.index, name="index_ads"),
    path("ads/<int:ad_id>/", ads.detail, name="detail_ad"),
    path("ads/<int:ad_id>/edit", ads.edit, name="edit_ad"),
    path("ads/<int:ad_id>/delete", ads.delete, name="delete_ad"),
    path("ads/new/", ads.new, name="new_ad"),
    path("ads/search/", ads.search, name="search_ad"),
    path('accounts/login/', users.login_user, name="login"),
    path("accounts/register/", users.register, name="register"),
    path("accounts/logout/", users.logout_user, name="logout"),
    path("categories/<str:category_name>/", categories.list_ads, name="category_list_ads"),
    path("accounts/me/", users.show_me, name="user_profile"),
    path("accounts/myads", users.show_my_ads, name="user_ads")
]