from django.db import models

class Harvest(models.Model):
    Harvest = models.CharField(max_length=50)
    total_mites_Harvest= models.IntegerField
    batch_number = models.CharField(max_length=50)
    date_harvested= models.DateTimeField()
def __str__(self):
    return(f"{self.harvest},{self.total_mite_Harvest},{self.batch_number},{self.date_harvested}",)

class Package(models.Model):
    package = models.IntegerField
    pack_date = models.DateField( auto_now=False, auto_now_add=False)
    Harvest = models.ForeignKey(Harvest,on_delete=models.CASCADE,related_name='harvest')
    batch_number =models.CharField(max_length=50)
    unit_size =models.IntegerField
    mites_tube = models.ImageField
    pack_date = models.DateField( auto_now=False, auto_now_add=False)

def __str__(self):
    return(f"{self.package},{self.Harvest},{self.batch_numer},{self.unit_size},{mites_tube},{self.pack_date}")


class Inventory(models.Model):
    package= models.ForeignKey(Package,on_delete=models.CASCADE, related_name='package')
    units_availlable =models.IntegerField
def __str__(self):
    return (f"{self.package}",[self.units_availlable])

class Quality_control(models.Model):
    quality_check = models.IntegerField
    harvest =models.ForeignKey(Package,on_delete=models.CASCADE,related_name='dispatch')
    qc_date_time =models.DateTimeField
    mortality_pct =models.DecimalField
    contamination = models.TextField
    pass_fail =models.BooleanField

def __str__(self):
    return (f"{self.quality_check},{self.package},{self.qc_date_time}.{self.mortality_pct},{self.contamination},{self.pass_fail}",)


class Distpach(models.Model):
    dispatch= models.IntegerField
    package = models.ForeignKey(Package,on_delete=models.CASCADE,related_name='quality_control')
    dispatch_date_time = models.DateTimeField
    client = models.CharField(max_length=100)
    method = models.CharField(max_length=50)
    quantity = models.IntegerField

def __str__(self):
    return (f"{self.dispatch},{self.package},{self.client},{self.method},{self.quantity}",)

