import simpy

class User(object):
	def __init__(self, env, website):
		self.env = env
		self.action = env.process(self.run())
		self.website = website
		
	def run(self):
		while True:
			print('went to website at %d' % self.env.now)
			self.website.action.interrupt()
			wait_duration = 5
			yield self.env.timeout(wait_duration)
			
			print('went to website 2 at %d' % self.env.now)
			wait_duration2 = 2
			yield self.env.timeout(wait_duration2)
