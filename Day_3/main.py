from Invoice import Invoice
from Invoice_validator import InvoiceController

invoice_1 = Invoice(101, "s", "10-07-2026", ['bun','butter','jam'], 230, "Paid")
control = InvoiceController(invoice_1)
print(control.validate())