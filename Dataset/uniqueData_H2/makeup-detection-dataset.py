import datasets
import pandas as pd

_CITATION = """\
@InProceedings{huggingface:dataset,
title = {makeup-detection-dataset},
author = {TrainingDataPro},
year = {2023}
}
"""

_DESCRIPTION = """\
The dataset consists of photos featuring the same individuals captured in two
distinct scenarios - *with and without makeup*. The dataset contains a diverse
range of individuals with various *ages, ethnicities and genders*. The images
themselves would be of high quality, ensuring clarity and detail for each
subject.
In photos with makeup, it is applied **to only specific parts** of the face,
such as *eyes, lips, or skin*.
In photos without makeup, individuals have a bare face with no visible
cosmetics or beauty enhancements. These images would provide a clear contrast
to the makeup images, allowing for significant visual analysis.
"""
_NAME = 'makeup-detection-dataset'

_HOMEPAGE = f"https://huggingface.co/datasets/TrainingDataPro/{_NAME}"

_LICENSE = ""

_DATA = f"https://huggingface.co/datasets/TrainingDataPro/{_NAME}/resolve/main/data/"


class MakeupDetectionDataset(datasets.GeneratorBasedBuilder):
    """Small sample of image-text pairs"""

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features({
                'no_makeup': datasets.Image(),
                'with_makeup': datasets.Image(),
                'part': datasets.Value('string'),
                'gender': datasets.Value('string'),
                'age': datasets.Value('int8'),
                'country': datasets.Value('string')
            }),
            supervised_keys=None,
            homepage=_HOMEPAGE,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        no_makeup = dl_manager.download(f"{_DATA}no_makeup.tar.gz")
        with_makeup = dl_manager.download(f"{_DATA}with_makeup.tar.gz")
        annotations = dl_manager.download(f"{_DATA}{_NAME}.csv")
        no_makeup = dl_manager.iter_archive(no_makeup)
        with_makeup = dl_manager.iter_archive(with_makeup)
        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN,
                                    gen_kwargs={
                                        "no_makeup": no_makeup,
                                        'with_makeup': with_makeup,
                                        'annotations': annotations
                                    }),
        ]

    def _generate_examples(self, no_makeup, with_makeup, annotations):
        annotations_df = pd.read_csv(annotations, sep=';')

        for idx, ((image_path, image),
                  (mask_path, mask)) in enumerate(zip(no_makeup, with_makeup)):
            yield idx, {
                "no_makeup": {
                    "path": image_path,
                    "bytes": image.read()
                },
                "with_makeup": {
                    "path": mask_path,
                    "bytes": mask.read()
                },
                'part':
                    annotations_df.loc[annotations_df['no_makeup'].str.lower() ==
                                       image_path.lower()]['part'].values[0],
                'gender':
                    annotations_df.loc[annotations_df['no_makeup'].str.lower() ==
                                       image_path.lower()]['gender'].values[0],
                'age':
                    annotations_df.loc[annotations_df['no_makeup'].str.lower() ==
                                       image_path.lower()]['age'].values[0],
                'country':
                    annotations_df.loc[annotations_df['no_makeup'].str.lower() ==
                                       image_path.lower()]['country'].values[0]
            }
