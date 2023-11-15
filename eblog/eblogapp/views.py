from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Post, Category
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'index.html'

class PostList(generic.ListView):
    template_name = 'index.html'

    def get_queryset(self):
        queryset = Post.objects.filter(status=1).order_by('-created_on')
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(categories=category)
        return queryset
    

def CategoriesView(request):
    categories = Category.objects.all()  # Query all categories from the database
    context = {
        'categories': categories,  # Pass the categories queryset to the template
    }
    return render(request, 'categories.html', context)

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'post_detail.html', {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})







