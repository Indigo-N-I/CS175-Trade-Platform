from src.agent.agent_thread import agent_thread
from src.util.util import *

# This is a very simple Agent, it will buy any time possible
# and sell if the current price is higher than buy-in price
class tcn_agent(agent_thread):
    def __init__(self):
        agent_thread.__init__(self)

        self.holding_time = 0
