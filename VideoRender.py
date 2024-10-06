from TetrisBattle.envs.tetris_env import TetrisDoubleEnv
from CustomAgent import Agent
import cv2
import numpy as np
import pandas as pd

class VideoRender():

    def __init__(self) -> None:
        pass

    def render(self, agent1, agent2, agent1_name=None, agent2_name=None, link = 'outpy.webm', fps = 100):

        agent_list = [agent1, agent2]
        env = TetrisDoubleEnv(gridchoice="none", obs_type="grid", mode="rgb_array")
        done = False
        state = env.reset(name1=agent1_name, name2=agent2_name)

        imgs = []

        while not done:
            img = env.render(mode='rgb_array') # img is rgb array, you need to render this or can check my colab notebook in readme file
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            imgs.append(img)
            action = agent_list[env.game_interface.getCurrentPlayerID()].choose_action(state)
            state, reward, done, _ = env.step(action)
            env.take_turns()
        
        # out = cv2.VideoWriter(link,cv2.VideoWriter_fourcc(*'DIVX'), fps, (800,600))
        # out = cv2.VideoWriter(link,cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, (800,600))
        # out = cv2.VideoWriter(link,cv2.VideoWriter_fourcc('M', 'P', 'E', 'G'), fps, (800,600))
        # out = cv2.VideoWriter(link,cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, (800,600))
        out = cv2.VideoWriter(link,cv2.VideoWriter_fourcc('V', 'P', '8', '0'), fps, (800,600))
        # out = cv2.VideoWriter(link,cv2.VideoWriter_fourcc('h', '2', '6', '4'), fps, (800,600))
        # out = cv2.VideoWriter(link,cv2.VideoWriter_fourcc('X', '2', '6', '4'), fps, (800,600))
        for img in imgs:
            cv2.imwrite('img.jpg',img)
            out.write(img)
        out.release()

        with open(link[:-4] + 'txt', 'w') as file:
            file.write(str(_['winner']) + '\n')

        # cv2.destroyAllWindows()

        return link
