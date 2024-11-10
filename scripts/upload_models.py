"""
Load models and upload to HF Hub with relevant metadata.
"""

# imports
import os
from pathlib import Path
from typing import Any

# packages
from huggingface_hub import HfApi

# get paths
PATH_LIST: list[str] = [
    # this is just getting the absolute path for `../kl3m-embedding-00*` as a string
    (Path(__file__).parent.parent / p).resolve().as_posix()
    for p in (
        "/nas4/data/checkpoints/kl3m-002-170m/",
        "/nas4/data/checkpoints/kl3m-003-1.7b/",
    )
]


if __name__ == "__main__":
    # iterate through paths, load the model, and print the basic model info
    # - name
    # - tokenizer name
    # - tokenizer config
    # - model type
    # - model config

    # track model metadata
    model_metadata: dict[str, Any] = {}

    for path in PATH_LIST:
        # get the model display name
        model_name = str(path).rsplit("/", maxsplit=1)[-1]
        repo_id = f"alea-institute/{model_name}"

        # use HfApi to upload all files from that folder
        hf_api = HfApi()
        try:
            repo_url = hf_api.create_repo(
                repo_id=repo_id,
                repo_type="model",
                private=True,
            )
        except Exception as e:
            print(f"Error creating repo {repo_id}: {e}")

        # now upload all files to main
        hf_api.upload_folder(
            repo_id=repo_id,
            folder_path=path,
        )
