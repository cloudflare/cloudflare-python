# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ScanListResponse", "Result", "ResultPage", "ResultStats", "ResultTask", "ResultVerdicts"]


class ResultPage(BaseModel):
    asn: str

    country: str

    ip: str

    url: str


class ResultStats(BaseModel):
    data_length: float = FieldInfo(alias="dataLength")

    requests: float

    uniq_countries: float = FieldInfo(alias="uniqCountries")

    uniq_ips: float = FieldInfo(alias="uniqIPs")


class ResultTask(BaseModel):
    time: str

    url: str

    uuid: str

    visibility: str


class ResultVerdicts(BaseModel):
    malicious: bool


class Result(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    page: ResultPage

    result: str

    stats: ResultStats

    task: ResultTask

    verdicts: ResultVerdicts


class ScanListResponse(BaseModel):
    results: List[Result]
