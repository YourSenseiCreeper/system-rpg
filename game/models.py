from django.db import models


class Answer(models.Model):
    answer_nbr = models.AutoField(primary_key=True)
    next_dialog = models.IntegerField()
    text = models.CharField(max_length = 1000, blank = False)
    action_result = models.CharField(max_length = 500)

    def __str__(self):
        return "(%s) %s" % (self.answer_nbr, self.text)


class Character(models.Model):
    character = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 150, blank = False)
    description = models.CharField(max_length = 1500)

    def __str__(self):
        return self.name


class Narration(models.Model):
    narration = models.AutoField(primary_key=True)
    friendly_name = models.CharField(max_length = 300, blank = True)
    text = models.CharField(max_length = 5000, blank = True)

    def __str__(self):
        if self.friendly_name is None:
            return self.narration_id
        else:
            return self.friendly_name


class Location(models.Model):
    location = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 200, blank = False)
    description = models.CharField(max_length = 5000, blank = True)

    def __str__(self):
        return self.name


class Dialogue(models.Model):
    dialogue = models.AutoField(primary_key=True)
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    answers = models.ManyToManyField(Answer)
    access_lvl = models.IntegerField(default=0, blank = False)
    character = models.ForeignKey(Character, on_delete = models.CASCADE)
    narration = models.ForeignKey(Narration, on_delete = models.CASCADE)
    friendly_name = models.CharField(max_length = 200, blank = False)

    def __str__(self):
        return "(%s) %s" % (self.dialogue, self.friendly_name)
