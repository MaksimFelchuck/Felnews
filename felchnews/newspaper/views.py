from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from newspaper.forms import NewsForm, ImageForm
from newspaper.models import News, Image


def get_images(images, news_id):
    if len(images) > 1:
        first_image = Image.objects.get(news=news_id, is_main=True)
        images = Image.objects.filter(news=news_id, is_main=False)
    elif len(images) == 0:
        first_image = None
    else:
        first_image = Image.objects.get(news=news_id, is_main=True)
        images = None
    return first_image, images


def index(request):
    return redirect("/news/pages5/")


def main(request, pages=5):

    all_news = News.objects.all()

    images = Image.objects.all()
    paginator = Paginator(all_news, pages)

    page = request.GET.get('page')
    try:
        all_news = paginator.page(page)
    except PageNotAnInteger:
        all_news = paginator.page(1)
    except EmptyPage:
        all_news = paginator.page(paginator.num_pages)
    first_images = Image.objects.filter(is_main=True)
    context = {
        "news": all_news,
        "images": images,
        "first_images": first_images

    }

    return render(request, "news.html", context)


def news(request, news):
    news_id = News.objects.get(id=news)
    images = Image.objects.filter(news=news_id)
    first_image, images = get_images(images, news_id)
    context = {
        "news": news_id,
        "images": images,
        "first_image": first_image
    }
    return render(request, "news_id.html", context)


def write_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST or None)
        if form.is_valid():
            head = form.cleaned_data.get("head")
            text = form.cleaned_data.get("text")
            new_news = News(head=head, text=text)
            new_news.save()
            return redirect(f"/{new_news.id}/load_image/")
    form = NewsForm()
    context = {
        "form": form
    }
    return render(request, "write_form.html", context)


def load_image(request, news):
    news = News.objects.get(id=news)

    images = Image.objects.filter(news=news)

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            upload_image = form.cleaned_data.get("image")
            new = True
            for image in Image.objects.all():
                if image.news == news:
                    new = False
                    break
            image = Image(image=upload_image, news=news, is_main=new)
            image.save()
            return redirect(f"/{news.id}/load_image/")

    form = ImageForm
    context = {
        "form": form,
        "images": images,
    }
    return render(request, "load_image.html", context)
