# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UnnamedSchemaRef91"]


class UnnamedSchemaRef91(BaseModel):
    escaped_worker_name: str = FieldInfo(alias="escapedWorkerName")

    worker_tag: str = FieldInfo(alias="workerTag")
