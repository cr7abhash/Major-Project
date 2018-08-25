from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.utils.text import slugify


PRODUCT_SUB_CAT = (
    ('highend', 'Highend'),
    ('midlevel', 'Midlevel'),
    ('lowend', 'Lowend'),
)


class Category(models.Model):
    title = models.CharField(max_length=120, unique=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return str(self.title)
    

class Product(models.Model):
    title = models.CharField(max_length = 120)
    product_id = models.CharField(max_length=120, unique=True, null = False, blank = False)
    description = models.TextField(blank = True, null = True)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    active = models.BooleanField(default = True,  verbose_name="Availability ?")
    manufacturer = models.CharField(max_length =120)
    category = models.ForeignKey(Category, null=True)
    sub_category = models.CharField(max_length=120, choices=PRODUCT_SUB_CAT, default='highend')
    relatable_keyword = models.CharField(max_length=120, null = True, blank = True,  verbose_name="Keyword to relate")


    def __str__(self):
        return str(self.title)
    
    def get_image_url(self):
        p1_images = self.productimage_set.all()
        img = p1_images.first()
        if img:
            return img.image.url
        return img

    def get_absolute_url(self):
        return reverse("product_detail", kwargs = {"pk": self.pk})


class Variation(models.Model):
    product = models.ForeignKey(Product)
    title = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits=20, null=False)
    sale_price = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    active = models.BooleanField(default = True)
    inventory = models.IntegerField(null = True, blank = True)

    def __str__(self):
        return str(self.title)
    
    def get_price(self):
        if self.sale_price is not None:
            return self.sale_price
        else:
            return self.price

    def get_absolute_url(self):
        return self.product.get_absolute_url()

    def add_to_cart(self):
        return "%s?item=%s&qty=1" %(reverse("cart"), self.id)

    def remove_from_cart(self):
        return "%s?item=%s&qty=1&delete=True" %(reverse("cart"), self.id)

    def get_title(self):
        return "%s - %s" %(self.product.title, self.title)

    

def product_post_save(sender, instance, created, *args, **kwargs):
    product = instance
    variations = product.variation_set.all()
    if variations.count() == 0:
        new_var = Variation()
        new_var.product = product
        #new_var.title = product.title + " - Default"
        new_var.title = str(product.product_id) + " - Default"
        new_var.price = product.price
        new_var.save()

post_save.connect(product_post_save, sender=Product)

# ------------------------ images ------------------------------------------

def image_upload_to(instance, filename):
    title = instance.product.title
    slug = slugify(title)
    basename, file_extension = filename.split(".")
    new_filename = "%s-%s.%s" %(slug, instance.id, file_extension)
    return "products/%s/%s" %(slug, new_filename)


class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to = image_upload_to)
    
    def __str__(self):
        return self.product.title
    
    def get_image_url(self):
        img = self
        if img:
            return img.image.url
        return img    
