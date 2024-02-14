# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Iterable

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["VariantZoneCacheSettingsChangeVariantsSettingParams", "Value"]


class VariantZoneCacheSettingsChangeVariantsSettingParams(TypedDict, total=False):
    value: Required[Value]
    """Value of the zone setting."""


class Value(TypedDict, total=False):
    avif: Iterable[object]
    """
    List of strings with the MIME types of all the variants that should be served
    for avif.
    """

    bmp: Iterable[object]
    """
    List of strings with the MIME types of all the variants that should be served
    for bmp.
    """

    gif: Iterable[object]
    """
    List of strings with the MIME types of all the variants that should be served
    for gif.
    """

    jp2: Iterable[object]
    """
    List of strings with the MIME types of all the variants that should be served
    for jp2.
    """

    jpeg: Iterable[object]
    """
    List of strings with the MIME types of all the variants that should be served
    for jpeg.
    """

    jpg: Iterable[object]
    """
    List of strings with the MIME types of all the variants that should be served
    for jpg.
    """

    jpg2: Iterable[object]
    """
    List of strings with the MIME types of all the variants that should be served
    for jpg2.
    """

    png: Iterable[object]
    """
    List of strings with the MIME types of all the variants that should be served
    for png.
    """

    tif: Iterable[object]
    """
    List of strings with the MIME types of all the variants that should be served
    for tif.
    """

    tiff: Iterable[object]
    """
    List of strings with the MIME types of all the variants that should be served
    for tiff.
    """

    webp: Iterable[object]
    """
    List of strings with the MIME types of all the variants that should be served
    for webp.
    """
