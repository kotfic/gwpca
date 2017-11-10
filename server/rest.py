from girder.api import access
from girder.api.describe import Description, autoDescribeRoute
from girder.api.rest import Resource, RestException, filtermodel
from girder.constants import AccessType, TokenScope
from girder.models.file import File as FileModel
from girder.plugins.jobs.models.job import Job as JobModel

from girder_worker_utils.transforms.girder_io import (
    GirderFileId,
    GirderItemMetadata,
    GirderUploadToItem)

from gwpca.tasks import gw_pca

class PCA(Resource):

    def __init__(self):
        super(PCA, self).__init__()
        self.resourceName = 'pca'
#        self.route('GET', (), self.test)
        self.route('POST', (':id',), self.generatePCAPlot)

    @access.public(scope=TokenScope.DATA_READ)
    @filtermodel(model=JobModel)
    @autoDescribeRoute(
        Description('Generate PCA for item with ID.')
        .responseClass('Job')
        .modelParam('id', model=FileModel, level=AccessType.READ)
        .errorResponse('ID was invalid.')
        .errorResponse('Read access was denied for the item.', 403)
    )
    def generatePCAPlot(self, file):

        file_id = str(file['_id'])
        item_id = str(file['itemId'])



        if file['mimeType'] != 'text/csv':
            raise RestException("File must be of type 'text/csv'", code=422)

        a = gw_pca.delay(file['name'], GirderFileId(file_id),
                         girder_result_hooks=[GirderItemMetadata(item_id),
                                              GirderUploadToItem(item_id)])

        return a.job

#     @filtermodel(model='job', plugin='jobs')
#     @autoDescribeRoute(
#         Description('Generate PCA for item with ID.'))
#     def test(self):
#         pass
#         a = gw_pca.delay(GirderItemIdToDirectory(ITEMID))
#
#         return a.job
#         # from common_tasks.test_tasks.fib import fibonacci
#         # fibonacci.delay(20)
