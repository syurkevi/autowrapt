from afsklearn.patcher import Patcher

def patch_sklearn(module):
    Patcher.patch_all()

