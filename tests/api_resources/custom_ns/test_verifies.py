# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.custom_ns import VerifyUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVerifies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        verify = client.custom_ns.verifies.update(
            "372e67954025e0ba6aaa6d586b9e0b59",
        )
        assert_matches_type(Optional[VerifyUpdateResponse], verify, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.custom_ns.verifies.with_raw_response.update(
            "372e67954025e0ba6aaa6d586b9e0b59",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify = response.parse()
        assert_matches_type(Optional[VerifyUpdateResponse], verify, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.custom_ns.verifies.with_streaming_response.update(
            "372e67954025e0ba6aaa6d586b9e0b59",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify = response.parse()
            assert_matches_type(Optional[VerifyUpdateResponse], verify, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.custom_ns.verifies.with_raw_response.update(
                "",
            )


class TestAsyncVerifies:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        verify = await async_client.custom_ns.verifies.update(
            "372e67954025e0ba6aaa6d586b9e0b59",
        )
        assert_matches_type(Optional[VerifyUpdateResponse], verify, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_ns.verifies.with_raw_response.update(
            "372e67954025e0ba6aaa6d586b9e0b59",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify = await response.parse()
        assert_matches_type(Optional[VerifyUpdateResponse], verify, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_ns.verifies.with_streaming_response.update(
            "372e67954025e0ba6aaa6d586b9e0b59",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify = await response.parse()
            assert_matches_type(Optional[VerifyUpdateResponse], verify, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.custom_ns.verifies.with_raw_response.update(
                "",
            )
