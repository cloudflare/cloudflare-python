# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SchemaGetResponse", "Input", "Output"]


class Input(BaseModel):
    additional_properties: bool = FieldInfo(alias="additionalProperties")

    description: str

    type: str


class Output(BaseModel):
    additional_properties: bool = FieldInfo(alias="additionalProperties")

    description: str

    type: str


class SchemaGetResponse(BaseModel):
    input: Input

    output: Output
