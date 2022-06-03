from pydoc import cli

import requests
import json

class Queue:
	elements=[]
	def __init__(self):
		self.elements=[]

	def enqueue(self, data):
		self.elements.append(data)
		return data

	def dequeue(self):
		return self.elements.pop(0)

	def rear(self):
		return self.elements[-1]

	def front(self):
		return self.elements[0]

	def is_empty(self):
		return len(self.elements) == 0

# if __name__ == '__main__':
#
# 	queue = Queue()
#
# 	## checking is_empty method -> True
# 	print(queue.is_empty())
#
# 	## adding the elements
# 	queue.enqueue(1)
# 	queue.enqueue(2)
# 	queue.enqueue(3)
# 	queue.enqueue(4)
# 	queue.enqueue(5)
#
# 	## again checking is_empty method -> False
# 	print(queue.is_empty())
#
# 	## printing the front and rear elements using front and rear methods respectively -> 1, 5
# 	print(queue.front(), end=' ')
# 	print(queue.rear())
#
# 	## removing the element -> 1
# 	queue.dequeue()
#
# 	## checking the front and rear elements using front and rear methods respectively -> 2 5
# 	print(queue.front(), end=' ')
# 	print(queue.rear())
#
# 	## removing all the elements
# 	queue.dequeue()
# 	queue.dequeue()
# 	queue.dequeue()
# 	queue.dequeue()
#
# 	## checking the is_empty method for the last time -> True
# 	print(queue.is_empty())

# =================================================================  Task 2 ======== =====================================================================================
class QueueOutOfRangeException(Exception):
    # """Exception raised for errors in the input salary.
    def __init__(self, length, message="Max Length is 5 "):
        self.length = length
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.length} -> {self.message}'

class Child_Queue:
	def __init__(self, name, size):
		super(Child_Queue, self).__init__()
		self.name = name
		self.size=size

	def enqueue(self, data):
		if len(Queue.elements) <=self.size:
			Queue.elements.append(data)
			return data
		else:
			raise QueueOutOfRangeException(self.size)

	def dequeue(self):
		return Queue.elements.pop(0)

	def rear(self):
		return Queue.elements[-1]

	def front(self):
		return Queue.elements[0]

	def is_empty(self):
		return len(Queue.elements) == 0
	def save(self,instance):
		f_instances = open("instances.txt", "a")
		f_instances.write(instance + "\n")
		print("Saved Successfully ! \n")
		print("Your Data : \t \t ", instance)
		f_instances.close()
	def load(self):
		f_instances = open("instances.txt", "r")
		lines = f_instances.readlines()
		for line in lines:
			print(line)


# queue = Queue()

child=Child_Queue("child1",5);

# save in file
child.save("child1")

# read from file
child.load()

# checking is_empty method -> True
print(child.is_empty())

## adding the elements
child.enqueue(1)
child.enqueue(2)
child.enqueue(3)
child.enqueue(4)
child.enqueue(5)

## again checking is_empty method -> False
print(child.is_empty())

## printing the front and rear elements using front and rear methods respectively -> 1, 5
print(child.front(), end=' ')
print(child.rear())

## removing the element -> 1
child.dequeue()

## checking the front and rear elements using front and rear methods respectively -> 2 5
print(child.front(), end=' ')
print(child.rear())

## removing all the elements
child.dequeue()
child.dequeue()
child.dequeue()
child.dequeue()

## checking the is_empty method for the last time -> True
print(child.is_empty())

# ===============================================   Task 3  =============================================================

class client_api:
	def __init__(self,api_key,base_url):
		self.api_key=api_key
		self.base_url=base_url
	def get_current_temperature(self,city):
		response = requests.get(self.base_url + self.api_key + "&q=" + self.city + "&aqi=no")
		print(response.json()["current"])
	def get_temperature_after(self,city, days, hour=None):
		response = requests.get(f'{self.base_url_forecast}?key={self.api_key}&q={city}&days={self.days}&aqi=no&alerts=no')
		print(response.json())
	def get_lat_and_long(self,city):
		response = requests.get(self.base_url + self.api_key + "&q=" + self.city + "&aqi=no")
		print(f'lat : {response.json()["location"]["lat"]} , lon:{response.json()["location"]["lon"]}')



api_key= "e94c7dee14ae43db8fa122633220306"
base_url = "http://api.weatherapi.com/v1/current.json?key="
base_url_forecast="http://api.weatherapi.com/v1/forecast.json?key=e94c7dee14ae43db8fa122633220306&q=Cairo&days=1&aqi=no&alerts=no"

def get_current_temperature(city):
	response = requests.get(base_url+api_key+"&q="+city+"&aqi=no")
	print(response.json()["current"])

def get_temperature_after(city, days, hour=None):
	response = requests.get(f'{base_url_forecast}?key={api_key}&q={city}&days={days}&aqi=no&alerts=no')
	print(response.json())

def get_lat_and_long(city):
	response = requests.get(base_url + api_key + "&q=" + city + "&aqi=no")
	print(f'lat : {response.json()["location"]["lat"]} , lon:{response.json()["location"]["lon"]}')

# get_current_temperature("Cairo")
# get_temperature_after("cairo","1")
# get_lat_and_long("cairo")












