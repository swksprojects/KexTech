from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from .models import Course


class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        return qs.filter(owner=self.request)


class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(OwnerEditMixin, self).form_valid(form)


class OwnerCourseMixin(OwnerMixin, LoginRequiredMixin):
    model = Course


class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    fields = ["subject", "title", "slug", "overview"]
    success_url = reverse_lazy("manage_course_list")
    template_name = "course/manage/course/form.html"


class ManageCourseListView(OwnerCourseMixin, ListView):
    template_name = "course/manage/course/list.html"


class CourseCreateView(OwnerCourseEditMixin, CreateView, PermissionRequiredMixin):
    permission_required = "course.add_course"


class CourseUpdateView(OwnerCourseEditMixin, UpdateView, PermissionRequiredMixin):
    permission_required = "course.change_course"


class CourseDeleteView(OwnerCourseMixin, DeleteView, PermissionRequiredMixin):
    permission_required = "course.delete_course"
    success_url = reverse_lazy("manage_course_list")
    template_name = "course/manage/course/delete.html"
    


