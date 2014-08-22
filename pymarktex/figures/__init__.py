# Futures #
from __future__ import division

# Built-in modules #

# Internal modules #
from pymarktex import Template

# Third party modules #

###############################################################################
class LatexFigure(Template):
    def check(self):
        if self.path.count('.') > 1:
            raise Exception("Can't have several extension in a LaTeX file path.")

###############################################################################
class ScaledFigure(LatexFigure):
    """A figure in latex code which can have its size adjusted"""

    def __repr__(self): return '<%s object on %s>' % (self.__class__.__name__, self.parent)

    def __init__(self, path, caption, label=None, **kwargs):
        # Attributes #
        self.path, self.caption = path, caption
        self.label = r"\label{" + label + "}\n" if label is not None else ''
        self.kwargs = kwargs
        self.check()

    def path(self): return self.path
    def caption(self): return self.caption
    def label(self): return self.label
    def graph_params(self):
        params = list('%s=%s' % (k,v) for k,v in self.kwargs.items())
        params += ['keepaspectratio']
        return ','.join(params)

###############################################################################
class DualFigure(LatexFigure):
    """A figure in latex code which has two subfigures"""

    def __repr__(self): return '<%s object on %s>' % (self.__class__.__name__, self.parent)

    def __init__(self, path_one, path_two, caption_one, caption_two, label_one, label_two, caption_main, label_main):
        # Attributes #
        self.path_one, self.path_two = path_one, path_two
        self.caption_one, self.caption_two = caption_one, caption_two
        self.label_one = r"\label{" + label_one + "}\n" if label_one is not None else ''
        self.label_two = r"\label{" + label_two + "}\n" if label_two is not None else ''
        self.caption_main = caption_main
        self.label_main = r"\label{" + label_main + "}\n" if label_main is not None else ''
        # Check #
        if self.path_one.count('.') > 1 or self.path_two.count('.') > 1:
            raise Exception("Can't have several extension in a LaTeX file path.")

    def path_one(self): return self.path_one
    def path_two(self): return self.path_two
    def caption_one(self): return self.caption_one
    def caption_two(self): return self.caption_two
    def label_one(self): return self.label_one
    def label_two(self): return self.label_two
    def caption_main(self): return self.caption_main