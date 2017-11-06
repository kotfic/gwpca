from girder_worker_utils.transform import Transform
from girder_worker import GirderWorkerPluginABC


class GirderFileId(Transform):
    def __init__(self, _id, apiurl=None, token=None):
        self.item_id = _id
        try:
            from girder.api.rest import getApiUrl, getCurrentToken
            self.apiurl = getApiUrl() if apiurl is None else apiurl
            self.token = getCurrentToken()['_id'] if token is None else token
        except ImportError:
            self.apiurl = apiurl
            self.token = token

    def transform(self):
        import rpdb; rpdb.set_trace()
        from girder_client import GirderClient
        gc = GirderClient(apiUrl=self.apiurl)
        gc.token = self.token

        gc.downloadFile(self.item_id, '/tmp/file.csv')

        return '/tmp/file.csv'


class GirderItemMetadata(Transform):
    def __init__(self, _id, *args, **kwargs):
        self.item_id = _id

    def transform(self, data):
        pass

class GWPCAPlugin(GirderWorkerPluginABC):
    def __init__(self, app, *args, **kwargs):
        self.app = app

    def task_imports(self):
        # Return a list of python importable paths to the
        # plugin's path directory
        return ['gwpca.tasks']
