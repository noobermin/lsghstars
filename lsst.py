#!/usr/bin/env python3
'''
List stars.

Usage: 
    lsst [options]

Options:
    --all -a           Print a lot.
    --ALL -A           Print every fucking thing.
    --description -d  
    --full_name -f
    --url -u
    --tags -t          Print tags.
'''
import json;
import pickle;
from misc import readtxt,take
if __name__ == "__main__":
    from docopt import docopt;
    opts = docopt(__doc__,help=True);
    stars = json.loads(readtxt("stars.json"));
    def filter_keys(keys):
        return
    keys = [];
    if opts['--tags']:
        with open('tags.pi','rb') as f:
            tags=pickle.load(f);
        def gettag(star):
            if star['id'] in tags:
                star['tags'] = ",".join(tags[star['id']])
            else:
                star['tags'] = "";
            return star;
        stars[:] = [gettag(star) for star in stars];
    if opts['--ALL']:
        pass;
    elif opts['--all']:
        keys.extend(['full_name','url','description']);
    else:
        keys = ['full_name'];
    #tags go last
    if opts['--tags']: keys.append('tags');
    stars = [ take(star,keys) for star in stars ];
    #tags
    for star in stars:
        for key in keys:
            print(star[key],end="\t");
        print("");
