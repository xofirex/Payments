from django.db import models

class Status(models.Model):
    In_Processing = "IP"
    Payed = "PD"
    Refunded = "RF"
    Declined = "DC"
    SHOW_STATUS = [
        (In_Processing, "В обработке"),
        (Payed, "Оплачено"),
        (Refunded, "Возврат"),
        (Declined, "Отклонен")
    ]
    name = models.CharField(max_length=2, choices=SHOW_STATUS, default=In_Processing)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

class Payments(models.Model):
    number = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    purpose = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status, blank=False, null=False, on_delete=models.DO_NOTHING)


    def __str__(self):
        return f'{self.number}'

    class Meta:
        verbose_name = 'Квитанция'
        verbose_name_plural = 'Квитанции'

class StatusString(models.Model):
    status = models.ForeignKey(Status, blank=False, null=True, on_delete=models.DO_NOTHING)
    string = models.TextField(blank=False, null=False, default=None)

    class Meta:
        verbose_name = 'Строка'
        verbose_name_plural = 'Строки'


class PaymentsString(models.Model):
    payments = models.ForeignKey(Payments, blank=False, null=True, on_delete=models.DO_NOTHING)
    string = models.TextField(blank=False, null=False, default=None)

    class Meta:
        verbose_name = 'Строка'
        verbose_name_plural = 'Строки'


