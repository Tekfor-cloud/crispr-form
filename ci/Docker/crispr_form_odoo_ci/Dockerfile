#--
# start from image
FROM article714/odoo-container
LABEL maintainer="Apside <dcouppe.2801@apside-groupe.com>"

ARG CI_JOB_TOKEN
ARG CI_COMMIT_REF_NAME

COPY container /container

RUN /container/build.sh
