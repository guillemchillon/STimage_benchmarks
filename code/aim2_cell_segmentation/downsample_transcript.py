
import os
import pandas as pd
import random
from glob import glob

# random seed
random_seed = 42

# select all parquet files
parquet_files = glob("/home/jiyaoz/statsproject/xenium_mouse_brain/grid_transcript/transcripts_x*_y*.parquet")

for file_path in parquet_files:
    # extract file name
    base_name = os.path.basename(file_path)
    id_part = base_name.replace("transcripts_", "").replace(".parquet", "")
    
    # read parquet file
    df = pd.read_parquet(file_path)
    
    # random select 50%
    df_sampled = df.sample(frac=0.5, random_state=random_seed)
    
    # new file name
    new_file = f"transcripts_downsample0.5_{id_part}.parquet"
    
    # save to new parquet
    df_sampled.to_parquet(new_file, index=False)
    
    print(f"Processed {base_name} -> {new_file}")



