from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

class Patient(models.Model):
    name = models.TextField()
    # doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    # doctor = models.ManyToManyField(Doctor, through='Reservation', related_name='patients')
    # 참조로 조회할 수 있게 설정 through=...
    # 역참조로 조회할 수 있게 설정 related_name=...
    doctor = models.ManyToManyField(Doctor,related_name='patients')

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

# 중개모델
# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.doctor.id}의사의 {self.patient.id}번 환자'    
    