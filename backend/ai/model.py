import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = "Qwen/Qwen3.5-0.8B"

# -------------------------
# Device selection (Apple Silicon)
# -------------------------
if torch.backends.mps.is_available():
    DEVICE = torch.device("mps")
else:
    DEVICE = torch.device("cpu")

# -------------------------
# Load tokenizer & model once
# -------------------------
tokenizer = AutoTokenizer.from_pretrained(
    MODEL_ID,
    trust_remote_code=True
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float16,
    device_map=None,
    trust_remote_code=True
)

model.to(DEVICE)
model.eval()

# -------------------------
# Inference function
# -------------------------
# def run_local_ai(prompt: str) -> str:
#     inputs = tokenizer(
#         prompt,
#         return_tensors="pt"
#     ).to(DEVICE)

#     with torch.no_grad():
#         output_ids = model.generate(
#             **inputs,
#             temperature = 0.2,
#             top_p = 0.9,
#             repetition_penalty = 1.2,
#             top_k = 20,
#             max_new_tokens=400,
#             do_sample=True,
#             eos_token_id=tokenizer.eos_token_id,
#         )

#     output_text = tokenizer.decode(
#         output_ids[0],
#         skip_special_tokens=True
#     )

#     return output_text[len(prompt):].strip()

def run_local_ai(prompt: str) -> str:
    inputs = tokenizer(
        prompt,
        return_tensors="pt"
    ).to(DEVICE)

    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=400,
            temperature=0.2,
            top_p=0.9,
            do_sample=True,
            eos_token_id=tokenizer.eos_token_id,
        )

    output_text = tokenizer.decode(
        output_ids[0],
        skip_special_tokens=True
    )

    # Return ONLY the generated part
    return output_text[len(prompt):].strip()