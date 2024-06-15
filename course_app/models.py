from django.db import models
from category.models import Menu
from credentials.models import Interest

# Create your models here.
# Model(offline/online/Hybrid)
class Mode(models.Model):
    type=models.CharField(max_length=20)

    def __str__(self):
        return self.type

# Model for storing Languages
class Language(models.Model):
    lang_name=models.CharField(max_length=20)

# Model for storing Locations
class Location(models.Model):
    location_name=models.CharField(max_length=20)

    def __str__(self):
        return self.location_name


# table for authors
class Authors(models.Model):
    author_name=models.CharField(max_length=20,default=None)
    author_img = models.ImageField(upload_to='authors_img',default=None)
    def __str__(self):
        return self.author_name


# table for collaborators
class Collaborators(models.Model):
    collab_name=models.CharField(max_length=20,default=None)
    collab_img = models.ImageField(upload_to='collab_img',default=None)
# Model for producers
class Producers(models.Model):
    producer_name=models.CharField(max_length=20,default=None)
    producer_img = models.ImageField(upload_to='producers_img',default=None)
    def __str__(self):
        return self.producer_name
# Model for educators
class Educators(models.Model):
    educator_name=models.CharField(max_length=20,default=None)
    educator_img = models.ImageField(upload_to='educators_img',default=None)
# Model for storing on-demand or live
class Stage(models.Model):
    stage_name=models.CharField(max_length=20,default=None)

    def __str__(self):
        return self.stage_name
# Model for storing sponsors
class Sponsors(models.Model):
    sponsor_name=models.CharField(max_length=20)
    sponsor_img=models.ImageField(upload_to='sponsors_img',default=None)

# Model for storing secctors
class Sectors(models.Model):
    sector_name=models.CharField(max_length=20,default=None)
    def __str__(self):
        return self.sector_name
class Topic(models.Model):
    name = models.CharField(max_length=100)
    parent_topics = models.ManyToManyField('self', blank=True, related_name='subtopics')
    def __str__(self):
        return self.name

# table to store course_details

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_description = models.TextField()
    course_date = models.DateField()
    course_price = models.IntegerField()
    course_learning_credits = models.IntegerField()
    course_lifetime_learners = models.IntegerField(default=None)
    course_rating = models.FloatField()
    course_num_ratings = models.IntegerField()
    course_first_published = models.DateField()
    course_times_launched = models.IntegerField()
    course_num_interested = models.IntegerField()
    course_num_hours = models.IntegerField()
    course_num_days = models.IntegerField()
    course_skills=models.CharField(max_length=200,default=None)
    more_about_course = models.TextField(default=None)
    course_relevance_of_program = models.TextField(default=None)
    course_recommended_learners = models.TextField(default=None)
    course_what_will_learn = models.TextField(default=None)
    course_img=models.ImageField(upload_to='course_pics',blank=True)
    course_time=models.TimeField(default=None)

    # Foreign keys and Many to Many fields
    course_medium_of_communication = models.ForeignKey(Language,on_delete=models.CASCADE)
    course_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    course_authors=models.ManyToManyField(Authors,related_name='courses',default=None)
    course_collab=models.ManyToManyField(Collaborators,related_name='courses',default=None)
    course_mode=models.ForeignKey(Mode,on_delete=models.CASCADE,default=None)
    course_producers=models.ManyToManyField(Producers,related_name='courses',default=None)
    course_sponsors=models.ManyToManyField(Sponsors,related_name='courses',default=None)
    course_interest=models.ManyToManyField(Interest,related_name='courses',default=None)
    course_stage=models.ForeignKey(Stage,on_delete=models.CASCADE,default=None)
    topics = models.ManyToManyField(Topic, related_name='courses')
    #newly added
    course_educators=models.ManyToManyField(Educators, related_name='current_educators', default=None, blank=True)
    course_past_educators=models.ManyToManyField(Educators, related_name='past_educators', default=None, blank=True)



    def __str__(self):
        return self.course_name
    