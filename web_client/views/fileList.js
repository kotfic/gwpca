import _ from 'underscore';
import { restRequest } from 'girder/rest';
import FileListWidget from 'girder/views/widgets/FileListWidget';
import { wrap } from 'girder/utilities/PluginUtils';
import JobStatus from 'girder_plugins/jobs/JobStatus';
import eventStream from 'girder/utilities/EventStream';
import gwpcaFileAction from '../templates/gwpca_fileAction.pug';
// import '../stylesheets/fileList.styl';

wrap(FileListWidget, 'render', function (render) {
    render.call(this);
    console.log("foobar");

    var files = this.collection.toArray();
    _.each(files, (file) => {
        var actions = this.$('.g-file-list-link[cid="' + file.cid + '"]')
          .closest('.g-file-list-entry').children('.g-file-actions-container');
        if (!actions.length) {
            return;
        }
        var fileAction = gwpcaFileAction({
            file: file});
        if (fileAction) {
            actions.prepend(fileAction);
        }
    });

    this.$('.g-run-pca').on('click', (event) => {
        var el = event.currentTarget;

        $(el).find('i').addClass('icon-spin5').removeClass('icon-chart-bar');

        restRequest({
            type: 'POST',
            url: 'pca/' + $(el).data('fileid'),
            error: null
        }).done((job) => {
            var refresh_when_done = (event) => {
                if(_.contains([JobStatus.SUCCESS,
                               JobStatus.ERROR,
                               JobStatus.CANCELED],
                              event.data.status)) {

                    this.parentView.model.fetch();

                    this.stopListening(eventStream, 'g:event.job_status', refresh_when_done);
                }

            };
            this.listenTo(eventStream, 'g:event.job_status', refresh_when_done);

        });
    });

    return this;
});
