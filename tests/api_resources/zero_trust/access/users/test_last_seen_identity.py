# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.access.users import AccessIdentity

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLastSeenIdentity:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        last_seen_identity = client.zero_trust.access.users.last_seen_identity.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AccessIdentity, last_seen_identity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.users.last_seen_identity.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        last_seen_identity = response.parse()
        assert_matches_type(AccessIdentity, last_seen_identity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.access.users.last_seen_identity.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            last_seen_identity = response.parse()
            assert_matches_type(AccessIdentity, last_seen_identity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.zero_trust.access.users.last_seen_identity.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zero_trust.access.users.last_seen_identity.with_raw_response.get(
                "",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncLastSeenIdentity:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        last_seen_identity = await async_client.zero_trust.access.users.last_seen_identity.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AccessIdentity, last_seen_identity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.users.last_seen_identity.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        last_seen_identity = await response.parse()
        assert_matches_type(AccessIdentity, last_seen_identity, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.users.last_seen_identity.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            last_seen_identity = await response.parse()
            assert_matches_type(AccessIdentity, last_seen_identity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.zero_trust.access.users.last_seen_identity.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zero_trust.access.users.last_seen_identity.with_raw_response.get(
                "",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )
