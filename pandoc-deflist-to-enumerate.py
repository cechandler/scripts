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

begin_row = [pf.RawBlock('html', '<div class="row mb-2">')]
begin_term_column = [pf.RawBlock('html', '<div class="col-2">')]
begin_definition_column = [pf.RawBlock('html', '<div class="col-10">')]
end_div = [pf.RawBlock('html', '</div>')]
begin_definition_para = [pf.RawBlock('html', '<p class="mb-0">')]
end_definition_para = [pf.RawBlock('html', '</p>')]

def list2items(key, val, fmt, meta):
    if 'DefinitionList' != key:
        return None
    elif fmt == "latex":
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
    elif fmt == "html":
        output = [pf.RawBlock('html', "<div></div>")]
        for pair in val:
            (term, definitions) = pair
            output += begin_row + begin_term_column + [pf.Plain(term)] + end_div
            output += begin_definition_column
            for definition in definitions:
                output += begin_definition_para + definition + end_definition_para
            output += end_div
            output += end_div
        return output

# <div class="row">
#   <div class="col-2">2017</div>
#   <div class="col-10">
#     <p class="mb-0">Ph.D. in Composition, Eastman School of Music, Rochester, NY</p>
#     <p class="mb-0"><em>Studied with:</em> Robert Morris, Carlos Sanchez-Gutierrez, Ricardo Zohn-Muldoon</p>
#     <p class="mb-0"><em>Dissertation:</em> Recontextualization and Variation: Associative Organization in Hans Abrahamsen's <em>Walden</em> and <em>Wald</em></p>
#   </div>
# </div>


# def filter_func(key, val, fmt, meta):
#     if 'Div' != key:
#         return None
#     if not 'enumerate' in val[0][1]:
#         return None
#     return pf.walk(val[-1], list2items, fmt, meta)


if __name__ == "__main__":
    pf.toJSONFilter(list2items)
