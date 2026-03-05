# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust.devices import (
    IPProfile,
    IPProfileDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIPProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        ip_profile = client.zero_trust.devices.ip_profiles.create(
            account_id="account_id",
            match='identity.email == "test@cloudflare.com"',
            name="IPv4 Cloudflare Source IPs",
            precedence=100,
            subnet_id="b70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(IPProfile, ip_profile, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        ip_profile = client.zero_trust.devices.ip_profiles.create(
            account_id="account_id",
            match='identity.email == "test@cloudflare.com"',
            name="IPv4 Cloudflare Source IPs",
            precedence=100,
            subnet_id="b70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            description="example comment",
            enabled=True,
        )
        assert_matches_type(IPProfile, ip_profile, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.ip_profiles.with_raw_response.create(
            account_id="account_id",
            match='identity.email == "test@cloudflare.com"',
            name="IPv4 Cloudflare Source IPs",
            precedence=100,
            subnet_id="b70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_profile = response.parse()
        assert_matches_type(IPProfile, ip_profile, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.ip_profiles.with_streaming_response.create(
            account_id="account_id",
            match='identity.email == "test@cloudflare.com"',
            name="IPv4 Cloudflare Source IPs",
            precedence=100,
            subnet_id="b70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_profile = response.parse()
            assert_matches_type(IPProfile, ip_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.ip_profiles.with_raw_response.create(
                account_id="",
                match='identity.email == "test@cloudflare.com"',
                name="IPv4 Cloudflare Source IPs",
                precedence=100,
                subnet_id="b70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        ip_profile = client.zero_trust.devices.ip_profiles.update(
            profile_id="profile_id",
            account_id="account_id",
        )
        assert_matches_type(IPProfile, ip_profile, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        ip_profile = client.zero_trust.devices.ip_profiles.update(
            profile_id="profile_id",
            account_id="account_id",
            description="example comment",
            enabled=True,
            match='identity.email == "test@cloudflare.com"',
            name="IPv4 Cloudflare Source IPs",
            precedence=100,
            subnet_id="b70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(IPProfile, ip_profile, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.ip_profiles.with_raw_response.update(
            profile_id="profile_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_profile = response.parse()
        assert_matches_type(IPProfile, ip_profile, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.ip_profiles.with_streaming_response.update(
            profile_id="profile_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_profile = response.parse()
            assert_matches_type(IPProfile, ip_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.ip_profiles.with_raw_response.update(
                profile_id="profile_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.zero_trust.devices.ip_profiles.with_raw_response.update(
                profile_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        ip_profile = client.zero_trust.devices.ip_profiles.list(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[IPProfile], ip_profile, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        ip_profile = client.zero_trust.devices.ip_profiles.list(
            account_id="account_id",
            per_page=1,
        )
        assert_matches_type(SyncSinglePage[IPProfile], ip_profile, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.ip_profiles.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_profile = response.parse()
        assert_matches_type(SyncSinglePage[IPProfile], ip_profile, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.ip_profiles.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_profile = response.parse()
            assert_matches_type(SyncSinglePage[IPProfile], ip_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.ip_profiles.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        ip_profile = client.zero_trust.devices.ip_profiles.delete(
            profile_id="profile_id",
            account_id="account_id",
        )
        assert_matches_type(IPProfileDeleteResponse, ip_profile, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.ip_profiles.with_raw_response.delete(
            profile_id="profile_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_profile = response.parse()
        assert_matches_type(IPProfileDeleteResponse, ip_profile, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.ip_profiles.with_streaming_response.delete(
            profile_id="profile_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_profile = response.parse()
            assert_matches_type(IPProfileDeleteResponse, ip_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.ip_profiles.with_raw_response.delete(
                profile_id="profile_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.zero_trust.devices.ip_profiles.with_raw_response.delete(
                profile_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        ip_profile = client.zero_trust.devices.ip_profiles.get(
            profile_id="profile_id",
            account_id="account_id",
        )
        assert_matches_type(IPProfile, ip_profile, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.ip_profiles.with_raw_response.get(
            profile_id="profile_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_profile = response.parse()
        assert_matches_type(IPProfile, ip_profile, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.ip_profiles.with_streaming_response.get(
            profile_id="profile_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_profile = response.parse()
            assert_matches_type(IPProfile, ip_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.ip_profiles.with_raw_response.get(
                profile_id="profile_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.zero_trust.devices.ip_profiles.with_raw_response.get(
                profile_id="",
                account_id="account_id",
            )


class TestAsyncIPProfiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        ip_profile = await async_client.zero_trust.devices.ip_profiles.create(
            account_id="account_id",
            match='identity.email == "test@cloudflare.com"',
            name="IPv4 Cloudflare Source IPs",
            precedence=100,
            subnet_id="b70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(IPProfile, ip_profile, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ip_profile = await async_client.zero_trust.devices.ip_profiles.create(
            account_id="account_id",
            match='identity.email == "test@cloudflare.com"',
            name="IPv4 Cloudflare Source IPs",
            precedence=100,
            subnet_id="b70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            description="example comment",
            enabled=True,
        )
        assert_matches_type(IPProfile, ip_profile, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.ip_profiles.with_raw_response.create(
            account_id="account_id",
            match='identity.email == "test@cloudflare.com"',
            name="IPv4 Cloudflare Source IPs",
            precedence=100,
            subnet_id="b70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_profile = await response.parse()
        assert_matches_type(IPProfile, ip_profile, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.ip_profiles.with_streaming_response.create(
            account_id="account_id",
            match='identity.email == "test@cloudflare.com"',
            name="IPv4 Cloudflare Source IPs",
            precedence=100,
            subnet_id="b70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_profile = await response.parse()
            assert_matches_type(IPProfile, ip_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.ip_profiles.with_raw_response.create(
                account_id="",
                match='identity.email == "test@cloudflare.com"',
                name="IPv4 Cloudflare Source IPs",
                precedence=100,
                subnet_id="b70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        ip_profile = await async_client.zero_trust.devices.ip_profiles.update(
            profile_id="profile_id",
            account_id="account_id",
        )
        assert_matches_type(IPProfile, ip_profile, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ip_profile = await async_client.zero_trust.devices.ip_profiles.update(
            profile_id="profile_id",
            account_id="account_id",
            description="example comment",
            enabled=True,
            match='identity.email == "test@cloudflare.com"',
            name="IPv4 Cloudflare Source IPs",
            precedence=100,
            subnet_id="b70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(IPProfile, ip_profile, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.ip_profiles.with_raw_response.update(
            profile_id="profile_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_profile = await response.parse()
        assert_matches_type(IPProfile, ip_profile, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.ip_profiles.with_streaming_response.update(
            profile_id="profile_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_profile = await response.parse()
            assert_matches_type(IPProfile, ip_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.ip_profiles.with_raw_response.update(
                profile_id="profile_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.zero_trust.devices.ip_profiles.with_raw_response.update(
                profile_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        ip_profile = await async_client.zero_trust.devices.ip_profiles.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[IPProfile], ip_profile, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ip_profile = await async_client.zero_trust.devices.ip_profiles.list(
            account_id="account_id",
            per_page=1,
        )
        assert_matches_type(AsyncSinglePage[IPProfile], ip_profile, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.ip_profiles.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_profile = await response.parse()
        assert_matches_type(AsyncSinglePage[IPProfile], ip_profile, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.ip_profiles.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_profile = await response.parse()
            assert_matches_type(AsyncSinglePage[IPProfile], ip_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.ip_profiles.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        ip_profile = await async_client.zero_trust.devices.ip_profiles.delete(
            profile_id="profile_id",
            account_id="account_id",
        )
        assert_matches_type(IPProfileDeleteResponse, ip_profile, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.ip_profiles.with_raw_response.delete(
            profile_id="profile_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_profile = await response.parse()
        assert_matches_type(IPProfileDeleteResponse, ip_profile, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.ip_profiles.with_streaming_response.delete(
            profile_id="profile_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_profile = await response.parse()
            assert_matches_type(IPProfileDeleteResponse, ip_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.ip_profiles.with_raw_response.delete(
                profile_id="profile_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.zero_trust.devices.ip_profiles.with_raw_response.delete(
                profile_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        ip_profile = await async_client.zero_trust.devices.ip_profiles.get(
            profile_id="profile_id",
            account_id="account_id",
        )
        assert_matches_type(IPProfile, ip_profile, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.ip_profiles.with_raw_response.get(
            profile_id="profile_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_profile = await response.parse()
        assert_matches_type(IPProfile, ip_profile, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.ip_profiles.with_streaming_response.get(
            profile_id="profile_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_profile = await response.parse()
            assert_matches_type(IPProfile, ip_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.ip_profiles.with_raw_response.get(
                profile_id="profile_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.zero_trust.devices.ip_profiles.with_raw_response.get(
                profile_id="",
                account_id="account_id",
            )
