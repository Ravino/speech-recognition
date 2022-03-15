curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer
sudo apt update
sudo apt install sox
sudo apt install ffmpeg
python3.8 -m venv .venv
source ./venv/bin/activate
pip3 install -r requirements.txt