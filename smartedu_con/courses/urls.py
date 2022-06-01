from django.urls import path
from . import views


urlpatterns = [
    path("", views.courses_list, name="courses"),
    path("<slug:category_slug>/<int:course_id>",
         views.course_detail, name="course_detail"),
    #     path("categories/<slug:category_slug>",
    #          views.category_list, name="courses_by_category"),
    path("categories/<slug:category_slug>",
         views.courses_list, name="courses_by_category"),

    #     path("tags/<slug:tag_slug>", views.tags_list, name="courses_by_tag"),
    path("tags/<slug:tag_slug>", views.courses_list, name="courses_by_tag"),
    path("search/", views.search, name="search"),
]
