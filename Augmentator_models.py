import torch
from styleaug.styleAugmentor import StyleAugmentor
from mixstyleaug.mixstyleAugmentor import MixStyleAugmentor

class Augmentator:
    def __init__(self, model_name, device):
        self.device = device
        if model_name=="styleaug":
            self.model = StyleAugmentor(device)
            self.model.eval()
        elif model_name=="mixstyleaug":
            self.model = MixStyleAugmentor(device)

    def inference(self, content, style=None):
        with torch.no_grad():
            if style is None:
                content = self.model(content)
            else:
                content = self.model.inference(content, style)
        return content