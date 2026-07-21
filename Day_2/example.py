import logging

logger = logging.getLogger(__name__)


def calc(data: list[dict], mode: str, u: bool) -> int:
    """
    it adds the elements based on the list r based on the status and mode
    """
    r = []
    for item in data:
        if item["status"] != "active":
            continue
        if mode == "sum":
            r.append(item["value"])
        elif item["value"] > 0:
            r.append(item["value"] * 1.1)
        else:
            print("skip")
    total = sum_of_r(r)
    total = is_true(u, total)
    return total


def sum_of_r(r: list) -> int:
    """
    it sums the elements in the list r
    """
    return sum(r)


def is_true(u: bool, total: int) -> int:
    """
    it adds the discount to the total
    """
    if u:
        total = total - (total * 0.05)
    return total


def read_log_file(total: int) -> int:
    """
    it writes the total in the file as an String
    """
    try:
        with open("log.txt", "a") as file:
            file.write(str(total) + "\n")
    except OSError as e:
        logger.error("Failed to fetch")
