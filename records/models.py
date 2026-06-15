from django.db import models
from django.contrib.auth.models import User


class Darta(models.Model):
    darta_no = models.CharField(max_length=100)
    darta_date = models.DateField()

    received_from = models.CharField(max_length=255)

    subject = models.CharField(max_length=255)

    remarks = models.TextField(blank=True)

    document = models.FileField(
    upload_to='darta_documents/',
    blank=True,
    null=True
)

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.darta_no


class DartaDocument(models.Model):

    darta = models.ForeignKey(
        Darta,
        on_delete=models.CASCADE,
        related_name='documents'
    )

    file = models.FileField(
        upload_to='darta_documents/'
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )


class Chalan(models.Model):

    chalan_no = models.CharField(max_length=100)

    chalan_date = models.DateField()

    sent_to = models.CharField(max_length=255)

    subject = models.CharField(max_length=255)

    remarks = models.TextField(blank=True)

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)
    document = models.FileField(
    upload_to='chalan_documents/',
    blank=True,
    null=True
)

    def __str__(self):
        return self.chalan_no


class ChalanDocument(models.Model):

    chalan = models.ForeignKey(
        Chalan,
        on_delete=models.CASCADE,
        related_name='documents'
    )

    file = models.FileField(
        upload_to='chalan_documents/'
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )
class ActivityLog(models.Model):
     action = models.CharField(max_length=255)
     created_at = models.DateTimeField(auto_now_add=True)
     def __str__(self):
         return self.action