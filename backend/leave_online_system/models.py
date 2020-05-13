from django.db import models
from django.utils import timezone

now = timezone.now()
# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class LeaveType(models.Model):
    title =  (
            ('Vacation',"Vacation Leave"),
            ('Personal',"Personal Leave"),
            ('Sick', "Sick Leave"),
            ('Ordination leave', "Ordination leave"),
            ('Marriage leave', "Marriage leave"),
            ('Military service leave', "Military service leave"),
            ('Study leave', "Study leave"),
            ('Maternity leave', "Maternity leave"),
            ('Compassionate/Bereavement leave', "compassionate/bereavement leave"),
            ('Accident', "Accident")
    )
    leaves = models.CharField(max_length=300,choices=title, default='Vactaion')

    

    def __str__(self):
        return self.leaves

class Type(models.Model):
    title = (
            ('Full day', "Full Day"),
            ('Half day', "Half Day")
    )
    choices = models.CharField(max_length=30,choices=title, default='Fullday')

    def __str__(self):
        return self.choices

    

class Employee(models.Model):
    fullName = models.CharField(max_length=50)
    emp_Id = models.CharField (max_length=4)
    initial_Id = models.CharField(max_length=2)
    email = models.CharField(max_length=50)  
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    description = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    createTime = models.DateTimeField(default=timezone.now) 
    
    def __str__(self):
        return self.fullName + ' ' + self.initial_Id

class LeaveDate(models.Model):
    fullName = models.ForeignKey(Employee, on_delete=models.CASCADE)     
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    description = models.ForeignKey(LeaveType, on_delete=models.CASCADE)  
    type = models.ForeignKey(Type, on_delete=models.CASCADE)  
    leaveDate = models.DateField()
    leaveEndDate = models.DateField()    
    createTime = models.DateField() 

    def __str__(self): 
        return str(self.fullName) + ' Description ' + str(self.description)

    




    



