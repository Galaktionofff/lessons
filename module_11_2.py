import inspect as i
from pprint import pprint


def introspection_info(obj):

    all_attributes = dir(obj)

    return (
        f'type: {type(obj)}, attributes: {[getattr(obj, attr) for attr in all_attributes if not callable(getattr(obj, attr)) and not attr.startswith("__")]},'
        f' methods: {[attr for attr in all_attributes if callable(getattr(obj, attr)) and not attr.startswith("__")]}'
        f', module: {i.getmodule(obj)}')

a = '123'
pprint(introspection_info(a))
