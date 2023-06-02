Thanks to the meta-reviewer and reviewers for your valuable comments of our work. Especially, thanks to R2 and R3 for accepting the paper directly. We appreciate your recognition of:
1. Our contributions (Meta-Reviewer: “useful for the ultrasound imaging community”);
2. Sufficient experiments (R3: “Good ablation experiment” R2: “demonstrate the improvements and advantages”);
3. Well-organization (R2: “detailed explanation of the proposed method” R2: “well-designed flowcharts and figures” R3: “well-written”).

Q1: Why focus on ultrasound (US) (R1). A1: US presents unique challenges compared to other modalities. 1) US is affected by speckle noise, which differs from common Gaussian noise. 2) Acoustic shadow in US can cause missing information in the image. These characteristics can lead to degraded performance in similar studies.

Q2: Clarifications of description in Sect.2.3 MaskAug (R1). A2: To provide clearer explanations, Fig. 2C illustrates the pipeline of MaskAug and the simplified steps are as follows: 1) Select content/style images from training/testing sources. 2) Use a trained network to generate ROIs of these images. 3) Feed the content image, style image and ROIs into style transfer network. 4) Translate the intensity distribution of ROIs in the content image to that of the style image.

Q3: Clarifications about Eq.1 (R1). A3: $A$ is not the feature maps after GAP, as shown in Fig.S1 of supplementary materials. Dynamic range noise for the mean and variance is the same.

Q4: Clarifications about the use of training/testing sources, validation set, and the input/output in Fig.2 (R1). A4: -As stated in the 3rd sentence of Sect.3, our datasets are divided into training and testing sources. Images from training and testing sources are available during training, but only labels from training source are used for loss computation. -We randomly selected 20% of training set as validation set during training. -In Fig.2, inputs are the images from training and testing sources, and outputs are the segmentation and classification results.

Q5: Why are LD1 and TD1 results for the training data in Table.1 (R1)? A5: They are not the results for training data. As mentioned in the caption of Table.1 and the 4th sentence of Sect.3, they represent the performance of the testing set from training sources.

Q6: Lack of information on preprocessing steps (R2). A6: Preprocessing steps are described in the 5th sentence of Sect.3.

Q7: Use of part B in final network (R3). A7: Part B (FeatAug) is not used in final network, as stated in the 1st sentence of Section 2.2.

Q8: Conduct experiments using public datasets (R1). A8: We conducted experiments on a public thyroid dataset (DDTI). The DSC/AUROC values for BigAug, Hesse et al., UDA and our method are 0.526/0.488, 0.645/0.537, 0.470/0.565 and 0.680/0.614, respectively. These experiments indicate that our method achieves the best performance on both public and private datasets, further demonstrating its generality.

Q9: A comparison with AutoAug would be helpful (R1). A9: To address your concern, we applied AutoAug to our datasets and found that it further highlights the superiority of our method. The DSC/AUROC values for LD1, LD2, LD3, TD1 and TD2 using AutoAug are 0.939/0.871, 0.876/0.653, 0.914/0.678, 0.687/0.769 and 0.535/0.392, respectively. The results indicate that AutoAug performs worse than our method and support our conclusions.

Q10: p could be reported in Table.1 and question about negligible improvement of dice score (R3). A10: 
- To compare our method with traditional augmentation, we conducted statistical analysis and observed significant improvements in DSC for TD1 and TD2 (p<0.05), as well as significant improvements in AUROC for LD1, LD2, LD3 and TD1 (p<0.05).
- The DSC shows no significant improvement in LDs, as the liver is easy to segment, resulting in a high baseline. Although the increase in DSC is slight, our method improves both AUROC and DSC across all sources.
