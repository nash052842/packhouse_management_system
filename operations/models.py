from django.db import models


class Harvest(models.Model):
    harvest = models.CharField(max_length=50)
    total_mites_harvest = models.IntegerField(default=0)
    batch_number = models.CharField(max_length=50)
    date_harvested = models.DateTimeField()

    def __str__(self):
        return f"{self.harvest}, {self.total_mites_harvest}, {self.batch_number}, {self.date_harvested}"


class Package(models.Model):
    package = models.IntegerField()
    pack_date = models.DateField()
    harvest = models.ForeignKey(Harvest, on_delete=models.CASCADE, related_name='packages')
    batch_number = models.CharField(max_length=50)
    unit_size = models.IntegerField()
    mites_tube = models.IntegerField()

    def __str__(self):
        return f"{self.package}, {self.harvest}, {self.batch_number}, {self.unit_size}, {self.mites_tube}, {self.pack_date}"


class Inventory(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='inventories')
    units_available = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return f"{self.package}, {self.units_available}"


class QualityControl(models.Model):
    quality_check = models.IntegerField()
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='qualitycontrol')
    qc_date_time = models.DateTimeField()
    mortality_pct = models.DecimalField(max_digits=5, decimal_places=2)
    contamination = models.TextField()
    pass_fail = models.BooleanField()

    def __str__(self):
        return f"{self.quality_check}, {self.package}, {self.qc_date_time}, {self.mortality_pct}, {self.contamination}, {self.pass_fail}"


class Dispatch(models.Model):
    dispatch = models.IntegerField()
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='dispatches')
    dispatch_date_time = models.DateTimeField()
    client = models.CharField(max_length=100)
    method = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.dispatch}, {self.package}, {self.client}, {self.method}, {self.quantity}"
