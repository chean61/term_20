## Team Members

- **이채안** (Team Leader)  
  - Project setup and repository management  
  - Overall integration and final submission  

- **고준원**  
  - README documentation improvement  

- **배주현**  
  - Negative sentiment example creation  

- **안세은**
  - Positive sentiment example creation 

## Notes on Sentiment Analysis

This project uses an English-based pretrained sentiment analysis model 
(`distilbert-base-uncased-finetuned-sst-2-english`) provided by Hugging Face.

Since the model is trained primarily on short English movie review sentences,
it performs most reliably when the input text is concise and evaluation-focused.

When analyzing non-English texts (e.g., Korean lecture reviews), shorter and 
clearly positive or negative sentences tend to produce more stable and 
interpretable results than long, descriptive paragraphs.  
This is because long sentences may include mixed sentiments or contextual 
information that the model was not specifically trained to handle.

Therefore, for demonstration and testing purposes, this project uses 
simple, single-sentence examples to clearly illustrate the behavior and 
limitations of the sentiment analysis model.
