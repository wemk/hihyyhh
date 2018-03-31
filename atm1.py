Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> money = 500
>>> request = 277
>>> while request > 0 :
	if request > 100:
		request = request - 100
		print "give 100"
	elif request > 50:
		request = request -50
		print "give 50"
	elif request > 10:
		request=request-10
		print "give 10"
	elif request >5:
		request=request-5
		print 'give 5'
	else:
		request=request-2
		print 'give 2'

		
give 100
give 100
give 50
give 10
give 10
give 5
give 2
>>> 
