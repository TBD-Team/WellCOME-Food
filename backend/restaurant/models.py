from django.db import models


class Menu(models.Model):
    date = models.DateField()
    day_period = models.PositiveSmallIntegerField(
        choices=((1, "Breakfast"), (2, "Lunch"), (3, "Dinner")),
        default=1
    )
    meals = models.ManyToManyField("Meal")

    class Meta:
        unique_together = (("date", "day_period"),)

    def __str__(self):
        return f"Menu: {self.date}"


class Meal(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.TextField()
    meal_type = models.PositiveSmallIntegerField(
        choices=((1, "Default"), (2, "Vegetarian"), (3, "Vegan")),
        default=1
    )

    def __str__(self):
        return f"Meal: {self.name}"

