from datetime import date
import json


def days_in_current_year():
  '''
  gets how many days are in a current year and returns it
  days_in_current_year()->int
  '''
  year = date.today().year
  is_leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

  if is_leap_year:
    return 366
  else:
    return 365

def days_elapsed():
  '''
  calculates how many days elpased since the beginning of the year
  days_elapsed()->int
  '''
  today = date.today()
  year_start = date(today.year, 1, 1)
  return (today - year_start).days + 1

def days_percent():
  '''
  turns how many days elpased in to procents
  days_procent()->str
  '''
  ret = (100 * days_elapsed())/ days_in_current_year()
  return "{:.2f}".format(ret)


def calc_all_weeks(lifespan=66):
  """# the bigger the lifespan the more weeks the program skips
  calculates how many weeks will be in somones lifespan
  calc_all_weeks() -> int
  """
  ret = lifespan *52
  return ret

def date_to_weeks(day,month):
  """ 
  counts how many weeks have passed sinced beginninig of the year
  date_to_weeks()-> int
  """
  if month == 1:
    wm = 0
  else:
    wm = month *4
  wd = day//7
  ret= wd + wm
  return ret



def weeks_since_birth(bday=1, bmonth=1, byear=2000):
  """ 
  calculates how many weeks have passed since inputed date
  weeks_since_birth()-> int
  """
  todayd = date.today().day
  todaym = date.today().month
  todayy = date.today().year
  diffyw = (todayy - byear)*52
  bw = date_to_weeks(bday, bmonth)
  tw = date_to_weeks(todayd,todaym)
  return (tw-bw) + diffyw   #logika chyba git delikatne różnice w wynikch


def lifetime_percent():
  """ 
  calculates how much time in percents have passed
  lifetime_percent()-> str
  """
  ret = (weeks_since_birth() *100 ) / calc_all_weeks()
  return "{:.2f}".format(ret)
