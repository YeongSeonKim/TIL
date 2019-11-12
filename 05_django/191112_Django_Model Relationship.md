# Model Relationship

## 1.Many to one

- 코드 ~
  - ~~

#### 



## 2. Many to Many

#### 2.1 1:N의 한계

#### 2.2  중개 모델 생성

- 1:N으로만 구현하려니 예약 정보 시스템을 표현하기가 어렵다.
  - 예를 들어 Patient가 다른 Doctor에게 진료를 받고자 할 때, 기존 기록을 지우지 않으려면 새로운 Patient 인스턴스를 생성해야 한다.
- 중개 모델(class Reservation)을 만들어서 Doctor와  Patient를 이어주는 예약 정보를 담아보자.

#### 2.3 through 옵션

- Patient 입장에서 중개 모델을 거쳐서 `reservation_set`형태로 예약 정보를 가져오는 것은 너무 불편하다.
  - 마찬가지로 Doctor도 `reservation_set`형태로 예약 정보를 먼저 불러온 뒤에 Patient의 정보를 꺼내 올 수 있다.
- Doctor 정보를 중개 모델을 거치지 않고, 다이렉트로 가져와보자.

#### 2.4 `related_name`

- 이제 Patient의 입장에서는 `patient.doctors.all()`과 같은 형태로 쉽게 Doctor 정보를 가져올 수 있다.
- 마찬가지로 Doctor의 입장에서도 `doctor.patients.all()`과 같은 형태로 Patient의 정보를 가져올 수 있게끔, `related_name`옵션을 사용해 보자.

#### 2.5 Many To Many

- 단순히 Doctor와 Patient를 이어줄 생각이라면 , 굳이 중개모델이 필요 없다. `ManyToManyField`만 사용하면 장고가 자동으로 중개 테이블을 만들어준다.

```python
# manytomany/models.py

class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

class Patient(models.Model):
    name = models.TextField()
    # doctor = models.ManyToManyField(Doctor, through='Reservation', related_name='patients')
    doctor = models.ManyToManyField(Doctor,related_name='patients')

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

```

- 중개모델을 만들지 않았지만 DB를 확인해보면 임의의 테이블을 자동으로 생성해준 것을 확인 할 수 있다.

![image-20191112165817926](assets\image-20191112165817926-1573547494955.png)

ex) 1:N ( 의사 : 환자 )

```shell
In [1]: doctor1 = Doctor.objects.create(name='도현')

In [2]: doctor2 = Doctor.objects.create(name='은애')

In [3]: patient1 = Patient.objects.create(name='민승')

In [4]: patient2 = Patient.objects.create(name='세환')

In [5]: Reservation.objects.create(doctor=doctor1, patient=patient2)
Out[5]: <Reservation: Reservation object (1)>

In [6]: Reservation.objects.create(doctor=doctor2, patient=patient2)
Out[6]: <Reservation: Reservation object (2)>

In [7]: Reservation.objects.get(pk=1)
Out[7]: <Reservation: 1의사의 2번 환자>


```



삭제하기

![image-20191112162411396](assets\image-20191112162411396-1573547494956.png)

마이그레이션에 있는  0001도 삭제

![image-20191112162641969](assets\image-20191112162641969-1573547494956.png)



다시 makemigration, migrate









```shell
In [1]: Doctor.objects.create(name='은애')
Out[1]: <Doctor: 1번 의사 은애>

In [2]: Doctor.objects.create(name='도현')
Out[2]: <Doctor: 2번 의사 도현>

In [3]: doctor1 = Doctor.objects.get(pk=1)

In [4]: doctor2 = Doctor.objects.get(pk=2)

In [5]: patient1 = Patient.objects.create(name='세환')

In [6]: patient2 = Patient.objects.create(name='민승')

In [7]: doctor1.patients.all()
Out[7]: <QuerySet []>

In [8]: doctor2.patients.all()
Out[8]: <QuerySet []>

In [9]: doctor1.patients.add(patient1)

In [10]: doctor1.patients.all()
Out[10]: <QuerySet [<Patient: 1번 환자 세환>]>

In [11]: doctor1.patients.add(patient2)

In [12]: doctor1.patients.all()
Out[12]: <QuerySet [<Patient: 1번 환자 세환>, <Patient: 2번 환자 민승>]>

In [13]: doctor1.patients.remove(patient1)

In [14]: doctor1.patients.all()
Out[14]: <QuerySet [<Patient: 2번 환자 민승>]>
```

![image-20191112163458597](assets\image-20191112163458597-1573547494956.png)