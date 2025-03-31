import os
import test


def path(file_name):
    return os.path.abspath(
        os.path.join(os.path.dirname(test.__file__), f'../resources/{file_name}')
    )