# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["BillingInvoiceHistoryResponse", "Invoice", "Pagination"]


class Invoice(BaseModel):
    amount_due: float

    amount_paid: float

    amount_remaining: float

    currency: str

    id: Optional[str] = None

    attempt_count: Optional[float] = None

    attempted: Optional[bool] = None

    auto_advance: Optional[bool] = None

    created: Optional[float] = None

    created_by: Optional[str] = None

    description: Optional[str] = None

    invoice_origin: Optional[str] = None

    invoice_pdf: Optional[str] = None

    status: Optional[str] = None


class Pagination(BaseModel):
    has_more: bool

    page: float

    per_page: float

    total_count: float


class BillingInvoiceHistoryResponse(BaseModel):
    invoices: List[Invoice]

    pagination: Pagination
