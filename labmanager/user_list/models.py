from django.db import models
from django.core.urlresolvers import reverse
# from .forms import UserForm
import datetime

# from django.utils import timezone
# from django.contrib.auth.models import User
# from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget

# Create your models here.


class ActiveManager (models.Manager):
    def get_queryset(self):
        return super(ActiveManager,self).get_queryset().filter(status='Active')


USER_TYPE_CHOICES=(
    ('U', 'User'),
    ('A', 'Lab admin'),
)

USER_RANK_CHOICES=(
    ('UG', 'Under graduate'),
    ('MSc', 'MSC student'),
    ('PhD', 'PhD student'),
    ('Staff', 'Staff'),
    ('Other', 'Other'),
)

STATUS_CHOICES=(
    ('NA', 'Non Active'),
    ('Active', 'Active'),
    ('New User', 'New'),
)


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super(ActiveManager,
                     self).get_queryset()\
                    .filter(status='Active')

class User(models.Model):
    users=models.Manager()
    non_active=ActiveManager()

    name=models.CharField(max_length = 30)
    email=models.CharField(max_length = 30)
    supervisor=models.CharField(max_length = 30)
    user_type = models.CharField(max_length = 10, choices = USER_TYPE_CHOICES, default = 'Non Active')
    user_rank = models.CharField(max_length = 10, choices = USER_RANK_CHOICES, default = 'Other')
    CID=models.IntegerField(null=True, blank=True)
    join_date = models.DateField(default=datetime.date(1977,7,25))
    status=models.CharField(max_length=8, choices=STATUS_CHOICES, default='Active')
    description = models.TextField(null=True, blank=True)

    objects=models.Manager()
    active=ActiveManager()
    class Meta:
        ordering = ('user_rank','name',)

    def __str__(self):
        return "%s,  %s, %s, (%s's group), Active since: %s" % \
               (self.name, self.email, self.user_rank, self.supervisor, self.join_date)

    def get_absolute_url(self):
        return reverse('users_list',
                        args=[self.name],)