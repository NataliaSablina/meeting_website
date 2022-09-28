from django.db import models
from userprofile.models import Profile


MALE = "M"
FEMALE = "F"
COMPANY = "C"

SEX_CHOICES = [
    (MALE, "male"),
    (FEMALE, "female"),
    (COMPANY, "company"),
]


class Form(models.Model):
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, verbose_name="profile", unique=True
    )

    class Meta:
        verbose_name = "Form"
        verbose_name_plural = "Forms"
        db_table = "Form"

    def __str__(self):
        return f"form_{self.profile}"


class CommonData(models.Model):
    form = models.OneToOneField(
        Form, on_delete=models.PROTECT, verbose_name="form", null=True
    )
    first_name = models.CharField(max_length=250, verbose_name="first_name", null=True)
    surname = models.CharField(max_length=250, verbose_name="surname", null=True)
    patronymic = models.CharField(
        max_length=250, verbose_name="patronymic", blank=True, null=True
    )
    sex = models.CharField(
        max_length=10, choices=SEX_CHOICES, default=MALE, verbose_name="sex", null=True
    )
    zodiac = models.CharField(
        max_length=20, verbose_name="zodiac", blank=True, null=True
    )
    country = models.CharField(max_length=100, verbose_name="country", null=True)
    city = models.CharField(max_length=100, verbose_name="city", null=True)
    personal_info = models.TextField(verbose_name="personal_info", null=True)

    class Meta:
        verbose_name = "CommonData"
        verbose_name_plural = "CommonData"
        db_table = "CommonData"

    def __str__(self):
        return f"{self.form}_commondata"


class Preferences(models.Model):
    form = models.OneToOneField(
        Form, on_delete=models.PROTECT, verbose_name="form", null=True
    )

    class Meta:
        verbose_name = "Preferences"
        verbose_name_plural = "Preferences"
        db_table = "Preferences"

    def __str__(self):
        return f"{self.form}_preferences"


class Type(models.Model):
    form = models.OneToOneField(
        Form, on_delete=models.PROTECT, verbose_name="form", null=True
    )

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Type"
        db_table = "Type"

    def __str__(self):
        return f"{self.form}_type"


class DifferentInfo(models.Model):
    form = models.OneToOneField(
        Form, on_delete=models.PROTECT, verbose_name="form", null=True
    )
    phone = models.CharField(max_length=20, verbose_name="phone", null=True)
    machine_mark = models.CharField(
        max_length=250, verbose_name="machine_mark", null=True
    )

    class Meta:
        verbose_name = "DifferentInfo"
        verbose_name_plural = "DifferentInfo"
        db_table = "DifferentInfo"

    def __str__(self):
        return f"{self.form}_different_info"
