from django.db import models
from django.core.exceptions import ValidationError
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class WBS(models.Model):
    name = models.CharField('Name', max_length=128)
    created_date = models.DateTimeField('Date', auto_now_add=True)

    class Meta:
        verbose_name = 'WBS'
        verbose_name_plural = 'WBS'
        ordering = ('-created_date',)
    
    def __str__(self):
        return f'WBS: {self.name} - {self.created_date}'


class Task(MPTTModel):
    name = models.CharField(max_length=128)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    wbs = models.ForeignKey('WBS', related_name='tasks', on_delete=models.CASCADE, null=True, blank=True,)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def save(self, *args, **kwargs): 
        # is not a child
        if self.wbs is None and self.parent is None:
            raise ValidationError("Cannot create a task without wbs")
        
        # is not root 
        if self.parent is not None:
            self.wbs = self.parent.wbs
        
        super(Task, self).save(*args, **kwargs) 
    

    def __str__(self):
        return f'Task: {self.wbs} - {self.name}'
