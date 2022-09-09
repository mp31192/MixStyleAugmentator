import torch
import torch.nn as nn
import random
import numpy as np
from .transfer_WCT import WCT2

class MixStyleAugmentor:
    def __init__(self, device, alpha=1.0, option_unpool='cat5', feature_used='encoder'):

        self.device = device

        option_unpool_ = option_unpool  # choices=['sum', 'cat5']
        self.alpha_ = alpha

        _transfer_at = set()
        _transfer_at.add(feature_used)  # choices=['encoder', 'decoder', 'skip', 'all']

        self.wct2 = WCT2(transfer_at=_transfer_at, option_unpool=option_unpool_, device=self.device)
        self.wct2.encoder.eval()
        self.wct2.decoder.eval()

    def inference(self, content, style, content_segment=np.asarray([]), style_segment=np.asarray([])):
        with torch.no_grad():
            inputs = self.wct2.transfer(content, style, content_segment, style_segment, alpha=self.alpha_)
            random_index = random.uniform(0.2, 0.8)
            results = inputs * random_index + content * (1-random_index)
        return results
