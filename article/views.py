from django.shortcuts import render
from .models import ArticleObj
from django.shortcuts import render, get_object_or_404

# Create your views here.
def article_list(request):
    articles = ArticleObj.objects.filter(publication_date__isnull=False).order_by('publication_date')
    return render(request, 'article/article_list.html', {'articles':articles})

def article_detail(request, pk):
    article = get_object_or_404(ArticleObj, pk=pk)
    return render(request, 'article/article_detail.html',{'article':article})