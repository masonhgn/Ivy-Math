from django.urls import path
from .views import PostListViewAlg
from .views import PostListViewCalc
from .views import PostListViewPrec
from .views import PostListViewTrig

from .views import PostDetailViewAlg, PostDetailViewPrec, PostDetailViewTrig, PostDetailViewCalc
from .views import PostCreateViewAlg, PostCreateViewPrec, PostCreateViewTrig, PostCreateViewCalc
from .views import PostUpdateViewAlg, PostUpdateViewPrec, PostUpdateViewTrig, PostUpdateViewCalc
from .views import PostDeleteViewAlg, PostDeleteViewPrec, PostDeleteViewTrig, PostDeleteViewCalc

from django.http import HttpResponse
from . import views

urlpatterns = [
    #make a home pattern
    path('',views.home,name='boards-home'),
    path('about',views.boardabout,name='boards-about'),


    #posts for each page
    path('alg', PostListViewAlg.as_view(),name='alg'),
    path('trig',PostListViewTrig.as_view(),name='trig'),
    path('prec',PostListViewPrec.as_view(),name='prec'),
    path('calc',PostListViewCalc.as_view(),name='calc'),

    #urls to specific posts
    path('postAlg/<int:pk>/', PostDetailViewAlg.as_view(),name='post-detail-alg'),
    path('postPrec/<int:pk>/', PostDetailViewPrec.as_view(),name='post-detail-prec'),
    path('postTrig/<int:pk>/', PostDetailViewTrig.as_view(),name='post-detail-trig'),
    path('postCalc/<int:pk>/', PostDetailViewCalc.as_view(),name='post-detail-calc'),

    #new post for each category
    path('postCalc/new/', PostCreateViewCalc.as_view(),name='post-create-calc'),
    path('postPrec/new/', PostCreateViewPrec.as_view(),name='post-create-prec'),
    path('postTrig/new/', PostCreateViewTrig.as_view(),name='post-create-trig'),
    path('postAlg/new/', PostCreateViewAlg.as_view(),name='post-create-alg'),

    #update post for each category
    path('postAlg/<int:pk>/update/', PostUpdateViewAlg.as_view(),name='post-update-alg'),
    path('postPrec/<int:pk>/update/', PostUpdateViewPrec.as_view(),name='post-update-prec'),
    path('postTrig/<int:pk>/update/', PostUpdateViewTrig.as_view(),name='post-update-trig'),
    path('postCalc/<int:pk>/update/', PostUpdateViewCalc.as_view(),name='post-update-calc'),


    #delete posts for each category

    path('postAlg/<int:pk>/delete/', PostDeleteViewAlg.as_view(),name='post-delete-alg'),
    path('postPrec/<int:pk>/delete/', PostDeleteViewPrec.as_view(),name='post-delete-prec'),
    path('postTrig/<int:pk>/delete/', PostDeleteViewTrig.as_view(),name='post-delete-trig'),
    path('postCalc/<int:pk>/delete/', PostDeleteViewCalc.as_view(),name='post-delete-calc'),
]