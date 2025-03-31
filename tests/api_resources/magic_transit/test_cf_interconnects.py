# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.magic_transit import (
    CfInterconnectGetResponse,
    CfInterconnectListResponse,
    CfInterconnectUpdateResponse,
    CfInterconnectBulkUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCfInterconnects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        cf_interconnect = client.magic_transit.cf_interconnects.update(
            cf_interconnect_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CfInterconnectUpdateResponse, cf_interconnect, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        cf_interconnect = client.magic_transit.cf_interconnects.update(
            cf_interconnect_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            description="Tunnel for Interconnect to ORD",
            gre={"cloudflare_endpoint": "203.0.113.1"},
            health_check={
                "enabled": True,
                "rate": "low",
                "target": {"saved": "203.0.113.1"},
                "type": "reply",
            },
            interface_address="192.0.2.0/31",
            mtu=0,
            x_magic_new_hc_target=True,
        )
        assert_matches_type(CfInterconnectUpdateResponse, cf_interconnect, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.magic_transit.cf_interconnects.with_raw_response.update(
            cf_interconnect_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cf_interconnect = response.parse()
        assert_matches_type(CfInterconnectUpdateResponse, cf_interconnect, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.magic_transit.cf_interconnects.with_streaming_response.update(
            cf_interconnect_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cf_interconnect = response.parse()
            assert_matches_type(CfInterconnectUpdateResponse, cf_interconnect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.cf_interconnects.with_raw_response.update(
                cf_interconnect_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cf_interconnect_id` but received ''"):
            client.magic_transit.cf_interconnects.with_raw_response.update(
                cf_interconnect_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        cf_interconnect = client.magic_transit.cf_interconnects.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CfInterconnectListResponse, cf_interconnect, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        cf_interconnect = client.magic_transit.cf_interconnects.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            x_magic_new_hc_target=True,
        )
        assert_matches_type(CfInterconnectListResponse, cf_interconnect, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.magic_transit.cf_interconnects.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cf_interconnect = response.parse()
        assert_matches_type(CfInterconnectListResponse, cf_interconnect, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.magic_transit.cf_interconnects.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cf_interconnect = response.parse()
            assert_matches_type(CfInterconnectListResponse, cf_interconnect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.cf_interconnects.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_bulk_update(self, client: Cloudflare) -> None:
        cf_interconnect = client.magic_transit.cf_interconnects.bulk_update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(CfInterconnectBulkUpdateResponse, cf_interconnect, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_bulk_update_with_all_params(self, client: Cloudflare) -> None:
        cf_interconnect = client.magic_transit.cf_interconnects.bulk_update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
            x_magic_new_hc_target=True,
        )
        assert_matches_type(CfInterconnectBulkUpdateResponse, cf_interconnect, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_bulk_update(self, client: Cloudflare) -> None:
        response = client.magic_transit.cf_interconnects.with_raw_response.bulk_update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cf_interconnect = response.parse()
        assert_matches_type(CfInterconnectBulkUpdateResponse, cf_interconnect, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_bulk_update(self, client: Cloudflare) -> None:
        with client.magic_transit.cf_interconnects.with_streaming_response.bulk_update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cf_interconnect = response.parse()
            assert_matches_type(CfInterconnectBulkUpdateResponse, cf_interconnect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_bulk_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.cf_interconnects.with_raw_response.bulk_update(
                account_id="",
                body={},
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        cf_interconnect = client.magic_transit.cf_interconnects.get(
            cf_interconnect_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CfInterconnectGetResponse, cf_interconnect, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        cf_interconnect = client.magic_transit.cf_interconnects.get(
            cf_interconnect_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            x_magic_new_hc_target=True,
        )
        assert_matches_type(CfInterconnectGetResponse, cf_interconnect, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.magic_transit.cf_interconnects.with_raw_response.get(
            cf_interconnect_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cf_interconnect = response.parse()
        assert_matches_type(CfInterconnectGetResponse, cf_interconnect, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.magic_transit.cf_interconnects.with_streaming_response.get(
            cf_interconnect_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cf_interconnect = response.parse()
            assert_matches_type(CfInterconnectGetResponse, cf_interconnect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.cf_interconnects.with_raw_response.get(
                cf_interconnect_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cf_interconnect_id` but received ''"):
            client.magic_transit.cf_interconnects.with_raw_response.get(
                cf_interconnect_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncCfInterconnects:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        cf_interconnect = await async_client.magic_transit.cf_interconnects.update(
            cf_interconnect_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CfInterconnectUpdateResponse, cf_interconnect, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        cf_interconnect = await async_client.magic_transit.cf_interconnects.update(
            cf_interconnect_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            description="Tunnel for Interconnect to ORD",
            gre={"cloudflare_endpoint": "203.0.113.1"},
            health_check={
                "enabled": True,
                "rate": "low",
                "target": {"saved": "203.0.113.1"},
                "type": "reply",
            },
            interface_address="192.0.2.0/31",
            mtu=0,
            x_magic_new_hc_target=True,
        )
        assert_matches_type(CfInterconnectUpdateResponse, cf_interconnect, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.cf_interconnects.with_raw_response.update(
            cf_interconnect_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cf_interconnect = await response.parse()
        assert_matches_type(CfInterconnectUpdateResponse, cf_interconnect, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.cf_interconnects.with_streaming_response.update(
            cf_interconnect_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cf_interconnect = await response.parse()
            assert_matches_type(CfInterconnectUpdateResponse, cf_interconnect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.cf_interconnects.with_raw_response.update(
                cf_interconnect_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cf_interconnect_id` but received ''"):
            await async_client.magic_transit.cf_interconnects.with_raw_response.update(
                cf_interconnect_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        cf_interconnect = await async_client.magic_transit.cf_interconnects.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CfInterconnectListResponse, cf_interconnect, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        cf_interconnect = await async_client.magic_transit.cf_interconnects.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            x_magic_new_hc_target=True,
        )
        assert_matches_type(CfInterconnectListResponse, cf_interconnect, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.cf_interconnects.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cf_interconnect = await response.parse()
        assert_matches_type(CfInterconnectListResponse, cf_interconnect, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.cf_interconnects.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cf_interconnect = await response.parse()
            assert_matches_type(CfInterconnectListResponse, cf_interconnect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.cf_interconnects.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_bulk_update(self, async_client: AsyncCloudflare) -> None:
        cf_interconnect = await async_client.magic_transit.cf_interconnects.bulk_update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(CfInterconnectBulkUpdateResponse, cf_interconnect, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_bulk_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        cf_interconnect = await async_client.magic_transit.cf_interconnects.bulk_update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
            x_magic_new_hc_target=True,
        )
        assert_matches_type(CfInterconnectBulkUpdateResponse, cf_interconnect, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_bulk_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.cf_interconnects.with_raw_response.bulk_update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cf_interconnect = await response.parse()
        assert_matches_type(CfInterconnectBulkUpdateResponse, cf_interconnect, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_bulk_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.cf_interconnects.with_streaming_response.bulk_update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cf_interconnect = await response.parse()
            assert_matches_type(CfInterconnectBulkUpdateResponse, cf_interconnect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_bulk_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.cf_interconnects.with_raw_response.bulk_update(
                account_id="",
                body={},
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        cf_interconnect = await async_client.magic_transit.cf_interconnects.get(
            cf_interconnect_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CfInterconnectGetResponse, cf_interconnect, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        cf_interconnect = await async_client.magic_transit.cf_interconnects.get(
            cf_interconnect_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            x_magic_new_hc_target=True,
        )
        assert_matches_type(CfInterconnectGetResponse, cf_interconnect, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.cf_interconnects.with_raw_response.get(
            cf_interconnect_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cf_interconnect = await response.parse()
        assert_matches_type(CfInterconnectGetResponse, cf_interconnect, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.cf_interconnects.with_streaming_response.get(
            cf_interconnect_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cf_interconnect = await response.parse()
            assert_matches_type(CfInterconnectGetResponse, cf_interconnect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.cf_interconnects.with_raw_response.get(
                cf_interconnect_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cf_interconnect_id` but received ''"):
            await async_client.magic_transit.cf_interconnects.with_raw_response.get(
                cf_interconnect_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
