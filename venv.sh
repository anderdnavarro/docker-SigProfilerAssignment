# Usage: bash venv.sh <path_to_venv>

path_to_venv=$1

# Create the virtual environment
python3.11 -m venv ${path_to_venv}

# Activate the virtual environment
source ${path_to_venv}/bin/activate

# Install the required packages
pip install --upgrade pip
pip install --no-cache-dir -r requirements.txt
python -c "from SigProfilerMatrixGenerator import install as genInstall; genInstall.install('GRCh37')" 
