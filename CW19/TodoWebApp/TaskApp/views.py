from django.shortcuts import render, redirect
from django.views import View
from .models import Task, Tag, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .mixin import TodoOwnerRequiredMixin as TORM, AllTodoOwnerRequiredMixin as ATORM


# Create your views here.
class AllTask(ATORM, View):
    def get(self, request):
        all_task = self.Tasks
        pg = Paginator(all_task, 5)
        page_number = request.GET.get('page')
        try:
            page_obj = pg.get_page(page_number)
        except PageNotAnInteger:
            page_obj = pg.page(1)
        except EmptyPage:
            page_obj = pg.page(pg.num_pages)

        return render(request, 'task/task.html', context={'page_obj': page_obj})


class TaskDetail(TORM, View):
    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        return render(request, 'task/task.html', {'single_task': task})


class NewTask(View):
    def post(self, request):
        if request.method == "POST":
            title = request.POST.get('title')
            category = request.POST.get('category')
            description = request.POST.get('description')
            due_date = request.POST.get('due_date')
            status = request.POST.get('status')
            tag = request.POST.getlist('tag')
            author = request.user
            # Create the task object
            task = Task.objects.create(
                title=title,
                category=Category.objects.get(id=category),
                description=description,
                due_date=due_date,
                status=status,
                author=author
            )
            print(tag)
            for each_tag in tag:
                tag_obj = Tag.objects.get(id=each_tag)
                task.tag.add(tag_obj)
            task.save()
            return redirect("/")