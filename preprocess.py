from tokenizer import split_into_sentences
from reynir import Greynir

g = Greynir()
count = 0

with open("islensk_wiki_lemmad.txt", 'w+', encoding='utf8') as out:
    with open("islensk_wiki_gogn.txt", encoding='utf8') as f:
        for sent in split_into_sentences(f):
            try:
                sent = g.parse_single(sent)
                if sent.tree != None:
                    for t in sent.terminals:
                        if t.lemma == ".":
                            out.write(t.lemma+'\n')
                        else:
                            out.write(t.lemma+" ")
                else:
                    count += 1
            except TypeError:
                count += 1
            except AttributeError:
                count += 1


print(count)
