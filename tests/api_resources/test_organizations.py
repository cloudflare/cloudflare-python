# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.organizations import (
    Organization,
    OrganizationDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        organization = client.organizations.create(
            name="name",
        )
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        organization = client.organizations.create(
            name="name",
            parent={"id": "a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8"},
            profile={
                "business_address": "business_address",
                "business_email": "business_email",
                "business_name": "business_name",
                "business_phone": "business_phone",
                "external_metadata": "external_metadata",
            },
        )
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.organizations.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.organizations.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(Organization, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        organization = client.organizations.update(
            organization_id="a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8",
            name="name",
        )
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        organization = client.organizations.update(
            organization_id="a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8",
            name="name",
            parent={"id": "a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8"},
            profile={
                "business_address": "business_address",
                "business_email": "business_email",
                "business_name": "business_name",
                "business_phone": "business_phone",
                "external_metadata": "external_metadata",
            },
        )
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.organizations.with_raw_response.update(
            organization_id="a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.organizations.with_streaming_response.update(
            organization_id="a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(Organization, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.with_raw_response.update(
                organization_id="",
                name="name",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        organization = client.organizations.list()
        assert_matches_type(SyncSinglePage[Organization], organization, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        organization = client.organizations.list(
            id=["a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8"],
            containing={
                "account": "account",
                "organization": "organization",
                "user": "user",
            },
            name={
                "contains": "contains",
                "ends_with": "endsWith",
                "starts_with": "startsWith",
            },
            page_size=0,
            page_token="page_token",
            parent={"id": "a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8"},
        )
        assert_matches_type(SyncSinglePage[Organization], organization, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.organizations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(SyncSinglePage[Organization], organization, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.organizations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(SyncSinglePage[Organization], organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        organization = client.organizations.delete(
            "a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8",
        )
        assert_matches_type(OrganizationDeleteResponse, organization, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.organizations.with_raw_response.delete(
            "a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationDeleteResponse, organization, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.organizations.with_streaming_response.delete(
            "a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationDeleteResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        organization = client.organizations.get(
            "a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8",
        )
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.organizations.with_raw_response.get(
            "a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.organizations.with_streaming_response.get(
            "a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(Organization, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.with_raw_response.get(
                "",
            )


class TestAsyncOrganizations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        organization = await async_client.organizations.create(
            name="name",
        )
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        organization = await async_client.organizations.create(
            name="name",
            parent={"id": "a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8"},
            profile={
                "business_address": "business_address",
                "business_email": "business_email",
                "business_name": "business_name",
                "business_phone": "business_phone",
                "external_metadata": "external_metadata",
            },
        )
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.organizations.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.organizations.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(Organization, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        organization = await async_client.organizations.update(
            organization_id="a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8",
            name="name",
        )
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        organization = await async_client.organizations.update(
            organization_id="a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8",
            name="name",
            parent={"id": "a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8"},
            profile={
                "business_address": "business_address",
                "business_email": "business_email",
                "business_name": "business_name",
                "business_phone": "business_phone",
                "external_metadata": "external_metadata",
            },
        )
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.organizations.with_raw_response.update(
            organization_id="a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.organizations.with_streaming_response.update(
            organization_id="a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(Organization, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.with_raw_response.update(
                organization_id="",
                name="name",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        organization = await async_client.organizations.list()
        assert_matches_type(AsyncSinglePage[Organization], organization, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        organization = await async_client.organizations.list(
            id=["a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8"],
            containing={
                "account": "account",
                "organization": "organization",
                "user": "user",
            },
            name={
                "contains": "contains",
                "ends_with": "endsWith",
                "starts_with": "startsWith",
            },
            page_size=0,
            page_token="page_token",
            parent={"id": "a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8"},
        )
        assert_matches_type(AsyncSinglePage[Organization], organization, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.organizations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(AsyncSinglePage[Organization], organization, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.organizations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(AsyncSinglePage[Organization], organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        organization = await async_client.organizations.delete(
            "a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8",
        )
        assert_matches_type(OrganizationDeleteResponse, organization, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.organizations.with_raw_response.delete(
            "a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationDeleteResponse, organization, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.organizations.with_streaming_response.delete(
            "a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationDeleteResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        organization = await async_client.organizations.get(
            "a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8",
        )
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.organizations.with_raw_response.get(
            "a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.organizations.with_streaming_response.get(
            "a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(Organization, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.with_raw_response.get(
                "",
            )
