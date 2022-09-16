import torch
from styleaug.styleAugmentor import StyleAugmentor
from mixstyleaug.mixstyleAugmentor import MixStyleAugmentor

class Augmentator:
    def __init__(self, model_name, device):
        self.device = device
        self.model_name = model_name
        if model_name=="styleaug":
            self.model = StyleAugmentor(device)
            self.model.eval()
        elif model_name=="mixstyleaug":
            self.model = MixStyleAugmentor(device, random_mix=True)

    def inference(self, content, style=None):
        content_shape = content.shape
        assert content_shape[1] == 3 or content_shape[1] == 1

        if content_shape[1] == 1:
            content = self.GrayToRGB(content)

        with torch.no_grad():
            if style is None and self.model_name == "styleaug":
                    content = self.model(content)
            elif self.model_name == "mixstyleaug":
                style_shape = style.shape
                if style_shape[1] == 1:
                    style = self.GrayToRGB(style)
                content = self.model.inference(content, style)
            else:
                print("Error Inputs!")

        if content_shape[1] == 1:
            content = self.RGBToGray(content)
        return content

    def GrayToRGB(self, image):
        image = image.repeat(1, 3, 1, 1)
        return image

    def RGBToGray(self, image):
        image = torch.sum(image, dim=1, keepdim=True) / 3
        return image
