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

    Must contain 2–50 UTF-8 bytes. Text in any language is supported, including
    spaces, numbers, punctuation, and symbols. Tabs, line breaks, invalid text, and
    invisible formatting characters are not allowed.
    """


class CustomTopicUpdateResponse(BaseModel):
    topics: Optional[List[Topic]] = None
    """Custom topic categories for AI Security for Apps content detection."""
