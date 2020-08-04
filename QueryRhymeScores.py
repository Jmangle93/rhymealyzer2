import datamuse

api = datamuse.Datamuse()

dummy_rhymes = api.words(rel_rhy='dummy', max=10)

val = '...'
for match in dummy_rhymes:
    val += 'FOUND' if 'mummy' == match['word'] else ''

print(val)
