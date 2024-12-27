class Car:
	def __init__(self):
		print('happy na!')
	
	def __del__(self):
		print('dist of car')
class Bike:
	def __init__(self):
		print('this is bike const ')
		
	def __del__(self):
		print('this is dist of bike ')
		
		
x,y,z,a,b,c = Car(),Car(),Car(),Car(),Car(),Car()


p,q,r,s	 = Bike(),Bike(),Bike(),Bike()
