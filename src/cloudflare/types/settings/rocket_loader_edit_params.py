# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RocketLoaderEditParams", "Value"]


class RocketLoaderEditParams(TypedDict, total=False):
    value: Required[Value]
    """
    Rocket Loader is a general-purpose asynchronous JavaScript optimisation that
    prioritises rendering your content while loading your site's Javascript
    asynchronously. Turning on Rocket Loader will immediately improve a web page's
    rendering time sometimes measured as Time to First Paint (TTFP), and also the
    `window.onload` time (assuming there is JavaScript on the page). This can have a
    positive impact on your Google search ranking. When turned on, Rocket Loader
    will automatically defer the loading of all Javascript referenced in your HTML,
    with no configuration required. Refer to
    [Understanding Rocket Loader](https://support.cloudflare.com/hc/articles/200168056)
    for more information.
    """


class Value(TypedDict, total=False):
    id: Required[Literal["rocket_loader"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""
