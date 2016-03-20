#!/usr/bin/env python3
'''
Tag a star. Either use a simple search string to match
full_name, or a regex to match full_name. Adds tags to
all matching unless passed the --last flag.

Usage:
    ./tag.py [options] <search> <tag>...
    ./tag.py [options] (--regex|-r) <regex> <tag>...

Options:
     --help              What do you think?
     --regex -r          Tag all full_names that match regex.
     --verbose -v        Make some noise.
     --last -1           Only add to the last.
     --undo -u           Untag something.
'''
import json;
from misc import readtxt,take;
import re;
import pickle;
import os;
if __name__ == "__main__":
    from docopt import docopt;
    opts = docopt(__doc__,help=True);
    stars = json.loads(readtxt("stars.json"));
    if opts['--regex']:
        rx = re.compile(opts['<regex>']);
        matches = [ star['id'] for star in stars
                    if rx.match(star['full_name']) ];
    else:
        matches = [ star['id'] for star in stars
                    if opts['<search>'] in star['full_name'] ];
    # The tag file is super complicated
    # omg, u have no idea
    # this is probably very inefficient though...
    if os.path.isfile('tags.pi'):
        with open('tags.pi','rb') as f:
            d = pickle.load(f);
    else:
        d={}
    for i in matches:
        if i not in d: d[i]=set()
        for tag in opts['<tag>']:
            if not opts['--undo']:
                d[i].add(tag);
            else:
                d[i].remove(tag);
    with open('tags.pi',"wb") as f:
        pickle.dump(d,f);
