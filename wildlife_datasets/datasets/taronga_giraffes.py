import os
import pandas as pd
from . import utils
from .datasets import DatasetFactory
# from .summary import summary


class TarongaGiraffes(DatasetFactory):
    summary = {"Description": "Taronga Giraffes"}  # summary['TarongaGiraffes']
    url = ''  # 'https://lilawildlife.blob.core.windows.net/lila-wildlife/wild-me/gzgc.coco.tar.gz'
    archive = ''  # 'gzgc.coco.tar.gz'

    @classmethod
    def _download(cls):
        pass 
        # utils.download_url(cls.url, cls.archive)

    @classmethod
    def _extract(cls):
        pass

    def create_catalogue(self) -> pd.DataFrame:
        src = pd.read_csv(os.path.join(self.root, "wildlife_output.csv"))
        df = pd.DataFrame({
            'image_id': src['index'],
            'path': src['filename'].apply(lambda x: os.path.join('training_images', os.path.basename(x))),
            'identity': src['identity'],
        })
        return self.finalize_catalogue(df)
