from django.db import models

from apps.students.models import Student


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return "{} {} {}".format(self.student, self.date, self.time)

    class Meta:
        ordering = ['-date']
        