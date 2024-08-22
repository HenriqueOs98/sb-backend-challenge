import json
from aws_lambda_powertools import Logger, Tracer, Metrics
from aws_lambda_powertools.utilities.typing import LambdaContext
from services.invoice_service import InvoiceService
from services.transfer_service import TransferService

# Initialize Logger, Tracer, and Metrics
logger = Logger()
tracer = Tracer()
metrics = Metrics()


# Initialize Services
invoice_service = InvoiceService(logger, tracer)
transfer = TransferService(logger, tracer)

# Lambda handler function
@logger.inject_lambda_context(log_event=True)
@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    if event.get("source") == "aws.events":
        logger.info("Triggered by CloudWatch event")
        invoice_service.create_invoices()
    elif event.get("Records"):
        logger.info("Triggered by SQS event")
        transfer.make_transfer(event)
    else:
        logger.info("Unknown event source")
    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }