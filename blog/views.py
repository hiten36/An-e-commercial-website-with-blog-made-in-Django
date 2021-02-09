from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import blogpost,post,usercomm,userreply,userlike,userlist,conatct
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def index(request):
    posts=post.objects.all()
    n=len(posts)
    params={'posts':posts,'n':n}
    return render(request,'blog/index.html',params)

def about(request):
    return render(request,'blog/about.html')

def contact1(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contacts=contact(con_name=name,con_email=email,con_phone=phone,con_desc=desc)
        contacts.save()
        messages.success(request,"Your feedback has been submitted.We'll get back to you ASAP!")

    return render(request,'blog/contact.html')

def blogpost1(request,myid):
    blogs=blogpost.objects.filter(post_id=myid)[0]
    n=len(blogpost.objects.all())
    allcomm=usercomm.objects.all()
    replys=userreply.objects.all()
    likes=userlike.objects.all()
    userlists=userlist.objects.all()
    if request.method=='POST':
        like1=request.POST.get('like1','')
        comm1=request.POST.get('comm_id','')
        userlike.objects.filter(like_comm_id=comm1).delete()
        user1=request.user
        likes1=userlike(blog_id3=blogs.post_id,like_comm_id=comm1,like_user_id=user1,like_count=like1)
        likes1.save()
        likes2=int(request.POST.get('likes21',''))+1
        print(likes2)
        userlists1=userlist(userlist_blog_id=blogs.post_id,userlist_comm_id=comm1,userlist_like_id=likes2,userlist_user=user1)
        userlists1.save()
    return render(request,'blog/blogpost.html',{'blogs':blogs,'length':n,'comm':allcomm,'reps':replys,'likes':likes,'userlists1':userlists})

def blogpost2(request,myid):
    blogs=blogpost.objects.filter(post_id=myid)[0]
    n=len(blogpost.objects.all())
    allcomm=usercomm.objects.all()
    replys=userreply.objects.all()
    likes=userlike.objects.all()
    if request.method=='POST':
        messages.success(request,"Your comment has been posted successfully")
        comm1=request.POST.get('comm1','')
        user1=request.user
        comment=usercomm(blog_id1=blogs.post_id,user_name=user1,desc=comm1)
        comment.save()
        last_id=usercomm.objects.last()
        with open('temp.txt','w') as f:
            f.write(str(last_id))
            f.close()
        with open('temp.txt') as f:
            last_id1=f.read()
            f.close()
        likes1=userlike(blog_id3=blogs.post_id,like_comm_id=last_id1,like_count=0)
        likes1.save()
    return redirect(f'/blog/blogpost/{myid}')

def blogpost3(request,myid):
    blogs=blogpost.objects.filter(post_id=myid)[0]
    n=len(blogpost.objects.all())
    allcomm=usercomm.objects.all()
    replys=userreply.objects.all()
    likes=userlike.objects.all()
    if request.method=='POST':
        comm2=request.POST.get('comm2','')
        user1=request.user
        comm_id2=request.POST.get('hcomm_id','')
        reply=userreply(blog_id2=blogs.post_id,user_name1=user1,desc1=comm2,comm_id=comm_id2)
        reply.save()
        messages.success(request,"Your reply has been posted successfully")
    return redirect(f'/blog/blogpost/{myid}')

def search(request):
    query=request.GET.get('query')
    posts1=post.objects.filter(post1__icontains=query)
    posts2=post.objects.filter(post2__icontains=query)
    posts3=post.objects.filter(post3__icontains=query)
    posts1=posts1.union(posts2,posts3)
    params={'posts':posts1,'query':query}
    return render(request,'blog/search.html',params)

def handlesignin(request):
    if request.method=='POST':
        user1=request.POST.get('user1')
        pass1=request.POST.get('pass1')
        cpass1=request.POST.get('cpass1')
        if pass1!=cpass1:
            messages.error(request,'Please recheck your password and try again')
            return redirect('/blog')
        if len(user1) <3:
            messages.error(request,'Username is too short.Try another username')
            return redirect('/blog')
        if len(user1) >16:
            messages.error(request,'Username is too big.Try another username')
            return redirect('/blog')
        if not user1.isalnum():
            messages.error(request,'Invalid Username type! Username must only contains alphabets and numbers.')
            return redirect('/blog')
        if not User.objects.filter(username=user1).exists():
            users=User.objects.create_user(user1,'',pass1)
            users.save()
            messages.success(request,'Your account has been created successfully.You can now Login')
            return redirect('/blog')
        else:
            messages.error(request,"Username already exists! Please try another Username")
            return redirect('/blog')
    else:
        return HttpResponse("Error - 404. Not found")

def handlelogin(request):
    if request.method=='POST':
        user2=request.POST.get('user2')
        pass2=request.POST.get('pass2')
        users=authenticate(username=user2,password=pass2)
        if users is not None:
            login(request,users)
            messages.success(request,'You have been logged in successfully!')
            return redirect('/blog')
        else:
            messages.error(request,'Invalid credentials! Please try again.')
            return redirect('/blog')
    else:
        return HttpResponse("Error - 404. Not found")

def handlelogout(request):
    logout(request)
    messages.success(request,'you have been logged out successfully!')
    return redirect('/blog')
