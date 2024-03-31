from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

model_id = "cardiffnlp/twitter-roberta-base-sentiment-latest"
tokenizer = AutoTokenizer.from_pretrained(model_id, legacy = False)
model = AutoModelForSequenceClassification.from_pretrained(model_id)
pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

def use_pipeline(text):
  res = pipeline(text)
  return res
