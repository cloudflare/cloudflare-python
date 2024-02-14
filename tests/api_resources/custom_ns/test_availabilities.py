# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.custom_ns import AvailabilityGetResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAvailabilities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        availability = client.custom_ns.availabilities.get(
            "372e67954025e0ba6aaa6d586b9e0b59",
        )
        assert_matches_type(Optional[AvailabilityGetResponse], availability, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.custom_ns.availabilities.with_raw_response.get(
            "372e67954025e0ba6aaa6d586b9e0b59",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        availability = response.parse()
        assert_matches_type(Optional[AvailabilityGetResponse], availability, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.custom_ns.availabilities.with_streaming_response.get(
            "372e67954025e0ba6aaa6d586b9e0b59",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            availability = response.parse()
            assert_matches_type(Optional[AvailabilityGetResponse], availability, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.custom_ns.availabilities.with_raw_response.get(
                "",
            )


class TestAsyncAvailabilities:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        availability = await async_client.custom_ns.availabilities.get(
            "372e67954025e0ba6aaa6d586b9e0b59",
        )
        assert_matches_type(Optional[AvailabilityGetResponse], availability, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_ns.availabilities.with_raw_response.get(
            "372e67954025e0ba6aaa6d586b9e0b59",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        availability = await response.parse()
        assert_matches_type(Optional[AvailabilityGetResponse], availability, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_ns.availabilities.with_streaming_response.get(
            "372e67954025e0ba6aaa6d586b9e0b59",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            availability = await response.parse()
            assert_matches_type(Optional[AvailabilityGetResponse], availability, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.custom_ns.availabilities.with_raw_response.get(
                "",
            )
