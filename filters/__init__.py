# image_processing_package/filters/__init__.py
# Este arquivo torna a pasta 'filters' um submódulo do pacote

__all__ = ['grayscale', 'blur', 'edge_detection']

from . import grayscale
from . import blur
from . import edge_detection