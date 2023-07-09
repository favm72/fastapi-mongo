export STAGE=dev
export RELOAD=true
export PORT=5000
export MONGO_URL=mongodb://localhost:27017/
export MONGO_DB=fastapi

#activate virtual environment
source .venv/Scripts/activate
#run the app
python start.py
