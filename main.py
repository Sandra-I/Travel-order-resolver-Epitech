import spacy


def get_cities(str):
  print (str)
  nlp = spacy.load("fr_core_news_lg")
  doc = nlp(str)
  ville = []
  for token in doc:
    # print(token.text, token.pos_, "         ", token.text, token.dep_, token.head.text)
    # print(token.text, token.dep_, token.head.text)
    if token.dep_ == 'case':
      # print(token.text, token.dep_, token.head.text)
      # print('pos: ', token.text)
      # print('city: ', token.head.text)
      ville.append([token.text, token.head.text])
  return(ville)
  #return (evaluate_trip(ville))

def evaluate_trip(ville):

  return(ville)

with open('database') as f:
   lines = f.readlines()
for line in lines:
  villes = get_cities(line)
  new_str =  str(villes)
  print(new_str + "\n")
  # f = open("database2.txt", "a")
  # f.write(line)
  # f.write(new_str)
  # f.close()
# ville = get_cities("J'aimerai partir de Lille pour arriver à Lyon.")