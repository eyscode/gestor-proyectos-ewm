from django.db import models

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=45)
    information = models.CharField(max_length=45)
    date_creation = models.CharField(max_length=45)

    def __unicode__(self):
        return self.name

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    password = models.CharField(max_length=45)

    def __unicode__(self):
        return self.first_name

#group and user

class Project(models.Model):
    name = models.CharField(max_length=255)
    date_creation = models.DateTimeField()
    company = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

#project and user

class Util(models.Model):
    name = models.CharField(max_length=45)
    date = models.DateTimeField()
    path = models.FilePathField()
    pro_id = models.ForeignKey(Project)

    def __unicode__(self):
        return self.name

class Data(models.Model):
    max_members = models.IntegerField()
    section = models.CharField(max_length=255)
    pro_id = models.ForeignKey(Project)

    def __unicode__(self):
        return self.max_members

class Document(models.Model):
    name = models.CharField(max_length=45)
    path = models.FilePathField()
    date_creation = models.DateTimeField()
    pro_id = models.ForeignKey(Project)

    def __unicode__(self):
        return self.name

class Meeting(models.Model):
    summary = models.CharField(max_length=45)
    description = models.TextField()
    date_creation = models.DateTimeField()
    initial = models.DateTimeField()
    end = models.DateTimeField()
    pro_id = models.ForeignKey(Project)

    def __unicode__(self):
        return self.summary

class Table(models.Model):
    name = models.CharField(max_length=45)
    date_creation = models.DateTimeField()
    columns = models.IntegerField()
    pro_id = models.ForeignKey(Project)

    def __unicode__(self):
        return self.name

class Column(models.Model):
    name = models.CharField(max_length=45)
    position = models.IntegerField()
    tab_id = models.ForeignKey(Table)

    def __unicode__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=45)
    subtitle = models.CharField(max_length=45)
    description = models.TextField()
    state = models.CharField(max_length=45)
    col_id = models.ForeignKey(Column)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    like = models.IntegerField()
    tas_id = models.ForeignKey(Task)

    def __unicode__(self):
        return self.content

class Image(models.Model):
    path = models.FilePathField()
    tas_id = models.ForeignKey(Task)

    def __unicode__(self):
        return self.path

class Check(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    condition = models.IntegerField()
    tas_id = models.ForeignKey(Task)

    def __unicode__(self):
        return self.name
