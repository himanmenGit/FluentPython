from a5.tag import tag

print(tag)

from functools import partial

picture = partial(tag, 'img', cls='pic-frame')

picture(src='wumpis.jpeg')
print(picture)
print(picture.func)
print(picture.args)
print(picture.keywords)