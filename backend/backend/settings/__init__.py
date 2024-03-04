from backend.settings.django import *
from backend.settings.drf import *

try:
    from spartner.settings.local import *
except ImportError:
    pass
