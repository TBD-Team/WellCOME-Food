import uuid

from django.conf import settings # AUTH_USER_MODEL
from django.db import models, transaction


class Account(models.Model):
    purchase_code = models.CharField(max_length=8, unique=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=19, decimal_places=10, default=0)

    def __str__(self):
        return f"Account: {self.user.username}"

    @classmethod
    def create(cls, user):
        purchase_code = str(uuid.uuid4())[-8:]
        account = cls.objects.create(
            user=user,
            purchase_code=purchase_code
        )
        return account

    def get_user_tax(self):
        if self.user.is_student:
            return 3.0
        elif self.user.is_professor:
            return 8.0
        elif self.user.is_technician or self.user.is_outsourced:
            return 4.0
        return 10.0

    def verify_balance(self, value):
        if self.balance >= value:
            return True
        return False

    def make_purchase(self):
        value = self.get_user_tax()
        if self.verify_balance(value):
            with transaction.atomic():
                purchase = Purchase.objects.create(value=value, account=self)
                self.balance = float(self.balance) - value
                self.save()
            return purchase
        else:
            raise Exception("Insufficient Balance!")


class Credit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    value = models.DecimalField(max_digits=19, decimal_places=10)
    status = models.CharField(
        max_length=2,
        choices=(("AN", "InAnalysis"), ("AP", "Approved"), ("DN", "Denied")),
        default="AN"
    )
    gru = models.OneToOneField("GRU", on_delete=models.CASCADE)
    account = models.ForeignKey("Account", on_delete=models.CASCADE)

    def __str__(self):
        return f"Credit: {self.value}, <{self.account}>"

    @classmethod
    def create(cls, account, value, code, expiration_time):
        with transaction.atomic():
            gru = GRU.objects.create(
                code=code,
                expiration_time=expiration_time
            )
            credit = cls.objects.create(
                account=account,
                value=value,
                gru=gru
            )
        return credit


class GRU(models.Model):
    receipt = models.FileField(upload_to="", null=True)
    code = models.CharField(max_length=15)
    expiration_time = models.DateField()

    def __str__(self):
        return f"GRU: {self.code}"


class Purchase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    value = models.DecimalField(max_digits=19, decimal_places=10)
    account = models.ForeignKey("Account", on_delete=models.CASCADE)

    def __str__(self):
        return f"Purchase: {self.value}, <{self.account}>"
