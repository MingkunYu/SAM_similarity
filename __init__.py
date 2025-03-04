from .node import *
from .install import *

NODE_CLASS_MAPPINGS = {
    'SAMModelLoader (segment anything)': SAMModelLoader,
    'SAMSimilarity (segment anything)': SAMSimilarity,
    'InvertMask (segment anything)': InvertMask,
    "IsMaskEmpty": IsMaskEmptyNode,
}

__all__ = ['NODE_CLASS_MAPPINGS']


