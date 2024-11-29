def introspection_info(obj):

    all_attributes = dir(obj)
    return (
        f'type: {type(obj)}, attributes: {[getattr(obj, attr) for attr in all_attributes if not callable(attr) and not attr.startswith("__")]},'
        f' methods: {[name for name in all_attributes if i.ismethod(name) or i.isfunction(name)]}'
        f', module: {i.getmodule(obj)}')


pprint(introspection_info(a))
