#!/usr/bin/env python
"""
Pandoc filter to convert code blocks with class "figure" to LaTeX
"""

from pandocfilters import toJSONFilter, CodeBlock, RawBlock, RawInline

def latex(code):
    """LaTeX inline"""
    return RawInline('latex', code)

def latexblock(code):
    """LaTeX block"""
    return RawBlock('latex', code)

def textfigure(key, value, fmt, meta):
	if key == 'CodeBlock':
		[[ident, classes, kvs], contents] = value
		kvs = {key: value for key, value in kvs}
		if "figure" in classes:
			if ident == "":
				label = ""
			else:
				label = '\n\\label{' + ident + '}'
			return [latexblock(
                "\n\\onehalfspacing" +
                "\n\\begin{quote}\n" + 
                contents + 
                "\n\\end{quote}" +
                label +
                "\n\\end{figure}" +
                "\n\\doublespacing" 
                )]
	else:
		return None

if __name__ == "__main__":
    toJSONFilter(textfigure)


# \begin{figure}[htbp]
#   \begin{quote}
#     Part A: Introduction, Variation 1, Variation 2\\
#     Part B: Variation 3 and Variation 4\\
#     Part C: Variation 5\\
#     Part D: Variation 6 and Variation 7
  
# \caption{\emph{Wald} formal groupings.}\label{fig:walden-formal-groupings}
# \end{figure}

# \doublespacing