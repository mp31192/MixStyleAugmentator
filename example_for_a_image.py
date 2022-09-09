import os
import numpy as np
from PIL import Image

import torch
from torch.nn import functional as F

from Augmentator_models import Augmentator

## select the number of GPU
device = torch.device('cuda:1' if torch.cuda.is_available() else 'cpu')

## Example for self-style augmentation
## choice an augmentation method
model_type = "styleaug" ## [styleaug, mixstyleaug]
augmentator = Augmentator(model_name=model_type, device=device)

## read example images
example_path = "content.jpg"
img = Image.open(example_path)
img_array = np.asarray(img) ## shape NxNx3, must be three channels image
img_shape = img_array.shape

## change to tensor
img_array = np.transpose(img_array, [2, 0, 1]) ## change dimension from NxNx3 to 3xNxN
img_array = torch.from_numpy(img_array).unsqueeze(0).to(device) ## change the array to tensor, and output a tensor with shape of Bx3xNxN in GPU type
img_array = img_array.float()
img_array = (img_array - torch.min(img_array)) / (torch.max(img_array) - torch.min(img_array))  ## normalization
img_array = F.interpolate(img_array, size=(256, 256), mode="bilinear", align_corners=True)

if model_type == "mixstyleaug":
    style_path = "style.jpg"
    style_img = Image.open(style_path)
    style_img_array = np.asarray(style_img)

    style_img_array = np.transpose(style_img_array, [2, 0, 1])  ## change dimension from NxNx3 to 3xNxN
    style_img_array = torch.from_numpy(style_img_array).unsqueeze(0).to(
        device)  ## change the array to tensor, and output a tensor with shape of Bx3xNxN in GPU type
    style_img_array = style_img_array.float()
    style_img_array = (style_img_array - torch.min(style_img_array)) / (torch.max(style_img_array) - torch.min(style_img_array))   ## normalization
    style_img_array = F.interpolate(style_img_array, size=(256, 256), mode="bilinear", align_corners=True)

## augmentation
if model_type == "styleaug":
    result = augmentator.inference(img_array)
elif model_type == "mixstyleaug":
    result = augmentator.inference(img_array, style_img_array)
else:
    print("Error! Wrong model type!")

result = F.interpolate(result, size=(img_shape[0], img_shape[1]), mode="bilinear", align_corners=True)

## save to jpg
save_img = result.cpu().numpy()
save_img = np.transpose(save_img[0, :, :, :], [1, 2, 0])
save_img = save_img * 255
save_img = save_img.astype('uint8')
save_img = Image.fromarray(save_img)
save_img.save("selfstylized.jpg")

print("Finish")
