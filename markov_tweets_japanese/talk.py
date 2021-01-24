import markovify

def make_sentences(json, max=70, min=20, tries=100):
    text = markovify.Text.from_json(json)
    for _ in range(tries):
        sentence = str(text.make_sentence()).replace(' ', '')
        if sentence and len(sentence) <= max and len(sentence) >= min:
            return sentence


with open('model/ruta.json') as f:
    markov_json = f.read()

sentence = make_sentences(markov_json)
print(sentence)