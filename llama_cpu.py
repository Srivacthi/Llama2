from langchain_community.llms import LlamaCpp
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# Path to Llama model
MODEL_PATH = "/home/snadar2/llama/llama-2-7b.gguf.q8_0.bin"

# Creating a function to load Llama model
def load_model():
    """Loads Llama model"""
    # Creating callback
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
    Llama_model = LlamaCpp(
        model_path=MODEL_PATH,
        temperature=0.5,
        max_tokens=2000,
        top_p=1,
        callback_manager=callback_manager,
        verbose=True
    )

    return Llama_model
    
# Calling load_model()
llm = load_model()

# Adding model prompt
model_prompt: str = """
Question: Explain the purpose of data encryption in cyber security
"""

# Getting and printing response
response: str = llm.invoke(model_prompt)
print(response)

