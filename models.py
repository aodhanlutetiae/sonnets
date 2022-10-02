from django.db import models

# this will map to the database
class SonnetModel(models.Model):
    line = models.CharField(max_length=200)
    sonnet_nb = models.DecimalField(decimal_places = 0, max_digits =3)

    class Meta:
        verbose_name_plural = "sonnets"

    def __str__(self):
        return self.line
