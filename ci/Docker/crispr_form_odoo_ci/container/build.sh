apt-get update

pip3 install pytest pytest-odoo

python3 /container/tools/clone_dependencies.py /home/odoo/addons 12.0

apt-get -yq clean && \
apt-get -yq autoremove && \
rm -rf /var/lib/apt/lists/* \

cd /home/odoo/addons
git clone --branch ${CI_COMMIT_REF_NAME} --single-branch https://gitlab-ci-token:${CI_JOB_TOKEN}@git.lease4.net/article714/crispr-form.git
