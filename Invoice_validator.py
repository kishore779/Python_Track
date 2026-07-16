from Invoice import Invoice

class InvoiceController:
    def __init__(self, invoice):
        self.invoice = invoice

    def validate(self):
        if not self.invoice.invoice_id:
            return "Name is required"
        if not self.invoice.customer_name:
            return "Id is mandatory"
        if not self.invoice.items:
            return "No Items"
        if self.invoice.total_amount < 0:
            return "Negative sum"
        return "Invoice Valid"