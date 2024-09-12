import os

ROOT_DIR = os.path.abspath(os.path.join(__file__, '../../../'))

DATA_DIR = os.path.join(ROOT_DIR, "freesound-oneshots-dataset")
OUT_DIR = os.path.join(ROOT_DIR, "test-output")

KK_DIR = os.path.join(DATA_DIR, "kick_samples")
SN_DIR = os.path.join(DATA_DIR, "snare_samples")
HH_DIR = os.path.join(DATA_DIR, "hh_samples")

assert os.path.isdir(DATA_DIR)
assert os.path.isdir(KK_DIR)
assert os.path.isdir(SN_DIR)
assert os.path.isdir(HH_DIR)
assert os.path.isdir(OUT_DIR)

KK_TRAIN_DIR = os.path.join(KK_DIR, "train")
SN_TRAIN_DIR = os.path.join(SN_DIR, "train")
HH_TRAIN_DIR = os.path.join(HH_DIR, "train")

KK_VAL_DIR = os.path.join(KK_DIR, "validation")
SN_VAL_DIR = os.path.join(SN_DIR, "validation")
HH_VAL_DIR = os.path.join(HH_DIR, "validation")

#from paths import KK_DIR, SN_DIR, HH_DIR, OUT_DIR