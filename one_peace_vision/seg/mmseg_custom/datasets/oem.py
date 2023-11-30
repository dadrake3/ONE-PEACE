from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset


@DATASETS.register_module()
class OpenEarthMapDataset(BaseSegDataset):

    METAINFO = dict(
        classes=("unknown", "Bareland", "Grass", "Pavement", "Road", "Tree", "Water", "Cropland", "buildings"),
        palette=[[127, 0, 255], [63, 97, 250], [0, 180, 235], [64, 236, 211], [128, 254, 179], [192, 234, 140], [255, 178, 96], [255, 95, 48], [255, 0, 0]]
    )

    def __init__(self,
                 img_suffix='.png',
                 seg_map_suffix='.png',
                 reduce_zero_label=True,
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix,
            seg_map_suffix=seg_map_suffix,
            reduce_zero_label=reduce_zero_label,
            **kwargs)
    