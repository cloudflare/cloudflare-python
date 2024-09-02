# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from cloudflare.types.radar.robots_txt.top import DirectiveGetResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar.robots_txt.top import directive_get_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDirective:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        directive = client.radar.robots_txt.top.directive.get(
            directive="ALLOW",
        )
        assert_matches_type(DirectiveGetResponse, directive, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        directive = client.radar.robots_txt.top.directive.get(
            directive="ALLOW",
            agent_category="AI",
            date="2024-09-19",
            format="JSON",
            limit=5,
            name=["string", "string", "string"],
        )
        assert_matches_type(DirectiveGetResponse, directive, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.radar.robots_txt.top.directive.with_raw_response.get(
            directive="ALLOW",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        directive = response.parse()
        assert_matches_type(DirectiveGetResponse, directive, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.radar.robots_txt.top.directive.with_streaming_response.get(
            directive="ALLOW",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            directive = response.parse()
            assert_matches_type(DirectiveGetResponse, directive, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDirective:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        directive = await async_client.radar.robots_txt.top.directive.get(
            directive="ALLOW",
        )
        assert_matches_type(DirectiveGetResponse, directive, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        directive = await async_client.radar.robots_txt.top.directive.get(
            directive="ALLOW",
            agent_category="AI",
            date="2024-09-19",
            format="JSON",
            limit=5,
            name=["string", "string", "string"],
        )
        assert_matches_type(DirectiveGetResponse, directive, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.robots_txt.top.directive.with_raw_response.get(
            directive="ALLOW",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        directive = await response.parse()
        assert_matches_type(DirectiveGetResponse, directive, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.robots_txt.top.directive.with_streaming_response.get(
            directive="ALLOW",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            directive = await response.parse()
            assert_matches_type(DirectiveGetResponse, directive, path=["response"])

        assert cast(Any, response.is_closed) is True
