# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.access import (
    IdPFederationGrant,
    IdPFederationGrantListResponse,
    IdPFederationGrantDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIdPFederationGrants:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        idp_federation_grant = client.zero_trust.access.idp_federation_grants.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            idp_id="a79de439-0e7f-4ebb-8a02-222222222222",
        )
        assert_matches_type(Optional[IdPFederationGrant], idp_federation_grant, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.idp_federation_grants.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            idp_id="a79de439-0e7f-4ebb-8a02-222222222222",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        idp_federation_grant = response.parse()
        assert_matches_type(Optional[IdPFederationGrant], idp_federation_grant, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.access.idp_federation_grants.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            idp_id="a79de439-0e7f-4ebb-8a02-222222222222",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            idp_federation_grant = response.parse()
            assert_matches_type(Optional[IdPFederationGrant], idp_federation_grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.idp_federation_grants.with_raw_response.create(
                account_id="",
                idp_id="a79de439-0e7f-4ebb-8a02-222222222222",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        idp_federation_grant = client.zero_trust.access.idp_federation_grants.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IdPFederationGrantListResponse], idp_federation_grant, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.idp_federation_grants.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        idp_federation_grant = response.parse()
        assert_matches_type(Optional[IdPFederationGrantListResponse], idp_federation_grant, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.access.idp_federation_grants.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            idp_federation_grant = response.parse()
            assert_matches_type(Optional[IdPFederationGrantListResponse], idp_federation_grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.idp_federation_grants.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        idp_federation_grant = client.zero_trust.access.idp_federation_grants.delete(
            grant_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IdPFederationGrantDeleteResponse], idp_federation_grant, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.idp_federation_grants.with_raw_response.delete(
            grant_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        idp_federation_grant = response.parse()
        assert_matches_type(Optional[IdPFederationGrantDeleteResponse], idp_federation_grant, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.access.idp_federation_grants.with_streaming_response.delete(
            grant_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            idp_federation_grant = response.parse()
            assert_matches_type(Optional[IdPFederationGrantDeleteResponse], idp_federation_grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.idp_federation_grants.with_raw_response.delete(
                grant_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `grant_id` but received ''"):
            client.zero_trust.access.idp_federation_grants.with_raw_response.delete(
                grant_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        idp_federation_grant = client.zero_trust.access.idp_federation_grants.get(
            grant_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IdPFederationGrant], idp_federation_grant, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.idp_federation_grants.with_raw_response.get(
            grant_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        idp_federation_grant = response.parse()
        assert_matches_type(Optional[IdPFederationGrant], idp_federation_grant, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.access.idp_federation_grants.with_streaming_response.get(
            grant_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            idp_federation_grant = response.parse()
            assert_matches_type(Optional[IdPFederationGrant], idp_federation_grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.idp_federation_grants.with_raw_response.get(
                grant_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `grant_id` but received ''"):
            client.zero_trust.access.idp_federation_grants.with_raw_response.get(
                grant_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncIdPFederationGrants:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        idp_federation_grant = await async_client.zero_trust.access.idp_federation_grants.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            idp_id="a79de439-0e7f-4ebb-8a02-222222222222",
        )
        assert_matches_type(Optional[IdPFederationGrant], idp_federation_grant, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.idp_federation_grants.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            idp_id="a79de439-0e7f-4ebb-8a02-222222222222",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        idp_federation_grant = await response.parse()
        assert_matches_type(Optional[IdPFederationGrant], idp_federation_grant, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.idp_federation_grants.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            idp_id="a79de439-0e7f-4ebb-8a02-222222222222",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            idp_federation_grant = await response.parse()
            assert_matches_type(Optional[IdPFederationGrant], idp_federation_grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.idp_federation_grants.with_raw_response.create(
                account_id="",
                idp_id="a79de439-0e7f-4ebb-8a02-222222222222",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        idp_federation_grant = await async_client.zero_trust.access.idp_federation_grants.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IdPFederationGrantListResponse], idp_federation_grant, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.idp_federation_grants.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        idp_federation_grant = await response.parse()
        assert_matches_type(Optional[IdPFederationGrantListResponse], idp_federation_grant, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.idp_federation_grants.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            idp_federation_grant = await response.parse()
            assert_matches_type(Optional[IdPFederationGrantListResponse], idp_federation_grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.idp_federation_grants.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        idp_federation_grant = await async_client.zero_trust.access.idp_federation_grants.delete(
            grant_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IdPFederationGrantDeleteResponse], idp_federation_grant, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.idp_federation_grants.with_raw_response.delete(
            grant_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        idp_federation_grant = await response.parse()
        assert_matches_type(Optional[IdPFederationGrantDeleteResponse], idp_federation_grant, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.idp_federation_grants.with_streaming_response.delete(
            grant_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            idp_federation_grant = await response.parse()
            assert_matches_type(Optional[IdPFederationGrantDeleteResponse], idp_federation_grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.idp_federation_grants.with_raw_response.delete(
                grant_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `grant_id` but received ''"):
            await async_client.zero_trust.access.idp_federation_grants.with_raw_response.delete(
                grant_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        idp_federation_grant = await async_client.zero_trust.access.idp_federation_grants.get(
            grant_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IdPFederationGrant], idp_federation_grant, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.idp_federation_grants.with_raw_response.get(
            grant_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        idp_federation_grant = await response.parse()
        assert_matches_type(Optional[IdPFederationGrant], idp_federation_grant, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.idp_federation_grants.with_streaming_response.get(
            grant_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            idp_federation_grant = await response.parse()
            assert_matches_type(Optional[IdPFederationGrant], idp_federation_grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.idp_federation_grants.with_raw_response.get(
                grant_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `grant_id` but received ''"):
            await async_client.zero_trust.access.idp_federation_grants.with_raw_response.get(
                grant_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
