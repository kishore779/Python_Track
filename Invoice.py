from dataclasses import dataclass

@dataclass
class Invoice:
    invoice_id : int
    customer_name : str
    date : str
    items : list[str]
    total_amount : int
    status : str

