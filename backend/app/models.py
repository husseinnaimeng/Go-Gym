from django.db import models
from django.contrib.auth import get_user_model

default_title = 'بلا عنوان'


User = get_user_model()


class Workout(models.Model):
    ''' A single workout object (pre-made) to use in workout item to avoid repeating the same exercise for each member workout plan  '''    
    title = models.CharField(max_length=150)
    desc  = models.TextField(max_length=4000)
    image = models.ImageField(upload_to='workout-media/images')
    media = models.FileField(upload_to='workout-media/videos')
    
    def __str__(self):
        
        return self.title if self.title else default_title


class WorkOutItem(models.Model):

    ''' Used in workout plan as an exercise  with different sets and reps for each member  '''
    
    workout     = models.ForeignKey(Workout,on_delete=models.SET_NULL,null=True)
    sets        = models.IntegerField(default=3)
    reps        = models.IntegerField(default=10)

    def __str__(self):
        
        return self.workout if self.workout else default_title
    

class WorkoutPlan(models.Model):
    ''' Full workout-plan with all the exercises that the trainer or the coach has assigned to the member  '''
    member = models.ForeignKey("members.Member",on_delete=models.CASCADE,related_name='member_workout_plan')
    exercises = models.ManyToManyField(WorkOutItem,blank=True)

    def __str__(self):
        
        return self.member.user.first_name if self.member.user.first_name else default_title



class IngredientCategory(models.Model):
    ''' ingredient category  '''
    title = models.CharField(max_length=150)
    
    def __str__(self):
        
        return self.title if self.title else default_title


class Ingredient(models.Model):
    ''' Ingredient item to use leater in the ``Meal`` opbject  '''
    image = models.ImageField(upload_to='meals/ingredient/%Y/%M/%d',blank=True)
    title = models.CharField(max_length=150)
    natural_facts = models.JSONField(default={})
    category = models.ForeignKey(IngredientCategory,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        
        return self.title if self.title else default_title

class MealSchedule(models.Model):
    
    ''' Which time should the member take this meal and what type is it  '''
    TYPES = (
        ("snack","Snack"),
        ('meal',"Meal")
    )
    
    title = models.CharField(max_length=150)
    type = models.CharField(max_length=10,choices=TYPES,default='meal')
    schedule = models.TimeField(blank=True)
    
    def __str__(self):
        
        return self.title if self.title else default_title


class Meal(models.Model):
    ''' Meal object to use leater in the DietPlan  '''
    image = models.ImageField(upload_to='meals/meal/%Y/%M/%d',blank=True)
    coocking_media = models.FileField(upload_to='meals/meal/coocking/%Y/%M/%d',blank=True)
    title = models.CharField(max_length=150)
    desc  = models.TextField(max_length=4000)
    ingredients = models.ManyToManyField(Ingredient)
    schedule = models.ForeignKey(MealSchedule,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        
        return self.title if self.title else default_title


class DietPlan(models.Model):
    member = models.ForeignKey("members.Member",on_delete=models.CASCADE,related_name='member_diet_plan')
    meals  = models.ManyToManyField(Meal,blank=True)

    def __str__(self):
        
        return self.member.user.first_name if self.member.user.first_name else default_title
