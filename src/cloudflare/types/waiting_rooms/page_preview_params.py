# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PagePreviewParams"]


class PagePreviewParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    custom_html: Required[str]
    """Only available for the Waiting Room Advanced subscription.

    This is a template html file that will be rendered at the edge. If no
    custom_page_html is provided, the default waiting room will be used. The
    template is based on mustache ( https://mustache.github.io/ ). There are several
    variables that are evaluated by the Cloudflare edge:

    1. {{`waitTimeKnown`}} Acts like a boolean value that indicates the behavior to
       take when wait time is not available, for instance when queue_all is
       **true**.
    2. {{`waitTimeFormatted`}} Estimated wait time for the user. For example, five
       minutes. Alternatively, you can use:
    3. {{`waitTime`}} Number of minutes of estimated wait for a user.
    4. {{`waitTimeHours`}} Number of hours of estimated wait for a user
       (`Math.floor(waitTime/60)`).
    5. {{`waitTimeHourMinutes`}} Number of minutes above the `waitTimeHours` value
       (`waitTime%60`).
    6. {{`queueIsFull`}} Changes to **true** when no more people can be added to the
       queue.

    To view the full list of variables, look at the `cfWaitingRoom` object described
    under the `json_response_enabled` property in other Waiting Room API calls.
    """
