import random
from datetime import datetime, timedelta
import starkbank
from starkbank import Invoice
from services.cpf_generator import generate_cpf
from services.name_generator import generate_name
from services.starkbank_initializer import initialize_starkbank
initialize_starkbank()

class InvoiceService:
    def __init__(self, logger, tracer):
        self.logger = logger
        self.tracer = tracer

    def create_invoices(self):
        invoices = []
        for _ in range(random.randint(8, 12)):
            invoices.append(
                Invoice(
                    amount=random.randint(10000, 50000),
                    name=generate_name(6),
                    tax_id=generate_cpf(),
                    due=datetime.now() + timedelta(days=2),
                    expiration=5097600,
                    fine=2.0,
                    interest=1.3,
                    discounts=[{'percentage': 10, 'due': datetime.now() + timedelta(days=1)}],
                    descriptions=[{'key': 'Service', 'value': 'Consulting'}],
                    tags=['random', 'invoice']
                )
            )
        created_invoices = starkbank.invoice.create(invoices)
        for invoice in created_invoices:
            self.logger.info(f"Created invoice: {invoice}")