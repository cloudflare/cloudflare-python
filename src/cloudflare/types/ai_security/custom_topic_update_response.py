# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CustomTopicUpdateResponse", "Topic"]


class Topic(BaseModel):
    label: str
    """Unique label identifier.

    Must contain only lowercase letters (a–z), digits (0–9), and hyphens.
    """

    topic: str
    """Description of the topic category.

    Must contain only printable ASCII characters.
    """


class CustomTopicUpdateResponse(BaseModel):
    topics: Optional[List[Topic]] = None
    """Custom topic categories for AI Security for Apps content detection."""
