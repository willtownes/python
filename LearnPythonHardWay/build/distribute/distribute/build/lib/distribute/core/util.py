import os
import re
from string import maketrans
from distutils.util import convert_path
from fnmatch import fnmatchcase

def find_packages(where='.', exclude=()):
    """Return a list all Python packages found within directory 'where'

    'where' should be supplied as a "cross-platform" (i.e. URL-style) path; it
    will be converted to the appropriate local path syntax.  'exclude' is a
    sequence of package names to exclude; '*' can be used as a wildcard in the
    names, such that 'foo.*' will exclude all subpackages of 'foo' (but not
    'foo' itself).
    """
    out = []
    stack = [(convert_path(where), '')]
    while stack:
        where, prefix = stack.pop(0)
        for name in os.listdir(where):
            if '.' in name:
                continue
            fn = os.path.join(where, name)
            if not os.path.isdir(fn):
                continue

            # check if its a package
            if os.path.isfile(os.path.join(fn, '__init__.py')):
                out.append(prefix+name)
                stack.append((fn, prefix+name+'.'))

    res = []

    def _match(name):
        for match in exclude:
            if fnmatchcase(pkg, match):
                return True
        return False

    return [pkg for pkg in out if not _match(pkg)]

#
# XXX Should this live somewhere else? Distribute.resources?
#

SPACE_TRANS = maketrans(' ', '.')
DASH_TRANS = maketrans('-', '_')

def egginfo_dirname(name, version):
    """Returns the egg-info directory name of a project.

    ``name`` is converted to a standard distribution name any runs of
    non-alphanumeric characters are replaced with a single '-'. ``version``
    is converted to a standard version string. Spaces become dots, and all othe
    non-alphanumeric characters become dashes, with runs of multiple dashes
    condensed to a single dash. Both attributes are then converted into their
    filename-escaped form. Any '-' characters are currently replaced with '_'.
    """
    name = re.sub('[^A-Za-z0-9.]+', '_', name)
    version = version.translate(SPACE_TRANS)
    version = re.sub('[^A-Za-z0-9.]+', '_', version)
    return '%s-%s.egg-info' % (name.translate(DASH_TRANS),
                               version.translate(DASH_TRANS))
