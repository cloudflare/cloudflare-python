# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.magic_cloud_networking import (
    ResourceGetResponse,
    ResourceListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResources:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        resource = client.magic_cloud_networking.resources.list(
            account_id="account_id",
        )
        assert_matches_type(SyncV4PagePaginationArray[ResourceListResponse], resource, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        resource = client.magic_cloud_networking.resources.list(
            account_id="account_id",
            cloudflare=True,
            desc=True,
            managed=True,
            order_by="order_by",
            page=1,
            per_page=1,
            provider_id="provider_id",
            region="region",
            resource_group="resource_group",
            resource_id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            resource_type=["aws_customer_gateway"],
            search=["string"],
            v2=True,
        )
        assert_matches_type(SyncV4PagePaginationArray[ResourceListResponse], resource, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.resources.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[ResourceListResponse], resource, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.resources.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[ResourceListResponse], resource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.resources.with_raw_response.list(
                account_id="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/account_id/magic/cloud/resources/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        resource = client.magic_cloud_networking.resources.export(
            account_id="account_id",
        )
        assert resource.is_closed
        assert resource.json() == {"foo": "bar"}
        assert cast(Any, resource.is_closed) is True
        assert isinstance(resource, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_with_all_params(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/account_id/magic/cloud/resources/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        resource = client.magic_cloud_networking.resources.export(
            account_id="account_id",
            desc=True,
            order_by="order_by",
            provider_id="provider_id",
            region="region",
            resource_group="resource_group",
            resource_id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            resource_type=["aws_customer_gateway"],
            search=["string"],
            v2=True,
        )
        assert resource.is_closed
        assert resource.json() == {"foo": "bar"}
        assert cast(Any, resource.is_closed) is True
        assert isinstance(resource, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_export(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/account_id/magic/cloud/resources/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        resource = client.magic_cloud_networking.resources.with_raw_response.export(
            account_id="account_id",
        )

        assert resource.is_closed is True
        assert resource.http_request.headers.get("X-Stainless-Lang") == "python"
        assert resource.json() == {"foo": "bar"}
        assert isinstance(resource, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_export(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/account_id/magic/cloud/resources/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.magic_cloud_networking.resources.with_streaming_response.export(
            account_id="account_id",
        ) as resource:
            assert not resource.is_closed
            assert resource.http_request.headers.get("X-Stainless-Lang") == "python"

            assert resource.json() == {"foo": "bar"}
            assert cast(Any, resource.is_closed) is True
            assert isinstance(resource, StreamedBinaryAPIResponse)

        assert cast(Any, resource.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_export(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.resources.with_raw_response.export(
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        resource = client.magic_cloud_networking.resources.get(
            resource_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(ResourceGetResponse, resource, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        resource = client.magic_cloud_networking.resources.get(
            resource_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            v2=True,
        )
        assert_matches_type(ResourceGetResponse, resource, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.resources.with_raw_response.get(
            resource_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource = response.parse()
        assert_matches_type(ResourceGetResponse, resource, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.resources.with_streaming_response.get(
            resource_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource = response.parse()
            assert_matches_type(ResourceGetResponse, resource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.resources.with_raw_response.get(
                resource_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_id` but received ''"):
            client.magic_cloud_networking.resources.with_raw_response.get(
                resource_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_policy_preview(self, client: Cloudflare) -> None:
        resource = client.magic_cloud_networking.resources.policy_preview(
            account_id="account_id",
            policy="policy",
        )
        assert_matches_type(str, resource, path=["response"])

    @parametrize
    def test_raw_response_policy_preview(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.resources.with_raw_response.policy_preview(
            account_id="account_id",
            policy="policy",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource = response.parse()
        assert_matches_type(str, resource, path=["response"])

    @parametrize
    def test_streaming_response_policy_preview(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.resources.with_streaming_response.policy_preview(
            account_id="account_id",
            policy="policy",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource = response.parse()
            assert_matches_type(str, resource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_policy_preview(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.resources.with_raw_response.policy_preview(
                account_id="",
                policy="policy",
            )


class TestAsyncResources:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        resource = await async_client.magic_cloud_networking.resources.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncV4PagePaginationArray[ResourceListResponse], resource, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        resource = await async_client.magic_cloud_networking.resources.list(
            account_id="account_id",
            cloudflare=True,
            desc=True,
            managed=True,
            order_by="order_by",
            page=1,
            per_page=1,
            provider_id="provider_id",
            region="region",
            resource_group="resource_group",
            resource_id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            resource_type=["aws_customer_gateway"],
            search=["string"],
            v2=True,
        )
        assert_matches_type(AsyncV4PagePaginationArray[ResourceListResponse], resource, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.resources.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[ResourceListResponse], resource, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.resources.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[ResourceListResponse], resource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.resources.with_raw_response.list(
                account_id="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/account_id/magic/cloud/resources/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        resource = await async_client.magic_cloud_networking.resources.export(
            account_id="account_id",
        )
        assert resource.is_closed
        assert await resource.json() == {"foo": "bar"}
        assert cast(Any, resource.is_closed) is True
        assert isinstance(resource, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_with_all_params(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/account_id/magic/cloud/resources/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        resource = await async_client.magic_cloud_networking.resources.export(
            account_id="account_id",
            desc=True,
            order_by="order_by",
            provider_id="provider_id",
            region="region",
            resource_group="resource_group",
            resource_id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            resource_type=["aws_customer_gateway"],
            search=["string"],
            v2=True,
        )
        assert resource.is_closed
        assert await resource.json() == {"foo": "bar"}
        assert cast(Any, resource.is_closed) is True
        assert isinstance(resource, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_export(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/account_id/magic/cloud/resources/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        resource = await async_client.magic_cloud_networking.resources.with_raw_response.export(
            account_id="account_id",
        )

        assert resource.is_closed is True
        assert resource.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await resource.json() == {"foo": "bar"}
        assert isinstance(resource, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_export(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/account_id/magic/cloud/resources/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.magic_cloud_networking.resources.with_streaming_response.export(
            account_id="account_id",
        ) as resource:
            assert not resource.is_closed
            assert resource.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await resource.json() == {"foo": "bar"}
            assert cast(Any, resource.is_closed) is True
            assert isinstance(resource, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, resource.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_export(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.resources.with_raw_response.export(
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        resource = await async_client.magic_cloud_networking.resources.get(
            resource_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(ResourceGetResponse, resource, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        resource = await async_client.magic_cloud_networking.resources.get(
            resource_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            v2=True,
        )
        assert_matches_type(ResourceGetResponse, resource, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.resources.with_raw_response.get(
            resource_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource = await response.parse()
        assert_matches_type(ResourceGetResponse, resource, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.resources.with_streaming_response.get(
            resource_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource = await response.parse()
            assert_matches_type(ResourceGetResponse, resource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.resources.with_raw_response.get(
                resource_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource_id` but received ''"):
            await async_client.magic_cloud_networking.resources.with_raw_response.get(
                resource_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_policy_preview(self, async_client: AsyncCloudflare) -> None:
        resource = await async_client.magic_cloud_networking.resources.policy_preview(
            account_id="account_id",
            policy="policy",
        )
        assert_matches_type(str, resource, path=["response"])

    @parametrize
    async def test_raw_response_policy_preview(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.resources.with_raw_response.policy_preview(
            account_id="account_id",
            policy="policy",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource = await response.parse()
        assert_matches_type(str, resource, path=["response"])

    @parametrize
    async def test_streaming_response_policy_preview(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.resources.with_streaming_response.policy_preview(
            account_id="account_id",
            policy="policy",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource = await response.parse()
            assert_matches_type(str, resource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_policy_preview(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.resources.with_raw_response.policy_preview(
                account_id="",
                policy="policy",
            )
