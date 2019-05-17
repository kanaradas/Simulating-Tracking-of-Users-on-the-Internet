import simpy
from user import User
from website import Website

#env = simpy.Environment()

#realuser = User(env)
#env.process(User(env))

#env.run(until=15)

env = simpy.Environment()
website1 = Website(env)
user1 = User(env,website1)

env.run(until=15)
