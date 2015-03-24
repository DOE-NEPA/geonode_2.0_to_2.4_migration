def get_django_content_type_id(id):
  if id == 10:
    return 67
  if id == 12:
    return 17
  if id == 17:
    return 23
  if id == 52:
    return 64
  if id == 25:
    return 65
  if id == 42:
    return 44
  if id == 59:
    return 68
  if id == 18:
    return 24
  if id == 60:
    return 69
  if id == 58:
    return 70
  if id == 53:
    return 71
  if id == 19:
    return 25
  if id == 54:
    return 72
  if id == 32:
    return 32
  if id == 4:
    return 3
  if id == 26:
    return 66
  if id == 50:
    return 48
  if id == 15:
    return 21
  if id == 16:
    return 22
  if id == 51:
    return 63
  if id == 49:
    return 73
  if id == 2:
    return 2
  if id == 41:
    return 41
  if id == 39:
    return 39
  if id == 7:
    return 6
  if id == 45:
    return 45
  if id == 46:
    return 46
  if id == 29:
    return 30
  if id == 11:
    return 74
  if id == 24:
    return 75
  if id == 23:
    return 76
  if id == 22:
    return 77
  if id == 47:
    return 78
  if id == 20:
    return 26
  if id == 1:
    return 1
  if id == 31:
    #<class 'psycopg2.IntegrityError'>
	#duplicate key value violates unique constraint "django_content_type_app_label_model_key"
	#DETAIL:  Key (app_label, model)=(people, profile) already exists.
	#select id, name, app_label, model from django_content_type
	#(31, 'profile', 'people', 'profile')
    return 3
  if id == 21:
    return 27
  if id == 35:
    return 35
  if id == 38:
    return 38
  if id == 36:
    return 36
  if id == 30:
    return 80
  if id == 5:
    return 4
  if id == 13:
    return 18
  if id == 14:
    return 20
  if id == 6:
    return 5
  if id == 34:
    return 34
  if id == 40:
    return 40
  if id == 55:
    return 81
  if id == 8:
    return 7
  if id == 56:
    return 82
  if id == 9:
    return 8
  if id == 27:
    return 28
  if id == 37:
    return 83
  if id == 33:
    return 33
  if id == 43:
    return 57
  if id == 44:
    return 58
  if id == 3:
    return 31
  if id == 48:
    return 0
  if id == 28:
    return 29
  if id == 57:
    return 84

  return None
  