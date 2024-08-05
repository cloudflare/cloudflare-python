# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .certificate_settings import CertificateSettings

__all__ = ["SettingGetResponse"]

SettingGetResponse: TypeAlias = List[CertificateSettings]
