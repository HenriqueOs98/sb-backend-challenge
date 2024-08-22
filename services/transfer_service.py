import json
from starkbank import Transfer
from services.starkbank_initializer import initialize_starkbank
import starkbank

initialize_starkbank()

class TransferService:
    def __init__(self, logger, tracer):
        self.logger = logger
        self.tracer = tracer

    def make_transfer(self, event):
        for record in event.get('Records', []):
            body = json.loads(record['body'])
            invoice_event = body.get("event")
            if invoice_event and invoice_event.get("subscription") == "invoice":
                invoice = invoice_event.get("log", {}).get("invoice", {})
                status = invoice.get("status")
                if status == "paid":
                    amount = invoice.get("amount")
                    transfer = Transfer(
                        amount=amount,
                        bank_code="20018183",
                        branch_code="0001",
                        account_number="6341320293482496",
                        account_type="payment",
                        name="Stark Bank S.A.",
                        tax_id="20.018.183/0001-80"
                    )
                    created_transfer = starkbank.transfer.create([transfer])
                    self.logger.info(f"Created transfer: {created_transfer}")