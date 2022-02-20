from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now

CATEGORY_CHOICES = (
    ("1", "I do not know now"),
    ("2", "Φυσική Καταστροφή - πλημμύρες"),
    ("3", "Φυσική Καταστροφή - φωτιές"),
    ("4", "Φυσική Καταστροφή - σεισμός"),
    ("5", "Φυσική Καταστροφή - Καταστροφή Δημόσιας Περιουσίας"),
    ("6", "Φυσική Καταστροφή - Ρύπανση"),
    ("7", "Δολιοφθορές - Ρύπανση"),
    ("8", "Δολιοφθορές - Καταστροφή Δημόσιας Περιουσίας"),
    ("9", "Δολιοφθορές - Ξυλοδαρμός"),
    ("10", "Δολιοφθορές - Κλοπή"),
)
 
DHMOS_CHOISES = (
    ("1", "Παράδειγμα Δήμου1"),
    ("2", "Παράδειγμα Δήμου2"),
    ("3", "Παράδειγμα Δήμου3"),
    ("4", "Παράδειγμα Δήμου4"),
    ("5", "Παράδειγμα Δήμου5"),
    ("6", "Παράδειγμα Δήμου6"),
    ("7", "Παράδειγμα Δήμου7"),
    ("8", "Παράδειγμα Δήμου8"),
    ("9", "Παράδειγμα Δήμου9"),
    ("10", "Παράδειγμα Δήμου10"),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone_no = models.IntegerField(blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)
    
    def __str__(self):
        return str(self.user)

class BlogPost(models.Model):
    title=models.CharField(max_length=255)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    #slug=models.CharField(max_length=130)
    content=models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Δεν γνωρίζω')
    dhmos = models.CharField(max_length=50, choices=DHMOS_CHOISES, default='Παράδειγμα Δήμου1')
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    location = models.CharField(max_length=255, default="None")
    dateTime=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.author) +  " Blog Title: " + self.title
    
    def get_absolute_url(self):
        return reverse('blogs')
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)   
    dateTime=models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username +  " Comment: " + self.content
    

