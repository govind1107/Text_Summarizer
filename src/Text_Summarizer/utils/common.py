import os
from box.exceptions import BoxValueError
import yaml
from Text_Summarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


"""
ConfigBox Usage:


What is ConfigBox?
ConfigBox is a specific class within the box library that extends the functionality of the standard Box class by adding support for configuration-specific features, such as:

Dot notation: You can access dictionary keys using dot notation, which is more intuitive and concise.
Default values: It allows for the assignment of default values for keys that may not exist in the dictionary.
Type enforcement: You can enforce types on the values associated with the keys.
from box import ConfigBox

# Create a ConfigBox object
config = ConfigBox({
    "database": {
        "host": "localhost",
        "port": 5432
    },
    "debug": True
})

# Accessing values using dot notation
print(config.database.host)  # Output: "localhost"
print(config.debug)          # Output: True
"""


"""
from ensure import ensure_annotations

Type Annotations: Python allows you to specify the expected types of function arguments and return values using type annotations. However, these annotations are not enforced by Python at runtime—they are primarily used for documentation and by static type checkers (like mypy).

ensure_annotations: The ensure_annotations module provides decorators that can enforce these type annotations at runtime. If the actual types of the arguments or the return value do not match the specified annotations, an error is raised.

from ensure import ensure_annotations

@ensure_annotations
def add(x: int, y: int) -> int:
    return x + y

add(3, 5)  # This will work fine.
add("3", 5)  # This will raise a TypeError because "3" is not an int.
"""


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"