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
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.magic_cloud_networking import (
    OnRampGetResponse,
    OnRampEditResponse,
    OnRampListResponse,
    OnRampPlanResponse,
    OnRampApplyResponse,
    OnRampCreateResponse,
    OnRampDeleteResponse,
    OnRampUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOnRamps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        on_ramp = client.magic_cloud_networking.on_ramps.create(
            account_id="account_id",
            cloud_type="AWS",
            install_routes_in_cloud=True,
            install_routes_in_magic_wan=True,
            name="name",
            type="OnrampTypeSingle",
        )
        assert_matches_type(OnRampCreateResponse, on_ramp, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        on_ramp = client.magic_cloud_networking.on_ramps.create(
            account_id="account_id",
            cloud_type="AWS",
            install_routes_in_cloud=True,
            install_routes_in_magic_wan=True,
            name="name",
            type="OnrampTypeSingle",
            adopted_hub_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            attached_hubs=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            attached_vpcs=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            description="description",
            hub_provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            manage_hub_to_hub_attachments=True,
            manage_vpc_to_hub_attachments=True,
            region="region",
            vpc="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            forwarded="forwarded",
        )
        assert_matches_type(OnRampCreateResponse, on_ramp, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.on_ramps.with_raw_response.create(
            account_id="account_id",
            cloud_type="AWS",
            install_routes_in_cloud=True,
            install_routes_in_magic_wan=True,
            name="name",
            type="OnrampTypeSingle",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        on_ramp = response.parse()
        assert_matches_type(OnRampCreateResponse, on_ramp, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.on_ramps.with_streaming_response.create(
            account_id="account_id",
            cloud_type="AWS",
            install_routes_in_cloud=True,
            install_routes_in_magic_wan=True,
            name="name",
            type="OnrampTypeSingle",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            on_ramp = response.parse()
            assert_matches_type(OnRampCreateResponse, on_ramp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.on_ramps.with_raw_response.create(
                account_id="",
                cloud_type="AWS",
                install_routes_in_cloud=True,
                install_routes_in_magic_wan=True,
                name="name",
                type="OnrampTypeSingle",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        on_ramp = client.magic_cloud_networking.on_ramps.update(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(OnRampUpdateResponse, on_ramp, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        on_ramp = client.magic_cloud_networking.on_ramps.update(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            attached_hubs=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            attached_vpcs=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            description="description",
            install_routes_in_cloud=True,
            install_routes_in_magic_wan=True,
            manage_hub_to_hub_attachments=True,
            manage_vpc_to_hub_attachments=True,
            name="name",
            vpc="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OnRampUpdateResponse, on_ramp, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.on_ramps.with_raw_response.update(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        on_ramp = response.parse()
        assert_matches_type(OnRampUpdateResponse, on_ramp, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.on_ramps.with_streaming_response.update(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            on_ramp = response.parse()
            assert_matches_type(OnRampUpdateResponse, on_ramp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.on_ramps.with_raw_response.update(
                onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `onramp_id` but received ''"):
            client.magic_cloud_networking.on_ramps.with_raw_response.update(
                onramp_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        on_ramp = client.magic_cloud_networking.on_ramps.list(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[OnRampListResponse], on_ramp, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        on_ramp = client.magic_cloud_networking.on_ramps.list(
            account_id="account_id",
            desc=True,
            order_by="order_by",
            status=True,
            vpcs=True,
        )
        assert_matches_type(SyncSinglePage[OnRampListResponse], on_ramp, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.on_ramps.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        on_ramp = response.parse()
        assert_matches_type(SyncSinglePage[OnRampListResponse], on_ramp, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.on_ramps.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            on_ramp = response.parse()
            assert_matches_type(SyncSinglePage[OnRampListResponse], on_ramp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.on_ramps.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        on_ramp = client.magic_cloud_networking.on_ramps.delete(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(OnRampDeleteResponse, on_ramp, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        on_ramp = client.magic_cloud_networking.on_ramps.delete(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            destroy=True,
            force=True,
        )
        assert_matches_type(OnRampDeleteResponse, on_ramp, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.on_ramps.with_raw_response.delete(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        on_ramp = response.parse()
        assert_matches_type(OnRampDeleteResponse, on_ramp, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.on_ramps.with_streaming_response.delete(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            on_ramp = response.parse()
            assert_matches_type(OnRampDeleteResponse, on_ramp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.on_ramps.with_raw_response.delete(
                onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `onramp_id` but received ''"):
            client.magic_cloud_networking.on_ramps.with_raw_response.delete(
                onramp_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_apply(self, client: Cloudflare) -> None:
        on_ramp = client.magic_cloud_networking.on_ramps.apply(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(OnRampApplyResponse, on_ramp, path=["response"])

    @parametrize
    def test_raw_response_apply(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.on_ramps.with_raw_response.apply(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        on_ramp = response.parse()
        assert_matches_type(OnRampApplyResponse, on_ramp, path=["response"])

    @parametrize
    def test_streaming_response_apply(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.on_ramps.with_streaming_response.apply(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            on_ramp = response.parse()
            assert_matches_type(OnRampApplyResponse, on_ramp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_apply(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.on_ramps.with_raw_response.apply(
                onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `onramp_id` but received ''"):
            client.magic_cloud_networking.on_ramps.with_raw_response.apply(
                onramp_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        on_ramp = client.magic_cloud_networking.on_ramps.edit(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(OnRampEditResponse, on_ramp, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        on_ramp = client.magic_cloud_networking.on_ramps.edit(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            attached_hubs=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            attached_vpcs=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            description="description",
            install_routes_in_cloud=True,
            install_routes_in_magic_wan=True,
            manage_hub_to_hub_attachments=True,
            manage_vpc_to_hub_attachments=True,
            name="name",
            vpc="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OnRampEditResponse, on_ramp, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.on_ramps.with_raw_response.edit(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        on_ramp = response.parse()
        assert_matches_type(OnRampEditResponse, on_ramp, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.on_ramps.with_streaming_response.edit(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            on_ramp = response.parse()
            assert_matches_type(OnRampEditResponse, on_ramp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.on_ramps.with_raw_response.edit(
                onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `onramp_id` but received ''"):
            client.magic_cloud_networking.on_ramps.with_raw_response.edit(
                onramp_id="",
                account_id="account_id",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post("/accounts/account_id/magic/cloud/onramps/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        on_ramp = client.magic_cloud_networking.on_ramps.export(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert on_ramp.is_closed
        assert on_ramp.json() == {"foo": "bar"}
        assert cast(Any, on_ramp.is_closed) is True
        assert isinstance(on_ramp, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_export(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post("/accounts/account_id/magic/cloud/onramps/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        on_ramp = client.magic_cloud_networking.on_ramps.with_raw_response.export(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert on_ramp.is_closed is True
        assert on_ramp.http_request.headers.get("X-Stainless-Lang") == "python"
        assert on_ramp.json() == {"foo": "bar"}
        assert isinstance(on_ramp, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_export(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post("/accounts/account_id/magic/cloud/onramps/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.magic_cloud_networking.on_ramps.with_streaming_response.export(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as on_ramp:
            assert not on_ramp.is_closed
            assert on_ramp.http_request.headers.get("X-Stainless-Lang") == "python"

            assert on_ramp.json() == {"foo": "bar"}
            assert cast(Any, on_ramp.is_closed) is True
            assert isinstance(on_ramp, StreamedBinaryAPIResponse)

        assert cast(Any, on_ramp.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_export(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.on_ramps.with_raw_response.export(
                onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `onramp_id` but received ''"):
            client.magic_cloud_networking.on_ramps.with_raw_response.export(
                onramp_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        on_ramp = client.magic_cloud_networking.on_ramps.get(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(OnRampGetResponse, on_ramp, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        on_ramp = client.magic_cloud_networking.on_ramps.get(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            planned_resources=True,
            post_apply_resources=True,
            status=True,
            vpcs=True,
        )
        assert_matches_type(OnRampGetResponse, on_ramp, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.on_ramps.with_raw_response.get(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        on_ramp = response.parse()
        assert_matches_type(OnRampGetResponse, on_ramp, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.on_ramps.with_streaming_response.get(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            on_ramp = response.parse()
            assert_matches_type(OnRampGetResponse, on_ramp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.on_ramps.with_raw_response.get(
                onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `onramp_id` but received ''"):
            client.magic_cloud_networking.on_ramps.with_raw_response.get(
                onramp_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_plan(self, client: Cloudflare) -> None:
        on_ramp = client.magic_cloud_networking.on_ramps.plan(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(OnRampPlanResponse, on_ramp, path=["response"])

    @parametrize
    def test_raw_response_plan(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.on_ramps.with_raw_response.plan(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        on_ramp = response.parse()
        assert_matches_type(OnRampPlanResponse, on_ramp, path=["response"])

    @parametrize
    def test_streaming_response_plan(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.on_ramps.with_streaming_response.plan(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            on_ramp = response.parse()
            assert_matches_type(OnRampPlanResponse, on_ramp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_plan(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.on_ramps.with_raw_response.plan(
                onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `onramp_id` but received ''"):
            client.magic_cloud_networking.on_ramps.with_raw_response.plan(
                onramp_id="",
                account_id="account_id",
            )


class TestAsyncOnRamps:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        on_ramp = await async_client.magic_cloud_networking.on_ramps.create(
            account_id="account_id",
            cloud_type="AWS",
            install_routes_in_cloud=True,
            install_routes_in_magic_wan=True,
            name="name",
            type="OnrampTypeSingle",
        )
        assert_matches_type(OnRampCreateResponse, on_ramp, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        on_ramp = await async_client.magic_cloud_networking.on_ramps.create(
            account_id="account_id",
            cloud_type="AWS",
            install_routes_in_cloud=True,
            install_routes_in_magic_wan=True,
            name="name",
            type="OnrampTypeSingle",
            adopted_hub_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            attached_hubs=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            attached_vpcs=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            description="description",
            hub_provider_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            manage_hub_to_hub_attachments=True,
            manage_vpc_to_hub_attachments=True,
            region="region",
            vpc="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            forwarded="forwarded",
        )
        assert_matches_type(OnRampCreateResponse, on_ramp, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.on_ramps.with_raw_response.create(
            account_id="account_id",
            cloud_type="AWS",
            install_routes_in_cloud=True,
            install_routes_in_magic_wan=True,
            name="name",
            type="OnrampTypeSingle",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        on_ramp = await response.parse()
        assert_matches_type(OnRampCreateResponse, on_ramp, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.on_ramps.with_streaming_response.create(
            account_id="account_id",
            cloud_type="AWS",
            install_routes_in_cloud=True,
            install_routes_in_magic_wan=True,
            name="name",
            type="OnrampTypeSingle",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            on_ramp = await response.parse()
            assert_matches_type(OnRampCreateResponse, on_ramp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.on_ramps.with_raw_response.create(
                account_id="",
                cloud_type="AWS",
                install_routes_in_cloud=True,
                install_routes_in_magic_wan=True,
                name="name",
                type="OnrampTypeSingle",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        on_ramp = await async_client.magic_cloud_networking.on_ramps.update(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(OnRampUpdateResponse, on_ramp, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        on_ramp = await async_client.magic_cloud_networking.on_ramps.update(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            attached_hubs=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            attached_vpcs=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            description="description",
            install_routes_in_cloud=True,
            install_routes_in_magic_wan=True,
            manage_hub_to_hub_attachments=True,
            manage_vpc_to_hub_attachments=True,
            name="name",
            vpc="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OnRampUpdateResponse, on_ramp, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.on_ramps.with_raw_response.update(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        on_ramp = await response.parse()
        assert_matches_type(OnRampUpdateResponse, on_ramp, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.on_ramps.with_streaming_response.update(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            on_ramp = await response.parse()
            assert_matches_type(OnRampUpdateResponse, on_ramp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.on_ramps.with_raw_response.update(
                onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `onramp_id` but received ''"):
            await async_client.magic_cloud_networking.on_ramps.with_raw_response.update(
                onramp_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        on_ramp = await async_client.magic_cloud_networking.on_ramps.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[OnRampListResponse], on_ramp, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        on_ramp = await async_client.magic_cloud_networking.on_ramps.list(
            account_id="account_id",
            desc=True,
            order_by="order_by",
            status=True,
            vpcs=True,
        )
        assert_matches_type(AsyncSinglePage[OnRampListResponse], on_ramp, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.on_ramps.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        on_ramp = await response.parse()
        assert_matches_type(AsyncSinglePage[OnRampListResponse], on_ramp, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.on_ramps.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            on_ramp = await response.parse()
            assert_matches_type(AsyncSinglePage[OnRampListResponse], on_ramp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.on_ramps.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        on_ramp = await async_client.magic_cloud_networking.on_ramps.delete(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(OnRampDeleteResponse, on_ramp, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        on_ramp = await async_client.magic_cloud_networking.on_ramps.delete(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            destroy=True,
            force=True,
        )
        assert_matches_type(OnRampDeleteResponse, on_ramp, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.on_ramps.with_raw_response.delete(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        on_ramp = await response.parse()
        assert_matches_type(OnRampDeleteResponse, on_ramp, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.on_ramps.with_streaming_response.delete(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            on_ramp = await response.parse()
            assert_matches_type(OnRampDeleteResponse, on_ramp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.on_ramps.with_raw_response.delete(
                onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `onramp_id` but received ''"):
            await async_client.magic_cloud_networking.on_ramps.with_raw_response.delete(
                onramp_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_apply(self, async_client: AsyncCloudflare) -> None:
        on_ramp = await async_client.magic_cloud_networking.on_ramps.apply(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(OnRampApplyResponse, on_ramp, path=["response"])

    @parametrize
    async def test_raw_response_apply(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.on_ramps.with_raw_response.apply(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        on_ramp = await response.parse()
        assert_matches_type(OnRampApplyResponse, on_ramp, path=["response"])

    @parametrize
    async def test_streaming_response_apply(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.on_ramps.with_streaming_response.apply(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            on_ramp = await response.parse()
            assert_matches_type(OnRampApplyResponse, on_ramp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_apply(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.on_ramps.with_raw_response.apply(
                onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `onramp_id` but received ''"):
            await async_client.magic_cloud_networking.on_ramps.with_raw_response.apply(
                onramp_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        on_ramp = await async_client.magic_cloud_networking.on_ramps.edit(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(OnRampEditResponse, on_ramp, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        on_ramp = await async_client.magic_cloud_networking.on_ramps.edit(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            attached_hubs=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            attached_vpcs=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            description="description",
            install_routes_in_cloud=True,
            install_routes_in_magic_wan=True,
            manage_hub_to_hub_attachments=True,
            manage_vpc_to_hub_attachments=True,
            name="name",
            vpc="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OnRampEditResponse, on_ramp, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.on_ramps.with_raw_response.edit(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        on_ramp = await response.parse()
        assert_matches_type(OnRampEditResponse, on_ramp, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.on_ramps.with_streaming_response.edit(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            on_ramp = await response.parse()
            assert_matches_type(OnRampEditResponse, on_ramp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.on_ramps.with_raw_response.edit(
                onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `onramp_id` but received ''"):
            await async_client.magic_cloud_networking.on_ramps.with_raw_response.edit(
                onramp_id="",
                account_id="account_id",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post("/accounts/account_id/magic/cloud/onramps/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        on_ramp = await async_client.magic_cloud_networking.on_ramps.export(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert on_ramp.is_closed
        assert await on_ramp.json() == {"foo": "bar"}
        assert cast(Any, on_ramp.is_closed) is True
        assert isinstance(on_ramp, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_export(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post("/accounts/account_id/magic/cloud/onramps/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        on_ramp = await async_client.magic_cloud_networking.on_ramps.with_raw_response.export(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert on_ramp.is_closed is True
        assert on_ramp.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await on_ramp.json() == {"foo": "bar"}
        assert isinstance(on_ramp, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_export(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post("/accounts/account_id/magic/cloud/onramps/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.magic_cloud_networking.on_ramps.with_streaming_response.export(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as on_ramp:
            assert not on_ramp.is_closed
            assert on_ramp.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await on_ramp.json() == {"foo": "bar"}
            assert cast(Any, on_ramp.is_closed) is True
            assert isinstance(on_ramp, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, on_ramp.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_export(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.on_ramps.with_raw_response.export(
                onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `onramp_id` but received ''"):
            await async_client.magic_cloud_networking.on_ramps.with_raw_response.export(
                onramp_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        on_ramp = await async_client.magic_cloud_networking.on_ramps.get(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(OnRampGetResponse, on_ramp, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        on_ramp = await async_client.magic_cloud_networking.on_ramps.get(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            planned_resources=True,
            post_apply_resources=True,
            status=True,
            vpcs=True,
        )
        assert_matches_type(OnRampGetResponse, on_ramp, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.on_ramps.with_raw_response.get(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        on_ramp = await response.parse()
        assert_matches_type(OnRampGetResponse, on_ramp, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.on_ramps.with_streaming_response.get(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            on_ramp = await response.parse()
            assert_matches_type(OnRampGetResponse, on_ramp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.on_ramps.with_raw_response.get(
                onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `onramp_id` but received ''"):
            await async_client.magic_cloud_networking.on_ramps.with_raw_response.get(
                onramp_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_plan(self, async_client: AsyncCloudflare) -> None:
        on_ramp = await async_client.magic_cloud_networking.on_ramps.plan(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(OnRampPlanResponse, on_ramp, path=["response"])

    @parametrize
    async def test_raw_response_plan(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.on_ramps.with_raw_response.plan(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        on_ramp = await response.parse()
        assert_matches_type(OnRampPlanResponse, on_ramp, path=["response"])

    @parametrize
    async def test_streaming_response_plan(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.on_ramps.with_streaming_response.plan(
            onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            on_ramp = await response.parse()
            assert_matches_type(OnRampPlanResponse, on_ramp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_plan(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.on_ramps.with_raw_response.plan(
                onramp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `onramp_id` but received ''"):
            await async_client.magic_cloud_networking.on_ramps.with_raw_response.plan(
                onramp_id="",
                account_id="account_id",
            )
