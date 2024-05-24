from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.contrib.postgres.fields import ArrayField

QUESTION_TOPICS=(
        ('Array', 'Array'),
        ('String', 'String'),
        ('Linked List', 'Linked List'),
        ('Stack', 'Stack'),
        ('Queue', 'Queue'),
        ('Binary Tree', 'Binary Tree'),
        ('Binary Search Tree', 'Binary Search Tree'),
        ('Heap', 'Heap'),
        ('Graph', 'Graph'),
        ('Greedy', 'Greedy'),
        ('Backtracking', 'Backtracking'),
        ('Dynamic Programming', 'Dynamic Programming'),
        ('Bit Manipulation', 'Bit Manipulation'),
        ('Trie', 'Trie'),
        ('Hashing', 'Hashing'),
        ('Matrix', 'Matrix'),
        ('Searching', 'Searching'),
        ('Sorting', 'Sorting'),
        ('Recursion', 'Recursion'),
        ('Randomized', 'Randomized'),
        ('Divide and Conquer', 'Divide and Conquer'),
        ('Game Theory', 'Game Theory'),
        ('Branch and Bound', 'Branch and Bound'),
        ('Geometry', 'Geometry'),
        ('Mathematical', 'Mathematical'),
        ('Combinatorics', 'Combinatorics'),
        ('Bit Magic', 'Bit Magic'),
        ('All', 'All')
    )

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("First Name"), max_length=100)
    last_name = models.CharField(_("Last Name"), max_length=100)
    email = models.EmailField(_("Email Address"), max_length=254, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined =  models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.email
    
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    

class Question(models.Model):
    question_title = models.CharField(max_length=100)
    question_link = models.CharField(max_length=255)
    question_created = models.DateTimeField(auto_now_add=True)
    question_updated = models.DateTimeField(auto_now=True)
    question_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions_author', null=True, blank=True)
    question_description = models.TextField(null=True, blank=True,default='')
    
    question_type = models.CharField(choices=(
        ('Contest Question', 'Contest Question'),
        ('General Practice', 'General Practice'),
        ('Daily Challenge', 'Daily Challenge'),
        ('Interview Question', 'Interview Question')
    ), max_length=100)
    question_status = models.CharField(choices=(
        ('Weak', 'Weak'),
        ('Average', 'Average'),
        ('Strong', 'Strong'),
        ('Very Strong', 'Very Strong')
    ), max_length=100)
   
   

    question_topics = ArrayField(
        models.CharField(
            max_length=100,
            choices=QUESTION_TOPICS
        ),
        size=10,
        default=list,
    )





class Solution(models.Model):
    solution_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    solution_approach=models.TextField()
    
    solution_time_complexity=models.CharField(max_length=255)
    solution_space_complexity=models.CharField(max_length=255)
    solution_type=models.CharField(max_length=255,choices=(
        ('Brute','Brute'),
        ('Optimized','Optimized'),
        ('Best','Best')
    
    ))

    
    
    

    CODE_LANGUAGES = (
       ('C', 'C'),
        ('C++', 'C++'),
        ('Java', 'Java'),
        ('Python', 'Python'),
        ('JavaScript', 'JavaScript'),
        ('Ruby', 'Ruby'),
        ('Go', 'Go'),
        ('Scala', 'Scala'),
        ('Kotlin', 'Kotlin'),
        ('Swift', 'Swift'),
        ('Rust', 'Rust'),
        ('PHP', 'PHP'),
        ('TypeScript', 'TypeScript'),
        ('C#', 'C#'),
        ('R', 'R'),
        ('Objective-C', 'Objective-C'),
        ('Perl', 'Perl'),
        ('Haskell', 'Haskell'),
        ('Lua', 'Lua'),
        ('HTML/CSS', 'HTML/CSS'),
        ('SQL', 'SQL'),
        ('Bash/Shell', 'Bash/Shell'),
        ('Matlab', 'Matlab'),
        ('Dart', 'Dart'),
        ('Groovy', 'Groovy'),
        ('Assembly', 'Assembly'),
        ('Visual Basic', 'Visual Basic'),
        ('Delphi/Object Pascal', 'Delphi/Object Pascal'),
        ('PL/SQL', 'PL/SQL'),
        ('Objective-C++', 'Objective-C++'),
        ('Scratch', 'Scratch'),
        ('RPG', 'RPG'),
        ('COBOL', 'COBOL'),
        ('Fortran', 'Fortran'),
        ('Julia', 'Julia'),
        ('Ada', 'Ada'),
        ('Lisp', 'Lisp'),
        ('Prolog', 'Prolog'),
        ('Scheme', 'Scheme'),
        ('F#', 'F#'),
        ('ABAP', 'ABAP'),
        ('ActionScript', 'ActionScript'),
        ('Apex', 'Apex'),
        ('AutoLISP', 'AutoLISP'),
        ('AutoIt', 'AutoIt'),
        ('Awk', 'Awk'),
        ('Ceylon', 'Ceylon'),
        ('CFML', 'CFML'),
        ('Clojure', 'Clojure'),
        ('Common Lisp', 'Common Lisp'),
        ('Crystal', 'Crystal'),
        ('D', 'D'),
        ('Elixir', 'Elixir'),
        ('Erlang', 'Erlang'),
        ('Forth', 'Forth'),
        ('Hack', 'Hack'),
        ('Haxe', 'Haxe'),
        ('Icon', 'Icon'),
        # Add more languages as needed
    )

   

    code_snippets=models.JSONField(default=dict)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def save_code_snippet(self, language, code):
        # Check if the specified language is one of the allowed choices
        if language in dict(self.CODE_LANGUAGES).keys():
            self.code_snippets[language] = code
            self.save()

    



       
    
    
    
   


class Post(models.Model):
    POST_TYPES = [
        ('Interview Experience', 'Interview Experience'),
        ('Technical Discussion', 'Technical Discussion'),
        ('Project Showcase', 'Project Showcase'),
        ('General Advice', 'General Advice'),
        ('Event Announcement', 'Event Announcement'),
       
    ]

    post_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    post_title = models.CharField(max_length=255)
    post_content = models.TextField()
    post_images = models.TextField(null=True, blank=True,max_length=20000)
    post_type = models.CharField(choices=POST_TYPES, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_title
    
    @property
    def get_post_by_id(id):
        return Post.objects.get(id=id)
    
    def get_post_by_author_id(id):
        return Post.objects.filter(post_author=id)

class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} liked {self.post.post_title}"
    @property
    def is_post_liked_by_me(self, user):
        return PostLike.objects.filter(post=self.post, user=user).exists()
    
   

class PostDislike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='dislikes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name+self.user.last_name} disliked {self.post.post_title}"
    
    def is_post_disliked_by_me(self, user):
        return PostDislike.objects.filter(post=self.post, user=user).exists()
    
class Comment(models.Model):
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    comment_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

    
class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} liked {self.comment.comment_content}"
    @property
    def is_comment_liked_by_me(self, user):
        return CommentLike.objects.filter(comment=self.comment, user=user).exists()

class CommentDislike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='dislikes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name+self.user.last_name} disliked {self.comment.comment_content}"
    @property
    def is_comment_disliked_by_me(self, user):
        return CommentDislike.objects.filter(comment=self.comment, user=user).exists()






