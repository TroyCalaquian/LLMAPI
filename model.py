from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

model_id = "facebook/blenderbot-400M-distill"
tokenizer = AutoTokenizer.from_pretrained(model_id, legacy = False)
model = AutoModelForSequenceClassification.from_pretrained(model_id)
chatbot_pipeline = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

def use_pipeline(text):
  res = chatbot_pipeline(text)
  return res
