from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT
from langgraph.graph import StatedGraph,MessageState,END,START
from langgraph.prebuilt import ToolNode,tools_condition



class GraphBuilder():
    def __init__(self):
        self.tools=[
            #weatherinfotool(),
            #placesearchtool(),
            #calculatortool(),
            #currencyconvertertool()
        ]
        self.system_prompt = SYSTEM_PROMPT

    def agent_function(self,state): # it will make decision
        """
        This function will analyze the current state and make a decision
        based on the available tools and user input.
        """
        user_question=state("messages")
        input_question=[self.system_prompt]+user_question
        response = self.llm_with_tools.invoke(input_question)
        return{"messages" : response}

    def build_graph(self):
        graph_builder = StatedGraph(MessageState)
        
        graph_builder.add_node("agent", self.agent_function)
        graph_builder.add_node("tools",ToolNode(tools=self.tools))
        graph_builder.add_edge(START,"agent")
        graph_builder.add_conditional_edges("agent", tools_condition)
        graph_builder.add_edge("tools","agent")
        graph_builder.add_edge("agent",END)

        self.graph = graph_builder.compile()
        return self.graph


        
        
        
    def __call__(self):
        pass