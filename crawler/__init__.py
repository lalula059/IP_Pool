import inspect
import pkgutil
from crawler.base_fetch import Base_Fetch
classes = []
for file_loader,name,is_pkg in pkgutil.walk_packages(__path__):
    module = file_loader.find_module(name).load_module(name)
    for name,value in inspect.getmembers(module):
        if inspect.isclass(value) and issubclass(value,Base_Fetch) and value is not Base_Fetch:
            classes.append(value)

__all__ = classes