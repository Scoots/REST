from django.db import models
import os

# This class combines the user and user_statistics tables
class User(models.Model):
  user_id = models.IntegerField()
  first_name = models.CharField(max_length=45)
  last_name = models.CharField(max_length=45)
  nickname = models.CharField(max_length=45)
  creation_time = models.DateField()

  num_wins = models.IntegerField()
  num_losses = models.IntegerField()
  win_streak = models.IntegerField()
  last_seen_time = models.DateField()

  def __init__(self, params):
    self.user_id = params[0]
    self.first_name = params[1]
    self.last_name = params[2]
    self.nickname = params[3]
    self.creation_time = params[4]
    self.num_wins = params[5]
    self.num_losses = params[6]
    self.win_streak = params[7]
    self.last_seen_time = params[8]

  def __unicode__(self):
    return u'user_id:{0}{9}first_name:{1}{9}last_name:{2}{9}nickname:{3}{9}creation_time:{4} \
      {9}num_wins:{5}{9}num_losses:{6}{9}win_streak:{7}{9}last_seen_time:{8}{9}'.format( \
      self.user_id, self.first_name, self.last_name, self.nickname, self.creation_time, \
      self.num_wins, self.num_losses, self.win_streak, self.last_seen_time, os.linesep)

# Class that represents the battle table
class Battle(models.Model):
  attacker_id = models.IntegerField()
  defender_id = models.IntegerField()
  winner_id = models.IntegerField()
  start_time = models.DateField()
  end_time = models.DateField()

  def __unicode__(self):
    return u'attacker:attacker:{0}{6}defender:{1}{6}winner:{2}{6}start:{3}{6}end:{4}{6}'.format( \
      self.attacker_id, self.defender_id, self.winner_id, self.start_time, self.end_time, os.linesep)