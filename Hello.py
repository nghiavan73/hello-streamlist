# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#https://www.youtube.com/watch?v=vzlQkAzWCeI&ab_channel=Streamlit





import os
import streamlit as st
from streamlit.logger import get_logger


from llama_index.core import StorageContext,ServiceContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.node_parser import (SentenceSplitter)
import torch
from transformers import BitsAndBytesConfig
from llama_index.core.prompts import PromptTemplate
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.vector_stores.qdrant import QdrantVectorStore
import qdrant_client
from transformers import BitsAndBytesConfig

#from llama_index.core import VectorStoreIndex, SimpleDirectoryReader,Settings, StorageContext
#from llama_index.core import vector_stores

#from llama_index.vector_stores.chroma import ChromaVectorStore
#import chromadb
#from google.colab import userdata
#from IPython.display import Markdown, display

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to Streamlit!05/01/2024 NV3 👋")
    huggingFaceAPIKey = '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'

    with st.sidebar:
      st.title("Chatbot Prac")
      testHuggingFaceAPIKey = st.text_input("Enter Huggingface API token:", type="password")
      st.write(testHuggingFaceAPIKey)

    #st.sidebar.success("Chatbot Prac")
    os.environ["HUGGINGFACE_API_TOKEN"] = huggingFaceAPIKey
    if "messages" not in st.session_state:
      st.session_state.messages = [{"role":"assitant","content":"NV is here: How may I help you?"}]

    for message in st.session_state.messages:
      with st.chat_message(message["role"]):
        st.write(message["content"])

    def resetChatHistory():
      st.session_state.messages = [{"role":"assitant","content":"How may I help you?"}]

    def getResponse(promptInput):
      stringDialogue = "You are a helpful assitant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assitant'"
      for dictMessage in st.session_state.messages:
        if dictMessage["role"] == "user":
            stringDialogue += "User: " + dictMessage["content"] +"\n\n"
        else:
            stringDialogue += "Assitant:: " + dictMessage["content"] +"\n\n"
      outputString = "Need to query to get an answer from  LLM for this: " + str(promptInput)
      return outputString
    
    #User provided prompt
    #Python, the walrus operator is used " := " because it emits the value assigned to the it's surrounding context.
    if prompt := st.chat_input("Your message?"):
      promptMessage = {"role":"user","content":prompt}
      st.session_state.messages.append(promptMessage)
      with st.chat_message("user"):
        st.write(prompt)

    #Generate a new response if the last message is not from assistant
    if st.session_state.messages[-1]["role"] != "assitant":
      with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = getResponse(prompt)
            placeHolder = st.empty()
            fullResponse = ""
            for item in response:
                fullResponse +=item
            placeHolder.markdown(fullResponse)
      responseMessage = {"role":"assistant","content": fullResponse}
      st.session_state.messages.append(responseMessage)
    





    #st.markdown(
    #    """
    #    Streamlit is an open-source app framework built specifically for
    #    Machine Learning and Data Science projects.
    #    **👈 Select a demo from the sidebar** to see some examples
    #    of what Streamlit can do!
    #    ### Want to learn more?
    #    - Check out [streamlit.io](https://streamlit.io)
    #    - Jump into our [documentation](https://docs.streamlit.io)
    #    - Ask a question in our [community
    #      forums](https://discuss.streamlit.io)
    #    ### See more complex demos
    #   - Use a neural net to [analyze the Udacity Self-driving Car Image
    #      Dataset](https://github.com/streamlit/demo-self-driving)
    #    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    #"""
    #)


    



if __name__ == "__main__":
    run()
