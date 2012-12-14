from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Template(models.Model):
    name = models.CharField(max_length=250)
    profile = models.ForeignKey(Profile)


class Client(models.Model):
    user = models.OneToOneField(User)
    profile = models.ForeignKey(Profile)
    projects = models.ManyToManyField('Project', through='Client_has_Project')

    def __unicode__(self):
        return self.user.__unicode__()


class Project(models.Model):
    name = models.CharField(max_length=250)
    date_creation = models.DateTimeField(auto_now_add=True)
    company = models.CharField(max_length=250, null=True, blank=True)
    base = models.BooleanField(default=False)
    template = models.ForeignKey(Template, null=True, blank=True)
    creador = models.ForeignKey(Client)

    def __unicode__(self):
        return self.name


class Client_has_Project(models.Model):
    client = models.ForeignKey(Client)
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return "{} | {}".format(self.client.__unicode__(), self.project.__unicode__())


class Group(models.Model):
    name = models.CharField(max_length=100)
    information = models.CharField(max_length=250)
    date_creation = models.DateTimeField(auto_now_add=True)
    creador = models.ForeignKey(Client, related_name='mis_grupos')

    def __unicode__(self):
        return self.name


class Group_has_Client(models.Model):
    group = models.ForeignKey(Group)
    client = models.ForeignKey(Client)

    def __unicode__(self):
        return "{} | {}".format(self.client.__unicode__(), self.group.__unicode__())


class Util(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField()
    path = models.FilePathField()
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.name


class Data(models.Model):
    max_members = models.IntegerField()
    section = models.CharField(max_length=100)
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.max_members


class Document(models.Model):
    name = models.CharField(max_length=50)
    path = models.FilePathField()
    date_creation = models.DateTimeField()
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.name


class Meeting(models.Model):
    summary = models.CharField(max_length=100)
    description = models.TextField()
    date_creation = models.DateTimeField()
    initial = models.DateTimeField()
    end = models.DateTimeField()
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.summary


class Table(models.Model):
    name = models.CharField(max_length=50)
    date_creation = models.DateTimeField(auto_now_add=True)
    columns = models.IntegerField()
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.name


class Column(models.Model):
    name = models.CharField(max_length=45)
    position = models.IntegerField()
    table = models.ForeignKey(Table, related_name="columnas")

    def __unicode__(self):
        return self.name


class Work_Package(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    prioridad = models.IntegerField()
    table = models.ForeignKey(Table)
    project = models.ForeignKey(Project, related_name="paquetes")

    def __unicode__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    state = models.CharField(max_length=50, null=True, blank=True)
    column = models.ForeignKey(Column, related_name="tareas", null=True, blank=True)
    work_package = models.ForeignKey(Work_Package, null=True, blank=True, related_name="tareas")

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    like = models.IntegerField()
    task = models.ForeignKey(Task)

    def __unicode__(self):
        return self.content


class Image(models.Model):
    path = models.FilePathField()
    task = models.ForeignKey(Task)

    def __unicode__(self):
        return self.path


class Check(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    condition = models.IntegerField()
    task = models.ForeignKey(Task)

    def __unicode__(self):
        return self.name


class Log(models.Model):
    project = models.ForeignKey(Project)
    datetime = models.DateTimeField(auto_now_add=True)
    mensaje = models.CharField(max_length=200)

    def __unicode__(self):
        return self.mensaje.format(self.project)