from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

model_id = "facebook/blenderbot-400M-distill"
tokenizer = AutoTokenizer.from_pretrained(model_id, legacy = False)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
chatbot_pipeline = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

def use_pipeline(text):
  res = chatbot_pipeline(text)
  return res
