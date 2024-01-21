from django.test import TestCase

# Create your tests here.
class FirstLevelCategories(models.Model):
    name = models.CharField(_('name'), max_length=200, null=True)
    short_name = models.CharField(_('short name'), max_length=40, null=True, blank=True)
    short_description = models.TextField(_('short description'),null=True, blank=True)
    slug = models.SlugField(_('slug'), allow_unicode=True, unique=True)
    icon = models.ImageField(upload_to='Core/Static/Photos/FirstLevelCategories', verbose_name=_("icon"), null=True, blank=True)
    class Meta:
        verbose_name = _("First Level Category")
        verbose_name_plural = _("First Level Categories")
    
    def __str__(self):
        return self.name + "( ID :" + str(self.id) +" )"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)   



class SecondLevelCategories(models.Model):
    name = models.CharField(_('name'), max_length=200, null=True)
    parent_cat = models.ForeignKey(FirstLevelCategories , verbose_name=_('parent category'), on_delete=models.CASCADE)
    short_name = models.CharField(_('short name'),max_length=40, null=True, blank=True)
    short_description = models.TextField(_('short description'),null=True, blank=True)
    slug = models.SlugField(_('slug'), allow_unicode=True, unique=True)
    icon = models.ImageField(upload_to='Core/Static/Photos/SecondLevelCategories',verbose_name=_("icon"), null=True, blank=True)
    
    class Meta:
        verbose_name = _("Second Level Category")
        verbose_name_plural = _("Second Level Categories")

    def __str__(self):
        return self.name + "( ID :" + str(self.id) +" )"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ThirdLevelCategories(models.Model):
    name = models.CharField(_('name'),max_length=200, null=True)
    parent_cat = models.ForeignKey('Core.SecondLevelCategories', verbose_name=_('parent category'), on_delete=models.CASCADE)
    short_name = models.CharField(_('short name'), max_length=40, null=True, blank=True)
    short_description = models.TextField(_('short description'), null=True, blank=True)
    slug = models.SlugField(_('slug'), allow_unicode=True, unique=True)
    icon = models.ImageField(_('icon'),upload_to='Core/Static/Photos/ThirdLevelCategories', null=True, blank=True)
    
    class Meta:
        verbose_name = _("Third Level Category")
        verbose_name_plural = _("Third Level Categories")
        
    def __str__(self):
        return self.name + "( ID :" + str(self.id) +" )"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ProductsDisplayed(models.Model):
    CHOICES = {
        ('Selling',_("For Selling")),
        ('Renting',_("For Renting")),
        ('Selling or Renting',_("For Selling or Renting"))
    }
    user = models.ForeignKey(User, verbose_name=_('user'), null=True, blank=True, on_delete=models.CASCADE)
    date_registered = models.DateField(verbose_name=_('date registered'), default=timezone.now)
    date_updated = models.DateField(verbose_name=_('date updated'), auto_now=True)
    manufactured_date = models.DateField(verbose_name=_('manufactured date'),null=True)
    product_name = models.CharField(_('product name'), max_length=200,null=False)
    product_category = models.ForeignKey(ThirdLevelCategories, verbose_name=_('product category') ,null=True, on_delete=models.CASCADE)
    product_short_description = models.TextField(_('product short description'), null=True, blank=True)
    manufacturer = models.CharField(_('manufacturer'), max_length=200, null=True, blank=True)
    for_sell_rent = models.CharField(verbose_name=_("For sell, rent or both"), max_length=40, choices=CHOICES, blank=True, null=True)
    model = models.CharField(_('model'), max_length=200, null=True, blank=True)
    price = models.FloatField(_('price'), null=True, blank=True)
   
    class Meta:
        verbose_name = _('Product Displayed')
        verbose_name_plural = _('Products Displayed')
           
    def __str__(self):
        return self.product_name