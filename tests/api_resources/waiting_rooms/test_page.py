# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.waiting_rooms import PagePreviewResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_preview(self, client: Cloudflare) -> None:
        page = client.waiting_rooms.page.preview(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="{{#waitTimeKnown}} {{waitTime}} mins {{/waitTimeKnown}} {{^waitTimeKnown}} Queue all enabled {{/waitTimeKnown}}",
        )
        assert_matches_type(PagePreviewResponse, page, path=["response"])

    @parametrize
    def test_raw_response_preview(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.page.with_raw_response.preview(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="{{#waitTimeKnown}} {{waitTime}} mins {{/waitTimeKnown}} {{^waitTimeKnown}} Queue all enabled {{/waitTimeKnown}}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(PagePreviewResponse, page, path=["response"])

    @parametrize
    def test_streaming_response_preview(self, client: Cloudflare) -> None:
        with client.waiting_rooms.page.with_streaming_response.preview(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="{{#waitTimeKnown}} {{waitTime}} mins {{/waitTimeKnown}} {{^waitTimeKnown}} Queue all enabled {{/waitTimeKnown}}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(PagePreviewResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_preview(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.waiting_rooms.page.with_raw_response.preview(
                zone_id="",
                custom_html="{{#waitTimeKnown}} {{waitTime}} mins {{/waitTimeKnown}} {{^waitTimeKnown}} Queue all enabled {{/waitTimeKnown}}",
            )


class TestAsyncPage:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_preview(self, async_client: AsyncCloudflare) -> None:
        page = await async_client.waiting_rooms.page.preview(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="{{#waitTimeKnown}} {{waitTime}} mins {{/waitTimeKnown}} {{^waitTimeKnown}} Queue all enabled {{/waitTimeKnown}}",
        )
        assert_matches_type(PagePreviewResponse, page, path=["response"])

    @parametrize
    async def test_raw_response_preview(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.page.with_raw_response.preview(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="{{#waitTimeKnown}} {{waitTime}} mins {{/waitTimeKnown}} {{^waitTimeKnown}} Queue all enabled {{/waitTimeKnown}}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(PagePreviewResponse, page, path=["response"])

    @parametrize
    async def test_streaming_response_preview(self, async_client: AsyncCloudflare) -> None:
        async with async_client.waiting_rooms.page.with_streaming_response.preview(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="{{#waitTimeKnown}} {{waitTime}} mins {{/waitTimeKnown}} {{^waitTimeKnown}} Queue all enabled {{/waitTimeKnown}}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(PagePreviewResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_preview(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.waiting_rooms.page.with_raw_response.preview(
                zone_id="",
                custom_html="{{#waitTimeKnown}} {{waitTime}} mins {{/waitTimeKnown}} {{^waitTimeKnown}} Queue all enabled {{/waitTimeKnown}}",
            )
