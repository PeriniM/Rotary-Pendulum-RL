from ..Environments import RealPendulumEnv as real
from ..Environments import PyBulletPendulumEnv as pb
from ..Environments import FakeEnv as fake
from ..DQN.Agent import Agent

isFake = False
isPyBullet = True
isReal = False

train = True
plot_colormaps = False

# select the environment
if isFake:
    env = fake.FakeEnv(1)
elif isPyBullet:
    env = pb.PyBulletPendulumEnv(render_mode='human')
elif isReal:
    env = real.RealPendulumEnv("COM3", 115200)
else:
    raise Exception("No environment selected!")

# create the agent
dqn_agent = Agent(env)

# train or evaluate the agent
if train:
    dqn_agent.train_model(render=True, plot=True, verbose=True, soft_start=False)
else:
    dqn_agent.evaluate_model(episodes=10, swingUp=False, render=True, verbose=True, final=False)

# plot the value function and policy
if plot_colormaps:
    dqn_agent.plot_value_policy('2D', resolution=50, final=False)