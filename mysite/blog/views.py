from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog,BlogType
from django.conf import settings

def get_blog_list_common_data(request,blogs_all_list):
    paginator = Paginator(blogs_all_list, settings.EACH_PAGE_BLOGS_NUMBER)  # 每10页进行分页
    page_num = request.GET.get('page', 1)  # 获取页码参数
    page_of_blogs = paginator.get_page(page_num)
    current_page_num = page_of_blogs.number  # 获取当前页码
    page_range = [x for x in range(current_page_num - 1, current_page_num + 2) if 0 < x <= paginator.num_pages]

    # 加上省略号页码
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)  # append是在末尾插入，insert是在指定位置插入

    context = {}
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    # context['blogs_count'] = Blog.objects.all().count() 得到共有几篇count
    context['blog_types'] = BlogType.objects.all()
    context['blog_dates'] = Blog.objects.dates('created_time', 'month', order='DESC')
    return context

def blog_list(request):
    blogs_all_list = Blog.objects.all()
    context = get_blog_list_common_data(request,blogs_all_list)
    return render_to_response('blog/blog_list.html',context)



def blogs_with_type(request,blog_type_id):
    blog_type = get_object_or_404(BlogType, id=blog_type_id)
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)#具体分类 获取分类的所有文章列表

    context = get_blog_list_common_data(request,blogs_all_list)
    context['blog_type'] = blog_type
    return render_to_response('blog/blog_with_type.html', context)


def blogs_with_date(request,year,month):
    blogs_all_list = Blog.objects.filter(created_time__year=year,created_time__month=month)

    context = get_blog_list_common_data(request,blogs_all_list)
    context['blogs_with_date'] = '%s年%s月' %(year,month)
    return render_to_response('blog/blog_with_date.html', context)




def blog_details(request,blog_id):
    context = {}
    blogs = get_object_or_404(Blog,id=blog_id)
    context['next_blog'] = Blog.objects.filter(created_time__gt=blogs.created_time).first()
    context['previous_blog'] = Blog.objects.filter(created_time__lt=blogs.created_time).last()
    context['blogs'] = blogs
    return render_to_response('blog/blog_detail.html', context)