import torch
import albumentations as A
from albumentations.pytorch import ToTensorV2

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
TRAIN_DIR = "Pix2Pix/ConcatenatedImages/train"
# TRAIN_DIR = "Pix2Pix/ConcatenatedImages/val"
VAL_DIR = "Pix2Pix/ConcatenatedImages/val"
LEARNING_RATE = 2e-4
BATCH_SIZE = 64
NUM_WORKERS = 2
IMAGE_SIZE = 256
CHANNELS_IMG = 1
L1_LAMBDA = 100
LAMBDA_GP = 10
NUM_EPOCHS = 500
LOAD_MODEL = True
SAVE_MODEL = False
CHECKPOINT_DISC = "Pix2Pix/Models/disc.pth.tar"
CHECKPOINT_GEN = "Pix2Pix/Models/gen.pth.tar"

both_transform = A.Compose(
    [A.Resize(width=256, height=256),
    #  A.HorizontalFlip(p=0.5),
    ],
     additional_targets={"image0": "image"},
)

transform_only_input = A.Compose(
    [
        # A.ColorJitter(p=0.2),
        A.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5], max_pixel_value=255.0,),
        ToTensorV2(),
    ]
)

transform_only_mask = A.Compose(
    [
        A.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5], max_pixel_value=255.0,),
        ToTensorV2(),
    ]
)