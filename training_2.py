import logging
from typing import Dict, Optional

logging.basicConfig(filename="dict.log", level="INFO")
logger = logging.getLogger(__name__)


def calculate_user_average_age(data: Dict[str, any]) -> Optional[float]:

    if "name" not in data or "age" not in data or "count" not in data:
        logger.error("Missing required details in given user dictionary")
        return None

    try:
        age = float(data["age"])
        count = float(data["count"])

        if count == 0:
            logger.error("Age cannot be divisible by 0")
            return 0.0

        logger.info(f"Successfully parsed for the data {data['name']}")
        return age / count

    except ValueError as err:
        logger.exception(f"Type Conversion failes {err}")
        return None


data = {
    "user_1": {"name": "kishore", "age": "ki", "count": 100},
    "user_2": {"name": "luffy", "age": 19, "count": 0},
}

for data_key, data_item in data.items():
    result = calculate_user_average_age(data_item)
    print(f"Result for {data_key} : {data_item}")
