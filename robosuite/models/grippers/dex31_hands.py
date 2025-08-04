"""
Dexterous hands for GR1 robot.
"""
import numpy as np

from robosuite.models.grippers.gripper_model import GripperModel
from robosuite.utils.mjcf_utils import xml_path_completion


class Dex31LeftHand(GripperModel):
    """
    Dexterous left hand of G1 robot

    Args:
        idn (int or str): Number or some other unique identification string for this gripper instance
    """

    def __init__(self, idn=0):
        super().__init__(xml_path_completion("grippers/dex31_left_hand.xml"), idn=idn)

    def format_action(self, action):
        # the more correct way is to add <equality> tag in the xml
        # however the tag makes finger movement laggy, so manually copy the value for finger joints
        # 0 is thumb rot, no copying. Thumb bend has 3 joints, so copy 3 times. Other fingers has 2 joints, so copy 2 times.
        assert len(action) == self.dof
        action = np.array(action)
        indices = np.array([0, 1, 2, 3, 4, 5, 6])
        #indices = np.array([0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5])
        return action[indices]

    @property
    def init_qpos(self):
        return np.array([0.0] * 7)
        #return np.array([0.0] * 12)

    @property
    def grasp_qpos(self):
        return {
            -1: np.array([0, 0, 0, 0, 0, 0, 0]),  # open
            1: np.array([1, 1, 1, 1, -1, -1, 0]),  # close
            # -1: np.array([-1.5, -1.5, -1.5, -1.5, -3, 3]),  # open
            # 1: np.array([1.5, 1.5, 1.5, 1.5, 3, 3]),  # close
            # -1: np.array([-1.5, -1.5, -1.5, -1.5, -3, 3]),  # open
            # 1: np.array([1.5, 1.5, 1.5, 1.5, 3, 3]),  # close
        }

    @property
    def speed(self):
        return 0.01

    @property
    def dof(self):
        return 7
        #return 6

    @property
    def _important_geoms(self):
        return {
            "left_finger": [
                "left_hand_thumb_0_link",
                "left_hand_thumb_1_link",
                "left_hand_thumb_2_link",
            ],
            "right_finger": [
                "left_hand_middle_0_link",
                "left_hand_middle_1_link",
                "left_hand_index_0_link",
                "left_hand_index_1_link",
            ],
            "left_fingerpad": [
                "left_hand_thumb_0_link",
                "left_hand_thumb_1_link",
                "left_hand_thumb_2_link",
            ],
            "right_fingerpad": [
                "left_hand_middle_0_link",
                "left_hand_middle_1_link",
                "left_hand_index_0_link",
                "left_hand_index_1_link",
            ],
        }


class Dex31RightHand(GripperModel):
    """
    Dexterous right hand of G1 robot

    Args:
        idn (int or str): Number or some other unique identification string for this gripper instance
    """

    def __init__(self, idn=0):
        super().__init__(xml_path_completion("grippers/dex31_right_hand.xml"), idn=idn)

    def format_action(self, action):
        # the more correct way is to add <equality> tag in the xml
        # however the tag makes finger movement laggy, so manually copy the value for finger joints
        # 0 is thumb rot, no copying. Thumb bend has 3 joints, so copy 3 times. Other fingers has 2 joints, so copy 2 times.
        assert len(action) == self.dof
        action = np.array(action)
        indices = np.array([0, 1, 2, 3, 4, 5, 6])
        #indices = np.array([0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5])
        return action[indices]

    @property
    def init_qpos(self):
        return np.array([0.0] * 7)
        #return np.array([0.0] * 12)

    @property
    def grasp_qpos(self):
        return {
            -1: np.array([0, 0, 0, 0, 0, 0, 0]),  # open
            1: np.array([1, 1, 1, 1, -1, -1, 0]),  # close
            # -1: np.array([1.5, 1.5, 1.5, 1.5, 3, 3]),  # open
            # 1: np.array([-1.5, -1.5, -1.5, -1.5, -3, 3]),  # close
            # -1: np.array([-1.5, -1.5, -1.5, -1.5, -3, 3]),  # open
            # 1: np.array([1.5, 1.5, 1.5, 1.5, 3, 3]),  # close
        }

    @property
    def speed(self):
        return 0.01

    @property
    def dof(self):
        return 7
        #return 6

    @property
    def _important_geoms(self):
        return {
            "left_finger": [
                "right_hand_thumb_0_link",
                "right_hand_thumb_1_link",
                "right_hand_thumb_2_link",
            ],
            "right_finger": [
                "right_hand_middle_0_link",
                "right_hand_middle_1_link",
                "right_hand_index_0_link",
                "right_hand_index_1_link",
            ],
            "left_fingerpad": [
                "right_hand_thumb_0_link",
                "right_hand_thumb_1_link",
                "right_hand_thumb_2_link",
            ],
            "right_fingerpad": [
                "right_hand_middle_0_link",
                "right_hand_middle_1_link",
                "right_hand_index_0_link",
                "right_hand_index_1_link",
            ],
        }
    
