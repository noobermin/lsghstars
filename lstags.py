#!/usr/bin/env python3
'''
Just list tags. Quicker than a filter and pipe through uniq.

Usage: 
    lstags [options]

Options:
    --help -h          What do you think?
'''
import pickle;

if __name__ == "__main__":
    from docopt import docopt;
    with open('tags.pi','rb') as f:
        tagsd=pickle.load(f);
    acc = set().union(*(tagsd[k] for k in tagsd))
    for tag in acc:
        print(tag);

