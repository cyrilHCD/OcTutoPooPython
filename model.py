class Agent:

    def __init__(self, agreeableness):
        self.agreeableness = agreeableness
    
    def sayHello(self, str) :
        return "Hello " + str
ag = Agent(1)
print(ag.agreeableness)
