import os

from girder_worker import GirderWorkerPluginABC


class GWPCAPlugin(GirderWorkerPluginABC):
    def __init__(self, app, *args, **kwargs):
        self.app = app

    def task_imports(self):
        # Return a list of python importable paths to the
        # plugin's path directory
        return ['gwpca.tasks']
