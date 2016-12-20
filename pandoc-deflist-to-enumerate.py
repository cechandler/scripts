#!/usr/bin/env python

"""
Pandoc filter for transforming a definition list into an enumerate
environment.

By default, all definition lists are transformed. If there's a need
to be selective, uncomment the filter_func at the bottom so that
transformed definition lists will need to be wrapped in a Div with
a class of "enumerate".
"""

import pandocfilters as pf
import sys

# Reusable document elements
begin_enumerate = [pf.RawBlock('latex', '\\begin{enumerate}')]
end_enumerate = [pf.RawBlock('latex', '\\end{enumerate}')]
begin_item = [pf.RawInline('latex', '\\item[')]
end_item = [pf.RawInline('latex', '] ')]

def list2items(key, val, fmt, meta):
    if 'DefinitionList' != key:
        return None
    return_list = list(begin_enumerate)  # clone
    for pair in val:
        (term, definitions) = pair
        # construct \item[term]
        item = begin_item + term + end_item
        # prepend \item[term] to (first) definition
        # get first para in first definition
        block = definitions[0][0]
        # check that it really is a para (or plain) or bail out
        if not isinstance(block, dict) or not block['t'] in ('Para', 'Plain'):
            sys.stderr.write(
                "Topic definitions must be plain paragraphs, not {0}!\n".format(block['t']))
            sys.exit(255)
        # the actual prepending
        block['c'] = item + block['c']
        # each definition is a list of blocks
        # merge each of them into the return list
        for definition in definitions:
            return_list = return_list + definition
    # append \end{enumerate} to the return list and return it
    return return_list + end_enumerate


# def filter_func(key, val, fmt, meta):
#     if 'Div' != key:
#         return None
#     if not 'enumerate' in val[0][1]:
#         return None
#     return pf.walk(val[-1], list2items, fmt, meta)


if __name__ == "__main__":
    pf.toJSONFilter(list2items)
