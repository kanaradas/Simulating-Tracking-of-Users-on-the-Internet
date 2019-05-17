import simpy

class Website(object):
	def __init__(self, env):
		self.env = env
		self.action = env.process(self.run())
		
	def run(self):
		visits = 0
		while True:
			
			print('number of visits %d' % visits)
			
			try:
				yield self.env.timeout(50)
				print('done with wait')
			except simpy.Interrupt:
				
				visits = visits + 1
				
				
			#yield self.env.timeout(50)
