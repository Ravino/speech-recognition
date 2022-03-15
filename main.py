import os
import wave

import numpy as np
import pandas as pd
from deepspeech import Model


def convert_wav_to_numpy(path: str) -> np.array:
    """Convert wav to numpy

    Args:
        path (str): relative path to file

    Returns:
        np.int16: np.array
    """

    real_path = f"{cur_dir()}/{path}"
    real_path = os.path.realpath(real_path)

    with wave.open(real_path, 'rb') as w:
        frames = w.getnframes()
        buffer = w.readframes(frames)
    data = np.frombuffer(buffer, dtype=np.int16)
    return data


def cur_dir() -> str:
    return os.path.dirname(os.path.abspath(__file__))


if __name__ == '__main__':
    my_path = "data/"
    wav_files = os.listdir(my_path)

    model = Model(f"{cur_dir()}/deepspeech-0.9.3-models.pbmm")
    model.enableExternalScorer(f"{cur_dir()}/deepspeech-0.9.3-models.scorer")
    lm_alpha = 0.5
    lm_beta = 1.18
    model.setScorerAlphaBeta(lm_alpha, lm_beta)

    results = [model.stt(convert_wav_to_numpy(f"{my_path}{wav_file}"))
               for wav_file in wav_files]

    df = pd.DataFrame({'original': wav_files, 'results': results})

    print(df)
