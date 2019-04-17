from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    """
    Class that contains location details of the image posted
    """
    name = models.CharField(max_length = 30)
    description = models.TextField()

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def del_location(self):
        self.delete()  
class Category(models.Model):
    """
    Class that contains the category details of the image posted
    """
    name = models.CharField(max_length = 30)
    description = models.TextField()

    def __str__(self):
        return self.name

    def save_cat(self):
        self.save()

    def del_cat(self):
        self.delete()
      
    


class Hotel(models.Model):
    photo = models.ImageField(upload_to = 'photo/',blank=True,)
    hotel_name = models.CharField(max_length =30)
    description = models.CharField(max_length =30)
    location = models.ForeignKey(Location,max_length=140,on_delete =models.CASCADE, blank=True, null=True) 
    category = models.ForeignKey(Category,max_length=140,on_delete =models.CASCADE,  blank=True, null=True) 

    
    def __str__(self):
        return self.hotel_name

    def save_hotel(self):
        self.save() 

    def update_hotel(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs) 
    @classmethod
    def all_hotel(cls):
        photos = cls.objects.all()
        return photos
    @classmethod
    def hotel_locations(cls):
        photos = cls.objects.order_by('location')
        return photos 
    @classmethod
    def photos_categories(cls):
        photos = cls.objects.order_by('category')
        return photos 
    @classmethod
    def search_by_category(cls, search_input):
        photos= cls.objects.filter(category__name__icontains=search_input)
        return photos      

    class Meta:
        ordering = ['hotel_name']
         
