set -e

rm -rf venv

python3 -m venv venv
source venv/bin/activate
pip install wheel==0.41.3
pip install \
    -r requirements-workspace.txt \
    -e analytics \
    -e library \
    -e projects \
    -e services/common \
    -e services/experience-prediction \
    -e services/meeting-planner

deactivate
