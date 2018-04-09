import os  # write and check full path to document if it exist


def get_template_path(path):
    #  write and check full path to document if it exist
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), path)
    if not os.path.isfile(file_path):
        raise Exception('This is not valid template path %s' % (file_path))
    return file_path


def get_tempalte(path):
    file_path = get_template_path(path)
    return open(file_path).read()


def render_context(template_string, context):
    return template_string.format(**context)
