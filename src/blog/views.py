from django.shortcuts import render

# Create your views here.
def index(request):
    posts=[
    {
    "title":"first post",
    "author":"yousef",
    "post_date":"1/5/2020",
    "content":"this is the first post"
    },
    {
    "title":"second post",
    "author":"nawar",
    "post_date":"10/5/2020",
    "content":"this is the second post"
    }
    ]
    context={"posts":posts}
    return render(request,"blog/index.html",context)
def about(request):
    pass
