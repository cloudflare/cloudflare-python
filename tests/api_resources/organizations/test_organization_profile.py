# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.organizations.organization_profile_get_params import Result

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganizationProfile:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        organization_profile = client.organizations.organization_profile.update(
            organization_id="organization_id",
            business_address="business_address",
            business_email="business_email",
            business_name="business_name",
            business_phone="business_phone",
            external_metadata="external_metadata",
        )
        assert organization_profile is None

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.organizations.organization_profile.with_raw_response.update(
            organization_id="organization_id",
            business_address="business_address",
            business_email="business_email",
            business_name="business_name",
            business_phone="business_phone",
            external_metadata="external_metadata",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization_profile = response.parse()
        assert organization_profile is None

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.organizations.organization_profile.with_streaming_response.update(
            organization_id="organization_id",
            business_address="business_address",
            business_email="business_email",
            business_name="business_name",
            business_phone="business_phone",
            external_metadata="external_metadata",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization_profile = response.parse()
            assert organization_profile is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.organization_profile.with_raw_response.update(
                organization_id="",
                business_address="business_address",
                business_email="business_email",
                business_name="business_name",
                business_phone="business_phone",
                external_metadata="external_metadata",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        organization_profile = client.organizations.organization_profile.get(
            "organization_id",
        )
        assert_matches_type(Result, organization_profile, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.organizations.organization_profile.with_raw_response.get(
            "organization_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization_profile = response.parse()
        assert_matches_type(Result, organization_profile, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.organizations.organization_profile.with_streaming_response.get(
            "organization_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization_profile = response.parse()
            assert_matches_type(Result, organization_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.organization_profile.with_raw_response.get(
                "",
            )


class TestAsyncOrganizationProfile:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        organization_profile = await async_client.organizations.organization_profile.update(
            organization_id="organization_id",
            business_address="business_address",
            business_email="business_email",
            business_name="business_name",
            business_phone="business_phone",
            external_metadata="external_metadata",
        )
        assert organization_profile is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.organizations.organization_profile.with_raw_response.update(
            organization_id="organization_id",
            business_address="business_address",
            business_email="business_email",
            business_name="business_name",
            business_phone="business_phone",
            external_metadata="external_metadata",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization_profile = await response.parse()
        assert organization_profile is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.organizations.organization_profile.with_streaming_response.update(
            organization_id="organization_id",
            business_address="business_address",
            business_email="business_email",
            business_name="business_name",
            business_phone="business_phone",
            external_metadata="external_metadata",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization_profile = await response.parse()
            assert organization_profile is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.organization_profile.with_raw_response.update(
                organization_id="",
                business_address="business_address",
                business_email="business_email",
                business_name="business_name",
                business_phone="business_phone",
                external_metadata="external_metadata",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        organization_profile = await async_client.organizations.organization_profile.get(
            "organization_id",
        )
        assert_matches_type(Result, organization_profile, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.organizations.organization_profile.with_raw_response.get(
            "organization_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization_profile = await response.parse()
        assert_matches_type(Result, organization_profile, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.organizations.organization_profile.with_streaming_response.get(
            "organization_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization_profile = await response.parse()
            assert_matches_type(Result, organization_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.organization_profile.with_raw_response.get(
                "",
            )
