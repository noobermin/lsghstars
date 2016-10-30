#!/usr/bin/env python3
'''
List stars. Optionally filter by tag or regex.

Usage: 
    lsst [options]
    lsst [options] filter <tag>...
    lsst [options] rx <regex>

Options:
    --all -a           Print a lot.
    --ALL -A           Print every fucking thing.
    --tags -t          Print tags.
    --fields=L -x L    Print these fields. Should be a
                       comma separated list. For a listing
                       of fields, see the json file.
    --description -d   Print descriptions.
    --stars=STARS      Path of stars file [default: stars.json]
'''
import json;
import pickle;
import re;
from misc import readtxt,take
def addto(e):
    pass;

if __name__ == "__main__":
    from docopt import docopt;
    opts = docopt(__doc__,help=True);
    stars = json.loads(readtxt(opts['--stars']));
    keys = opts['--fields'].split(',') if opts['--fields'] else []
    
    readtags = opts['--tags'] or opts['rx'] or opts['filter'];
    readtags = readtags or 'tags' in keys;

    if readtags:
        with open('tags.pi','rb') as f:
            tags=pickle.load(f);
        def gettag(star):
            if star['id'] in tags:
                star['tags'] = tags[star['id']]
            else:
                star['tags'] = [];
            return star;
        stars[:] = [gettag(star) for star in stars];
        if opts['filter']:
            stars = [ star for star in stars
                      if set(opts['<tag>']).issubset(star['tags']) ]
        elif opts['rx']:
            rx = re.compile('<regex>');
            def match(tags):
                for tag in tags:
                    if rx.match(tag):
                        return True;
                pass;
            stars = [ star for star in stars
                      if match(star['tags']) ];
        #now, convert "tags" to a string
        def tagstostr(star):
            star['tags']  = ','.join(star['tags']);
            return star;
        stars[:] = [tagstostr(star) for star in stars];
    if opts['--ALL']:
        pass;
    elif opts['--all']:
        keys = ['full_name','html_url','description'] + keys;
    elif not opts['--fields']:
        keys = ['full_name'];
    if opts['--tags'] and 'tags' not in keys: keys.append('tags');
    if opts['--description'] and 'description' not in keys:
        keys.append('description');
    stars = [ take(star,keys) for star in stars ];
    #tags
    for star in stars:
        for key in keys:
            print(star[key],end="\t");
        print("");
