from django.db import models
from datetime import date


class Category(models.Model):
    """ Categories"""
    name = models.CharField("Category", max_length=150)
    description = models.TextField("Description")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Actor(models.Model):
    """Actors"""
    name = models.CharField("Name", max_length=100)
    age = models.PositiveSmallIntegerField("Age", default=0)
    description = models.TextField("Description")
    image = models.ImageField("Pictures", upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Actors and director"
        verbose_name_plural = "Actors and director"


class Genre(models.Model):
    """Genre"""
    name = models.CharField("Category", max_length=100)
    description = models.TextField("Description")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class Movie(models.Model):
    """Movies"""
    title = models.CharField("Title", max_length=100)
    tagLine = models.CharField("Tag", max_length=100, default='')
    description = models.TextField("Description")
    poster = models.ImageField("Poster", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Release date", default=2019)
    country = models.CharField("Country", max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name="director", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="actors", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="genres")
    world_premiere = models.DateField("Premiere in world", default=date.today)
    budget = models.PositiveIntegerField("Budget", default=0, help_text="sum in dollars")
    fees_in_usa = models.PositiveIntegerField("Fees USA", default=0, help_text="sum in dollars")
    fees_in_world = models.PositiveIntegerField("Fees in World", default=0, help_text="sum in dollars")
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Draft", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"


class MovieShots(models.Model):
    """Screenshot from movie"""
    title = models.CharField("Title", max_length=100)
    description = models.TextField("Description")
    image = models.ImageField("Pictures", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Movie", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Shot from movie"
        verbose_name_plural = "Shots from movie"


class RatingStar(models.Model):
    """Star rating"""
    value = models.PositiveSmallIntegerField("Value", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Star rating"
        verbose_name_plural = "Stars rating"


class Rating(models.Model):
    """Rating"""
    ip = models.CharField("IP address", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="star")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="movie")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"


class Reviews(models.Model):
    """Reviews"""
    email = models.EmailField()
    name = models.CharField("Name", max_length=100)
    text = models.TextField("Message", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Parent", on_delete=models.SET_NULL, blank=True, null=True)
    movie  = models.ForeignKey(Movie, verbose_name="movie", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
