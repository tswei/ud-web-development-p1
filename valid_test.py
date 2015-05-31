import unittest

def valid_month(month):
	months = ['January',
			  'February',
			  'March',
			  'April',
			  'May',
			  'June',
			  'July',
			  'August',
			  'September',
			  'November',
			  'December']
	
	mon_dict = dict((m[:3],m) for m in months)
	if month and (len(month) >= 3):
		month = month.capitalize()[:3]
		return mon_dict.get(month)

def valid_day(day):
	if day.isdigit() and int(day) in range(1,32):
		return int(day)
		
def valid_year(year):
	if year.isdigit() and int(year) in range(1900, 2021):
		return int(year)

def test_all():
	#test valid_month
	valid_month("January") == "January"
	valid_month("feb") == "February"
	valid_month("") == None
	valid_month("foo")== None
		
	#test valid_day
	valid_day("1") == 1
	valid_day("31") == 31
	valid_day("0") == None
	valid_day("one") == None
	valid_day("") == None
	
	#test valid_year
	valid_year("111") == None
	valid_year("ninteen-hundred") == None
	valid_year("") == None
	valid_year("1900") == 1900
	valid_year("2020") == 2020
	
	return "All Tests Pass"
	
print test_all()