import os
import sys
import numpy as np

import gymnasium as gym

import robosuite  # noqa: F401
sys.path.append('/home/hogun/Desktop/robocasa_g1')
import robocasa  # noqa: F401
from robocasa.utils.gym_utils import GrootRoboCasaEnv  # noqa: F401

# import sys
# sys.path.append('/home/hogunkee/robocasa-gr1-tabletop-tasks')

env_id = 'g1_unified/PnPCupToDrawerClose_G1ArmsAndWaistFourierHands_Env'
env = gym.make(env_id, enable_render=True)
print(env)