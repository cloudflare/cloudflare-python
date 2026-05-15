# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "BillingInvoicePreviewResponse",
    "InvoiceLine",
    "InvoiceLinePeriod",
    "InvoiceLinePricing",
    "InvoiceLinePretaxCreditAmount",
]


class InvoiceLinePeriod(BaseModel):
    end: float

    start: float


class InvoiceLinePricing(BaseModel):
    unit_amount_decimal: Optional[str] = None


class InvoiceLinePretaxCreditAmount(BaseModel):
    amount: float

    type: str

    credit_balance_transaction: Optional[str] = None

    discount: Optional[str] = None


class InvoiceLine(BaseModel):
    amount: float

    currency: str

    description: Optional[str] = None

    period: InvoiceLinePeriod

    pricing: InvoiceLinePricing

    quantity: float

    pretax_credit_amounts: Optional[List[InvoiceLinePretaxCreditAmount]] = None


class BillingInvoicePreviewResponse(BaseModel):
    id: str

    amount_due: float

    amount_paid: float

    amount_remaining: float

    currency: str

    invoice_lines: List[InvoiceLine]

    period_end: float

    period_start: float

    status: Literal["draft", "open", "paid", "uncollectible", "void"]
