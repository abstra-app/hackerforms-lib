url_params = {}


def set_params(new_params):
    global url_params
    for param_key in new_params:
        url_params[param_key] = new_params[param_key]
