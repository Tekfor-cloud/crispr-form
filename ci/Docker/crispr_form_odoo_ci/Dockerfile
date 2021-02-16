#--
# start from image
FROM lease4/odoo_ci:1.4
LABEL maintainer="Apside <dcouppe.2801@apside-groupe.com>"

ARG CI_JOB_TOKEN
ARG CI_COMMIT_REF_NAME

COPY container /container

RUN /container/build.sh
