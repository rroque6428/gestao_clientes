from django.db import models
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template

# - - - DOCUMENTO

class Documento(models.Model):
    num_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.num_doc


# - - - PERSON

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)
    doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s, %s" % (self.last_name, self.first_name)

    @property
    def fullname(self):
        return "%s, %s" % (self.last_name, self.first_name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        context = {"nome": self.first_name}

        msg_plain_text = render_to_string("clientes/emails/novo_cliente.txt", context=context)
        msg_html = render_to_string("clientes/emails/novo_cliente.html", context=context)

        send_mail(
            'Novo cliente (%s)' % self.first_name,
            msg_plain_text,
            'rroque6428@terra.com.br',
            ['rroque6428@terra.com.br'],
            html_message=msg_html,
            fail_silently=False,
            )
