import spacy
import pandas as pd

nlp = spacy.load("pt_core_news_sm")

data = {'texto': ['rápido', 'rápida', 'Correndo','correr', 
                  'Andando','andar','Especialistas',
                  'especialista','excelente','excelência',
                  'dúvidas','dúvida']} 

df = pd.DataFrame(data)
df['texto'] = df['texto'].str.lower() 


def lematizar_texto(texto):
    doc = nlp(texto)
    return ' '.join([token.lemma_ for token in doc if token.is_alpha ]) 

df['texto_lemmatizado'] = df['texto'].apply(lematizar_texto) 



