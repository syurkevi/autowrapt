import sys
import os
import site

from setuptools import setup
from distutils.sysconfig import get_python_lib


def is_venv():
    return (hasattr(sys, 'real_prefix') or \
           (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

def remove_prefix(s, prefix):
    return s[len(prefix):] if s.startswith(prefix) else s

if is_venv():
    site_path_pth = get_python_lib(prefix='')
else:
    #sys.prefix not pointing to correct data dir for some reason...
    #site_path_pth = remove_prefix(site.getsitepackages()[0], sys.prefix + '/')
    path = site.getsitepackages()[0]
    prefix = sys.prefix + '/local/' if 'local' in path else sys.prefix
    site_path_pth = remove_prefix(path, prefix)

setup_kwargs = dict(
    name = 'autowrapt',
    version = '0.0.1',
    description = 'Boostrap mechanism for monkey patches.',
    author = 'Graham Dumpleton',
    author_email = 'Graham.Dumpleton@gmail.com',
    license = 'BSD',
    url = 'https://github.com/GrahamDumpleton/autowrapt',
    packages = ['autowrapt'],
    package_dir = {'autowrapt': 'src'},
    package_data = {'autowrapt': ['__startup__/sitecustomize.py']},
    data_files = [(site_path_pth, ['autowrapt-init.pth'])],
    entry_points = {
        'console_scripts': ['autowrapt = autowrapt.main:main'],
        'autowrapt.examples': ['this = autowrapt.examples:autowrapt_this'],
        'afsklearn': ['sklearn = autowrapt.afsklearn:patch_sklearn']},
    install_requires = ['wrapt>=1.10.4'],
)

setup(**setup_kwargs)
