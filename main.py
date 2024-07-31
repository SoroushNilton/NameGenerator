#%%
words = open('names.txt', 'r').read().splitlines()
# %%
words[:10]
# %%
len(words)
# %%
min(len(word) for word in words)
# %%
max(len(words) for word in words)
# %%
max(words, key=len)
# %%
b = {}
for word in words:
    chs = ['<S>'] + list(word) + ['<E>']
    for ch1, ch2 in zip(chs, chs[1:]):
        bigram = (ch1, ch2)
        b[bigram] = b.get(bigram, 0) + 1
        # print(ch1, ch2)
# %%
b
# %%
sorted(b.items(), key= lambda kv: kv[1], reverse=True)
# sorted(b.items(), key= lambda kv: -kv[1]) # this and the one above are similar

# %%
import torch

N = torch.zeros((28, 28), dtype= torch.int32)

# %%
all_letters = sorted((list(set(''.join(words)))))
all_letters
# %%
stoi = {ch: i for i, ch in enumerate(all_letters)}
# itos = {i: ch for i, ch in enumerate(all_letters)}
# %%

# %%
