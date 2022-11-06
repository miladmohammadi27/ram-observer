import datetime

from django.db import models

class RAMStatus(models.Model):
    used = models.FloatField(max_length=50, verbose_name='Used Memory Status(MB)')
    free = models.FloatField(max_length=50, verbose_name='Free Memory Status(MB)')
    total = models.FloatField(max_length=50, verbose_name='Total Memory Status(MB)')
    report_date = models.DateTimeField(verbose_name='Report Created', default=datetime.datetime.now())

    class Meta:
        verbose_name = 'RAM Status'
        verbose_name_plural = 'RAM Statuses'

    def __str__(self):
        return '{} - Total: {} - Free: {} - Used: {}'.format(self.report_date, self.total, self.free, self.used)