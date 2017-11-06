from girder.api import access
from girder.api.describe import Description, autoDescribeRoute
from girder.api.rest import Resource, filtermodel, getCurrentToken
from girder.constants import AccessType, TokenScope
from girder.models.item import Item as ItemModel
from gwpca.tasks import gw_pca
from gwpca import GirderFileId
from girder.api.rest import getApiUrl

FILEID = '59fce33bf4b1490001f1eb77'


class PCA(Resource):

    def __init__(self):
        super(PCA, self).__init__()
        self.resourceName = 'pca'
        self.route('GET', (), self.test)
        self.route('POST', (':id',), self.generatePCAPlot)

    @access.public(scope=TokenScope.DATA_READ)
    @filtermodel(model=ItemModel)
    @autoDescribeRoute(
        Description('Generate PCA for item with ID.')
        .responseClass('Item')
        .modelParam('id', model=ItemModel, level=AccessType.READ)
        .errorResponse('ID was invalid.')
        .errorResponse('Read access was denied for the item.', 403)
    )
    def generatePCAPlot(self, item):
        gw_pca.delay(GirderFileId(item['_id']))

        return item

    @autoDescribeRoute(
        Description('Generate PCA for item with ID.')
    )

    def test(self):
        token = getCurrentToken()

        gw_pca.delay(
            GirderFileId(FILEID),
#            girder_results=[GirderItemMetadata(item['_id']),
#                            GirderUploadToFileToItem(item['_id'])]
        )


        # gw_pca.delay('/gw_pca/iris.csv', girder_results="Foobar")
