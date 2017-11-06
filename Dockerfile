FROM girder/girder_worker:latest

USER root

RUN apt-get update && \
    apt-get -qy install\
     git \
     python-scipy\
     python-numpy\
     python-pandas\
     python-matplotlib

COPY . /gw_pca
VOLUME /gw_pca

# Make sure we have the newest girder_worker_utils
# This should be switched to master
#  once https://github.com/girder/girder_worker_utils/pull/2 is merged
RUN pip install https://github.com/girder/girder_worker_utils/archive/transform-refactor.zip

WORKDIR /gw_pca
RUN pip install -U -e ".[worker]" && pip install rpdb
RUN chown -R worker:worker /gw_pca


WORKDIR /girder_worker
USER worker
