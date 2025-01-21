# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.page_shield import script_list_params
from ...types.page_shield.script import Script
from ...types.page_shield.script_get_response import ScriptGetResponse

__all__ = ["ScriptsResource", "AsyncScriptsResource"]


class ScriptsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScriptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ScriptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScriptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ScriptsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        zone_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        exclude_cdn_cgi: bool | NotGiven = NOT_GIVEN,
        exclude_duplicates: bool | NotGiven = NOT_GIVEN,
        exclude_urls: str | NotGiven = NOT_GIVEN,
        export: Literal["csv"] | NotGiven = NOT_GIVEN,
        hosts: str | NotGiven = NOT_GIVEN,
        order_by: Literal["first_seen_at", "last_seen_at"] | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        page_url: str | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        prioritize_malicious: bool | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        urls: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[Script]:
        """
        Lists all scripts detected by Page Shield.

        Args:
          zone_id: Identifier

          direction: The direction used to sort returned scripts.

          exclude_cdn_cgi: When true, excludes scripts seen in a `/cdn-cgi` path from the returned scripts.
              The default value is true.

          exclude_duplicates: When true, excludes duplicate scripts. We consider a script duplicate of another
              if their javascript content matches and they share the same url host and zone
              hostname. In such case, we return the most recent script for the URL host and
              zone hostname combination.

          exclude_urls: Excludes scripts whose URL contains one of the URL-encoded URLs separated by
              commas.

          export: Export the list of scripts as a file.

          hosts: Includes scripts that match one or more URL-encoded hostnames separated by
              commas.

              Wildcards are supported at the start and end of each hostname to support starts
              with, ends with and contains. If no wildcards are used, results will be filtered
              by exact match

          order_by: The field used to sort returned scripts.

          page: The current page number of the paginated results.

              We additionally support a special value "all". When "all" is used, the API will
              return all the scripts with the applied filters in a single page. This feature
              is best-effort and it may only work for zones with a low number of scripts

          page_url: Includes scripts that match one or more page URLs (separated by commas) where
              they were last seen

              Wildcards are supported at the start and end of each page URL to support starts
              with, ends with and contains. If no wildcards are used, results will be filtered
              by exact match

          per_page: The number of results per page.

          prioritize_malicious: When true, malicious scripts appear first in the returned scripts.

          status: Filters the returned scripts using a comma-separated list of scripts statuses.
              Accepted values: `active`, `infrequent`, and `inactive`. The default value is
              `active`.

          urls: Includes scripts whose URL contain one or more URL-encoded URLs separated by
              commas.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/page_shield/scripts",
            page=SyncSinglePage[Script],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "exclude_cdn_cgi": exclude_cdn_cgi,
                        "exclude_duplicates": exclude_duplicates,
                        "exclude_urls": exclude_urls,
                        "export": export,
                        "hosts": hosts,
                        "order_by": order_by,
                        "page": page,
                        "page_url": page_url,
                        "per_page": per_page,
                        "prioritize_malicious": prioritize_malicious,
                        "status": status,
                        "urls": urls,
                    },
                    script_list_params.ScriptListParams,
                ),
            ),
            model=Script,
        )

    def get(
        self,
        script_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ScriptGetResponse]:
        """
        Fetches a script detected by Page Shield by script ID.

        Args:
          zone_id: Identifier

          script_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not script_id:
            raise ValueError(f"Expected a non-empty value for `script_id` but received {script_id!r}")
        return self._get(
            f"/zones/{zone_id}/page_shield/scripts/{script_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ScriptGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ScriptGetResponse]], ResultWrapper[ScriptGetResponse]),
        )


class AsyncScriptsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScriptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScriptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScriptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncScriptsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        zone_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        exclude_cdn_cgi: bool | NotGiven = NOT_GIVEN,
        exclude_duplicates: bool | NotGiven = NOT_GIVEN,
        exclude_urls: str | NotGiven = NOT_GIVEN,
        export: Literal["csv"] | NotGiven = NOT_GIVEN,
        hosts: str | NotGiven = NOT_GIVEN,
        order_by: Literal["first_seen_at", "last_seen_at"] | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        page_url: str | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        prioritize_malicious: bool | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        urls: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Script, AsyncSinglePage[Script]]:
        """
        Lists all scripts detected by Page Shield.

        Args:
          zone_id: Identifier

          direction: The direction used to sort returned scripts.

          exclude_cdn_cgi: When true, excludes scripts seen in a `/cdn-cgi` path from the returned scripts.
              The default value is true.

          exclude_duplicates: When true, excludes duplicate scripts. We consider a script duplicate of another
              if their javascript content matches and they share the same url host and zone
              hostname. In such case, we return the most recent script for the URL host and
              zone hostname combination.

          exclude_urls: Excludes scripts whose URL contains one of the URL-encoded URLs separated by
              commas.

          export: Export the list of scripts as a file.

          hosts: Includes scripts that match one or more URL-encoded hostnames separated by
              commas.

              Wildcards are supported at the start and end of each hostname to support starts
              with, ends with and contains. If no wildcards are used, results will be filtered
              by exact match

          order_by: The field used to sort returned scripts.

          page: The current page number of the paginated results.

              We additionally support a special value "all". When "all" is used, the API will
              return all the scripts with the applied filters in a single page. This feature
              is best-effort and it may only work for zones with a low number of scripts

          page_url: Includes scripts that match one or more page URLs (separated by commas) where
              they were last seen

              Wildcards are supported at the start and end of each page URL to support starts
              with, ends with and contains. If no wildcards are used, results will be filtered
              by exact match

          per_page: The number of results per page.

          prioritize_malicious: When true, malicious scripts appear first in the returned scripts.

          status: Filters the returned scripts using a comma-separated list of scripts statuses.
              Accepted values: `active`, `infrequent`, and `inactive`. The default value is
              `active`.

          urls: Includes scripts whose URL contain one or more URL-encoded URLs separated by
              commas.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/page_shield/scripts",
            page=AsyncSinglePage[Script],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "exclude_cdn_cgi": exclude_cdn_cgi,
                        "exclude_duplicates": exclude_duplicates,
                        "exclude_urls": exclude_urls,
                        "export": export,
                        "hosts": hosts,
                        "order_by": order_by,
                        "page": page,
                        "page_url": page_url,
                        "per_page": per_page,
                        "prioritize_malicious": prioritize_malicious,
                        "status": status,
                        "urls": urls,
                    },
                    script_list_params.ScriptListParams,
                ),
            ),
            model=Script,
        )

    async def get(
        self,
        script_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ScriptGetResponse]:
        """
        Fetches a script detected by Page Shield by script ID.

        Args:
          zone_id: Identifier

          script_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not script_id:
            raise ValueError(f"Expected a non-empty value for `script_id` but received {script_id!r}")
        return await self._get(
            f"/zones/{zone_id}/page_shield/scripts/{script_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ScriptGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ScriptGetResponse]], ResultWrapper[ScriptGetResponse]),
        )


class ScriptsResourceWithRawResponse:
    def __init__(self, scripts: ScriptsResource) -> None:
        self._scripts = scripts

        self.list = to_raw_response_wrapper(
            scripts.list,
        )
        self.get = to_raw_response_wrapper(
            scripts.get,
        )


class AsyncScriptsResourceWithRawResponse:
    def __init__(self, scripts: AsyncScriptsResource) -> None:
        self._scripts = scripts

        self.list = async_to_raw_response_wrapper(
            scripts.list,
        )
        self.get = async_to_raw_response_wrapper(
            scripts.get,
        )


class ScriptsResourceWithStreamingResponse:
    def __init__(self, scripts: ScriptsResource) -> None:
        self._scripts = scripts

        self.list = to_streamed_response_wrapper(
            scripts.list,
        )
        self.get = to_streamed_response_wrapper(
            scripts.get,
        )


class AsyncScriptsResourceWithStreamingResponse:
    def __init__(self, scripts: AsyncScriptsResource) -> None:
        self._scripts = scripts

        self.list = async_to_streamed_response_wrapper(
            scripts.list,
        )
        self.get = async_to_streamed_response_wrapper(
            scripts.get,
        )
