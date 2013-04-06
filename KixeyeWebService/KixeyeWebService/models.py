from django.db import models

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

  def __unicode__(self):
    return u'{0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8}'.format( \
      self.userId, self.first_name, self.last_name, self.nickname, self.creation_time, \
      num_wins, num_losses, win_streak, last_seen_time)

# Class that represents the battle table
class Battle(models.Model):
  attacker_id = models.IntegerField()
  defender_id = models.IntegerField()
  winner_id = models.IntegerField()
  start_time = models.DateField()
  end_time = models.DateField()

  def __unicode__(self):
    return u'{1} | {1} | {1} | {1} | {1}'.format( \
      self.attacker_id, self.defender_id, self.winner_id, self.start_time, self.end_time)