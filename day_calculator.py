import datetime
import sys

SCHOOL = "school"
NOT_SCHOOL = "not-school"

def calculate_day_type(date):
	sDay = datetime.datetime(2020, 7, 20)
	x = [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0 ,0 ,0 , 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0]	
	
	delta = date - sDay
	
	if (delta.days < 28):
		if (x[delta.days]) == 1:
			return SCHOOL
		else:
			return NOT_SCHOOL
	else:
		if (x[(delta.days-28)]) == 1:
			return SCHOOL
		else:
			return NOT_SCHOOL
