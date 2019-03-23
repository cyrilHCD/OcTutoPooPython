import json

class Agent:

    def __init__(self, **attr):
        for attribute_name, attribute_value in attr.items():
            setattr(self, attribute_name, attribute_value)
    
    def sayHello(self, str) :
        return "Hello " + str
def main():    
    for agents_attributes in json.load(open("agents-100k.json")):
        agent = Agent(**agents_attributes)
        print(agent.longitude)

main()

