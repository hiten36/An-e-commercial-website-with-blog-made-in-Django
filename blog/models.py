from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class post(models.Model):
    post_id1=models.AutoField(primary_key=True)
    post1=models.CharField(max_length=20)
    post2=models.CharField(max_length=40,default="")
    post3=models.CharField(max_length=400,default="")
    ts=models.DateTimeField(default=now)
    img=models.ImageField(upload_to='blog/images')

    def __str__(self):
        return self.post2

class blogpost(models.Model):
    post_id=models.AutoField(primary_key=True)
    auth_name=models.CharField(max_length=40,default="")
    post_title=models.CharField(max_length=200)
    post_desc=models.CharField(max_length=2000)
    post_head1=models.CharField(max_length=200)
    post_desc1=models.CharField(max_length=2000)
    post_head2=models.CharField(max_length=200)
    post_desc2=models.CharField(max_length=2000)
    pub_date=models.DateTimeField(default=now)

    def __str__(self):
        return self.post_title

class usercomm(models.Model):
    user_id=models.AutoField(primary_key=True)
    blog_id1=models.IntegerField(default=0)
    user_name=models.ForeignKey(User,on_delete=models.CASCADE)
    desc=models.CharField(max_length=3000,default="")
    ts1=models.DateTimeField(default=now)

    def __str__(self):
        return str(self.user_id)

class userreply(models.Model):
    user_id1=models.AutoField(primary_key=True)
    blog_id2=models.IntegerField(default=0)
    comm_id=models.IntegerField(default=0)
    user_name1=models.ForeignKey(User,on_delete=models.CASCADE)
    desc1=models.CharField(max_length=3000,default="")
    ts2=models.DateTimeField(default=now)

    def __str__(self):
        return self.desc1

class userlike(models.Model):
    like_id=models.AutoField(primary_key=True)
    blog_id3=models.IntegerField(default=0)
    like_comm_id=models.IntegerField(default=0)
    like_user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    like_count=models.IntegerField(default=0)

    def __str__(self):
        return str(self.like_comm_id)

class userlist(models.Model):
    userlist_id=models.AutoField(primary_key=True)
    userlist_blog_id=models.IntegerField(default=0)
    userlist_comm_id=models.IntegerField(default=0)
    userlist_like_id=models.IntegerField(default=0)
    userlist_user=models.CharField(max_length=30)

    def __str__(self):
        return self.userlist_user

class conatct(models.Model):
    con_id=models.AutoField(primary_key=True)
    con_name=models.CharField(max_length=30)
    con_email=models.CharField(max_length=80)
    con_phone=models.CharField(max_length=15)
    con_desc=models.CharField(max_length=800)

    def __str__(self):
        return self.con_name