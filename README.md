# Speech recognistion "Set English expressions and catchphrases"


## Running in docker
```
docker pull ravino/speech-recognition:1.0.0
docker run --rm ravino/speech-recognition:1.0.0
```
## Install
```
poetry install
poetry shell
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer
sudo apt update
sudo apt install sox
```
## Install bash
```
sudo chmod +x ./install.sh
. ./install.sh
```

## WAV File 
 You need 16 bit 16kGh mono normilized data wav files
 You can preprocessing with https://www.online-convert.com/ru or some python code
