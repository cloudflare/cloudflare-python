# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ...._models import BaseModel

__all__ = ["SkipConfiguration"]


class SkipConfiguration(BaseModel):
    files: bool
    """If the content type is a file, skip context analysis and return all matches."""
