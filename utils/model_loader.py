######here exists code to load the model

#dependencies

import os
from dotenv import load_dorenv
from typing import Literal,optional,Any
from pydantic import BaseModel,Field
from utils.config_loader import load_config # its just a yaml loader 
from langchain_groq import chatGroq
from langchain_openai import chatOpenAI

class ConfigLoader:
    def __init__(self):
        print(f"loading config.....")
        self.config=load_config()
    def __getitem__(self,key):
        return self.config.get(key)






class ModelLoader(BaseModel):
    model_provider:Literal["groq","openai"] ="groq"
    config: optional[ConfigLoader] =Field(default=None,exclude=True)
    def model_post_init(self,__context: Any)->None:
        self.config = ConfigLoader()
    class Config:
        arbitary_types_alowed =True
        
    def load_llm(self):
        print("llm is loading")
        print(f"loading model from provider: {self.model_provider}")
        if self.model_provider=="groq":
            print("loading llm for m groq...............")
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name=self.config["llm"]["groq"]["model_name"]
            llm = chatGroq(model=model_name, api_key=groq_api_key)
        else: 
            self.model_provider=="openai":
            print("loading model from Openai........... ")
            openai_api_key=os.getenv("OPENAI_API_KEY")
            model_name=self.config["llm"]["openai"]["model_name"]
            llm = chatOpenAI(model=model_name, api_key=openai_api_key)
        return llm