#%%

from transformers import AutoTokenizer, AutoModelForCausalLM
    
tokenizer = AutoTokenizer.from_pretrained("model_name")
model = AutoModelForCausalLM.from_pretrained("model_name")

model
#%%


import sys
from   langchain.llms import LlamaCpp

verbose = False

llm = LlamaCpp(
    model_path="/home/chris/MODELS/synthia-7b-v2.0-16k.Q4_K_M.gguf",
    n_ctx=4096,
    n_gpu_layers=32,
    n_batch=1024,
    f16_kv=True,
    verbose=verbose,
)

while True:
    question = input("Ask me a question: ")
    if question == "stop":
        sys.exit(1)
    output = llm(
        question,
        max_tokens=4096,
        temperature=0.2,
        top_p=0.1
    )
    print(f"\n{output}") 