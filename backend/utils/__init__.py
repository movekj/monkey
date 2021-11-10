from .exception import *


def param_preprocessing(params, filter_keys=('id')):
    bad_params = list(set(params.keys()) - set(filter_keys))
    if bad_params:
        raise ParamError(bad_params[0], '多余的参数[%s]' % bad_params)

    _params = dict()
    for key in params:
        value = params.get(key)
        if value:
            _params[key] = value

    return _params
