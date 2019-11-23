version_info = (0, 2, '0a')
# format:
# ('spinup_major', 'spinup_minor', 'spinup_patch')

def get_version():
    "Returns the version as a human-format string."
    return f'{version_info[0]}.{version_info[1]}.{version_info[2]}'

__version__ = get_version()
