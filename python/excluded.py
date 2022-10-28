import os

old = '/Users/josh/Dropbox/Coding/Github/blog/words'

old = os.listdir(old)

new = '/Users/josh/Dropbox/Coding/Github/sk-blog/words/'

new = os.listdir(new)

not_in = [x for x in old if x not in new]

['fish-that-ate-the-whale.md', 'tesla-is-finding-the-limits-of-naive-innovation.md', 
'why-nations-fail.md', 'isaac-newton.md', 'informing-the-news.md', 'are-barriers-worth-it.md', 
'primed-for-determinism.md', 'year-without-pants.md', 'there-is-a-limit-to-your-creative-potential.md', 
'words.json', 'the-ascent-of-money.md', 'muhammad.md',
 'the-accidental-billionares.md', 'what-happened-to-the-dynamism-of-religions.md']

print(not_in)