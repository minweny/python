from django.shortcuts import render

posts = []

authorDic = {}

for i in range(20):
    authorDic = authorDic.copy()
    authorDic['author'] = 'author' + str(i)
    authorDic['title'] = 'title' + str(i)
    posts += [authorDic]

# Create your views here.
def home(request):
    return render(request, 'blog/home.html', {'posts':posts, 'title': 'title'})

def about(request):
    return render(request, 'blog/about.html')