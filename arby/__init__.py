# __init__.py

__version__ = "0.1a1"

from .integrals import Integration
from .greedy import ReducedOrderModeling, GramSchmidt

__all__ = [Integration, ReducedOrderModeling, GramSchmidt]
