from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import (MaxValueValidator,
                                    MinValueValidator,
                                    RegexValidator)
import datetime

User = get_user_model()


class Category(models.Model):
    name = models.CharField(verbose_name="Category name",
                            max_length=256)
    slug = models.SlugField(verbose_name="Category slug",
                            max_length=50,
                            unique=True,
                            validators=[
                                RegexValidator(regex="^[-a-zA-Z0-9_]+$")
                            ])

    def __str__(self) -> str:
        return self.name


class Genre(models.Model):
    name = models.CharField(verbose_name="Genre name",
                            max_length=256)
    slug = models.SlugField(verbose_name="Genre slug",
                            max_length=50,
                            unique=True,
                            validators=[
                                RegexValidator(regex="^[-a-zA-Z0-9_]+$")
                            ])

    def __str__(self) -> str:
        return self.name


class Title(models.Model):
    MINIMUM_TITLE_YEAR = -500000  # The first known work of art

    name = models.CharField(verbose_name="Name of art work",
                            max_length=256,
                            default='default name')
    description = models.TextField(verbose_name="Short description",
                                   null=True,
                                   blank=True)
    year = models.IntegerField(verbose_name="Creation year",
                               validators=[
                                   MinValueValidator(MINIMUM_TITLE_YEAR),
                                   MaxValueValidator(
                                       datetime.date.today().year)],
                               )

    category = models.ForeignKey(Category,
                                 verbose_name='Category',
                                 null=True,
                                 related_name='titles',
                                 on_delete=models.SET_NULL)

    genre = models.ManyToManyField(Genre,
                                   verbose_name='Genre',
                                   related_name="titles",
                                   blank=True,
                                   )


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField(
        verbose_name="Review text",
        blank=False
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Author",
        related_name='reviews'
    )
    score = models.IntegerField(
        verbose_name="Score of the title",
        blank=False,
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    pub_date = models.DateTimeField(
        verbose_name="Publication date",
        auto_now_add=True
    )

    class Meta:
        unique_together = ['title', 'author']

    def __str__(self):
        return self.text


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='сomments',
    )
    text = models.TextField(
        verbose_name="Сomment text",
        blank=False
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Author",
        related_name='сomments',
    )
    pub_date = models.DateTimeField(
        verbose_name="Publication date",
        auto_now_add=True
    )

    def __str__(self):
        return self.text