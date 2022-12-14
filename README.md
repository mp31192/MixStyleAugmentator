# MixStyleAugmentator
Please read [**example_for_a_image.py**](https://github.com/mp31192/MixStyleAugmentator/blob/main/example_for_a_image.py) to use the augmentator.

Two augmentators are implemented in this project.

"styleaug" - self-style augmentation. (Thanks to https://github.com/philipjackson/style-augmentation)

"mixstyleaug" - mixed style augmentation. (Thanks to https://github.com/clovaai/WCT2)

# Geodesic distance
Example of geodesic distance calculation is presented in [**geodesic_distance_torch.py**](https://github.com/mp31192/MixStyleAugmentator/blob/main/geodesic_distance_torch.py)

Thanks to https://github.com/thuml/Domain-Adaptation-Regression.

# Todo list
- [X] Solve the bugs for CPU.
- [X] Available for single channel images (gray images).
- [ ] Available for 3D patches.
- [X] More optional parameters for mixstyleaug. A random_mix parameter has been added.
- [X] Fix the bugs in [**example_for_a_image.py**](https://github.com/mp31192/MixStyleAugmentator/blob/main/example_for_a_image.py) for saving images.
- [ ] Traditional augmentation.
- [ ] AugMix.
- [ ] Mixup.
- [ ] Copy and paste.
- [X] Add calculation of geodesic distance for datasets estimation.
