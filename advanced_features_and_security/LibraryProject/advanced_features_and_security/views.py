from django.shortcuts import render

# Create your views here.
# advanced_features_and_security/views.py

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .models import Article


@permission_required('advanced_features_and_security.can_view', raise_exception=True)
def view_articles(request):
    articles = Article.objects.all()
    return render(request, "articles/list.html", {"articles": articles})


@permission_required('advanced_features_and_security.can_create', raise_exception=True)
def create_article(request):
    return HttpResponse("You can create an article.")


@permission_required('advanced_features_and_security.can_edit', raise_exception=True)
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return HttpResponse(f"You can edit the article: {article.title}")


@permission_required('advanced_features_and_security.can_delete', raise_exception=True)
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return HttpResponse(f"You can delete: {article.title}")
