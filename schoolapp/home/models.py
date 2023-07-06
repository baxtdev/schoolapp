from django.db import models
from django.urls import reverse


# Create your models here.


class List(models.Model):
    choice_class = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'),
                    ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'),
                    ('9', '9'), ('10', '10'), ('11', '11')]
    list_class = models.CharField(choices=choice_class, max_length=10, default=None, null=True, verbose_name="Класс")
    name = [('A', 'А'), ('Б', 'Б')]
    letter_class = models.CharField(choices=name, max_length=10, default=None, null=True)

    class Meta:
        verbose_name = "класс кошуу"
        verbose_name_plural = 'класстарды кошуу'
        ordering = ['-id']

    def __str__(self):
        return f'{self.list_class} {self.letter_class} класс'


class Student(models.Model):
    gender_choices = [('АЯ', 'Аял'), ('ЭР', 'Эркек')]
    gender = models.CharField(choices=gender_choices, max_length=10,
                              default=None, null=True, verbose_name="Пол")
    first_name = models.CharField(max_length=250, verbose_name="Аты")
    last_name = models.CharField(max_length=250, verbose_name="Фамилиясы")
    fathers_name = models.CharField(max_length=250, verbose_name="Атасынын аты")
    mothers_name = models.CharField(max_length=250, verbose_name="Апасынын аты")
    date_birth = models.DateField(verbose_name="туулган датасы", auto_now_add=False)
    # objects = models.Manager()
    l_class = models.ForeignKey(List, on_delete=models.CASCADE, blank=True, null=True , related_name='students',verbose_name="Класс")
    phone_number = models.CharField(max_length=12, null=True, verbose_name="телефон")




    # The default manager
    # choice_class = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'),
    #                 ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'),
    #                 ('9', '9'), ('10', '10'), ('11', '11')]
    # list_class = models.CharField(choices=choice_class, max_length=10, default=None, null=True)
    # std_classes = models.ForeignKey(ABC, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Окуучу"
        verbose_name_plural = 'Окуучулар'
        ordering = ['id']

    def __str__(self):
        return f'Имя: {self.first_name}, Фамилия: {self.last_name}'


class Teachers(models.Model):
    first_name = models.CharField(max_length=250, verbose_name="Аты")
    last_name = models.CharField(max_length=250, verbose_name="Фамилиясы")
    sub = models.CharField(max_length=250, verbose_name="Окутатурган сабагы")
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'

    class Meta:
        verbose_name_plural = 'Мугалимдер'


class Courses(models.Model):
    li_class = models.ForeignKey(List, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Класс")

    # class_name = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'),
    #               ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'),
    #               ('9', '9'), ('10', '10'), ('11', '11')]
    # number_class = models.CharField(choices=class_name, max_length=10, default=None, null=True)
    # # child_name = models.CharField(max_length=250)
    # classes = models.ForeignKey(ABC, on_delete=models.CASCADE, blank=True, null=True)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Класс жетекчиси")


    class Meta:
        verbose_name_plural = 'Класстар'

    def __str__(self):
        return f'{self.li_class}'

# class Student_Class(models.Model):
#     stdclass = models.ManyToManyField(Student)



# SELECT first_name, l_class_id From home_student where l_class_id=1