# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.users.load_balancers import PreviewGetResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPreviews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        preview = client.users.load_balancers.previews.get(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        )
        assert_matches_type(PreviewGetResponse, preview, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.users.load_balancers.previews.with_raw_response.get(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = response.parse()
        assert_matches_type(PreviewGetResponse, preview, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.users.load_balancers.previews.with_streaming_response.get(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = response.parse()
            assert_matches_type(PreviewGetResponse, preview, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPreviews:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        preview = await async_client.users.load_balancers.previews.get(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        )
        assert_matches_type(PreviewGetResponse, preview, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.load_balancers.previews.with_raw_response.get(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = await response.parse()
        assert_matches_type(PreviewGetResponse, preview, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.users.load_balancers.previews.with_streaming_response.get(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = await response.parse()
            assert_matches_type(PreviewGetResponse, preview, path=["response"])

        assert cast(Any, response.is_closed) is True
