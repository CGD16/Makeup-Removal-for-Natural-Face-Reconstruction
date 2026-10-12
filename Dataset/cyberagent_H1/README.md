---
license: cc-by-nc-sa-4.0
---

# Dataset Card for FFHQ-Makeup

FFHQ-Makeup is a large-scale paired synthetic facial makeup dataset designed to support research on virtual try-on, makeup transfer, and beauty-related vision tasks. The dataset provides paired bare–makeup facial images while maintaining identity and expression consistency across diverse subjects and makeup styles.

## Dataset Details

### Dataset Description

The FFHQ-Makeup dataset is a high-quality synthetic dataset that builds upon the FFHQ dataset. It uses an advanced makeup transfer pipeline to apply real-world makeup styles to 18,000 identities, generating five distinct makeup styles for each subject. The dataset maintains consistent facial identity and expression across bare and makeup images, which is critical for tasks such as makeup transfer, facial editing, and aesthetic analysis.

- **Curated by:** CyberAgent AI Lab
- **Language(s) (NLP):** N/A (Image dataset)
- **License:** We inherit the same license [https://github.com/NVlabs/ffhq-dataset?tab=readme-ov-file#licenses] from FFHQ

### Dataset Sources

- **Repository:** [https://github.com/YangXingchao/FFHQ-Makeup](https://github.com/YangXingchao/FFHQ-Makeup)
- **Paper:** [https://www.arxiv.org/abs/2508.03241](https://www.arxiv.org/abs/2508.03241)
- **Project Page:** [https://yangxingchao.github.io/FFHQ-Makeup-page/](https://yangxingchao.github.io/FFHQ-Makeup-page/)

## Uses

### Direct Use

The dataset is intended for use in:

- Makeup transfer and synthesis
- Virtual makeup try-on systems
- Identity-preserving image generation
- Facial attribute editing
- Facial aesthetics and beauty analysis
- Training and evaluation of disentanglement models

### Out-of-Scope Use

- Use for commercial purposes is restricted under the dataset's **non-commercial license**.

## Dataset Structure

The dataset consists of:
- Bare face images: selected from the original FFHQ dataset
- Makeup-applied images: created by transferring makeup styles to the base images

Each of the 18,000 subjects has:
- One **bare face** image
- Five **makeup-applied** images, each representing a different style

All images are:
- 512×512 pixels
- In JPEG format
- Aligned and identity-consistent across styles

Example file naming:
- bare.jpg
- makeup_01.jpg
- makeup_02.jpg
- makeup_03.jpg
- makeup_04.jpg
- makeup_05.jpg


## Dataset Creation

### Curation Rationale

Real-world paired bare–makeup facial datasets are scarce due to privacy and annotation constraints. FFHQ-Makeup was created to provide a controlled, diverse, and scalable alternative through synthetic generation, enabling consistent identity and expression across varying makeup styles.

### Source Data

The base images come from the publicly available FFHQ dataset. Makeup styles were collected from various makeup datasets or extracted from real-world references.

#### Data Collection and Processing

- Facial images are selected from FFHQ.
- A novel disentangled makeup transfer model was used to apply realistic makeup while preserving identity.
- Each bare face is transferred to five diverse makeup styles.

#### Who are the source data producers?

The base images originate from [FFHQ (Flickr-Faces-HQ)](https://github.com/NVlabs/ffhq-dataset) by NVIDIA, which consists of high-quality Flickr images released under Creative Commons. Makeup reference images come from curated online sources and existing datasets.

The license and original author of each base image can be found in the original metadata at [https://drive.google.com/file/d/16N0RV4fHI6joBuKbQAoG34V_cQk7vxSA/view](https://drive.google.com/file/d/16N0RV4fHI6joBuKbQAoG34V_cQk7vxSA/view).
```
A Style-Based Generator Architecture for Generative Adversarial Networks
Tero Karras (NVIDIA), Samuli Laine (NVIDIA), Timo Aila (NVIDIA)
https://arxiv.org/abs/1812.04948
```

#### Personal and Sensitive Information

This dataset does not contain personally identifiable or sensitive information. All identities are derived from the FFHQ dataset and are anonymized or synthetic. No real user data or annotations were used during dataset creation.

## Bias, Risks, and Limitations

While FFHQ-Makeup offers high-quality and consistent image pairs, it has some limitations:

- Makeup styles are limited to those from the MT and LADN datasets.

- Faces are based on FFHQ and may lack global demographic diversity.

- Occasional artifacts may appear outside the face region (e.g., clothing color).

- Quality control involves manual filtering, which may introduce bias.

  
## Citation

**BibTeX:**
```bibtex
@inproceedings{yang_2025_ffhq_makeup,
  title={FFHQ-Makeup: Paired Synthetic Makeup Dataset with Facial Consistency Across Multiple Styles}, 
  author={Xingchao Yang and Shiori Ueda and Yuantian Huang and Tomoya Akiyama and Takafumi Taketomi},
  booktitle={arXiv},
  year={2025},
}