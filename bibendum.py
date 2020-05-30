import string
from pathlib import Path

import markovify
from html2text import html2text


models = []


END = ['?', '!', '.']
TO_REMOVE = "↑" + string.punctuation
TRANSLATOR = str.maketrans({char: ' ' for char in TO_REMOVE if char not in END})


print("* read")
candidates = Path('./seed/').glob('*/*')
candidates = list(candidates)[:1000]
for index, path in enumerate(candidates):
    print("**", index, path)
    with open(str(path)) as f:
        html = f.read()
    text = html2text(html)
    clean = text.translate(TRANSLATOR)
    model = markovify.Text(clean)
    models.append(model)

print('* combine')
model = markovify.combine(models)
print('* compile')
model.compile()

print('* generate')
for i in range(5):
    print("** ", model.make_sentence())
