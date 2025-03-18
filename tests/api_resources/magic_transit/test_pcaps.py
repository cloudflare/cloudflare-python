# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.magic_transit import (
    PCAPGetResponse,
    PCAPListResponse,
    PCAPCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPCAPs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Cloudflare) -> None:
        pcap = client.magic_transit.pcaps.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            packet_limit=10000,
            system="magic-transit",
            time_limit=300,
            type="simple",
        )
        assert_matches_type(PCAPCreateResponse, pcap, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Cloudflare) -> None:
        pcap = client.magic_transit.pcaps.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            packet_limit=10000,
            system="magic-transit",
            time_limit=300,
            type="simple",
            filter_v1={
                "destination_address": "1.2.3.4",
                "destination_port": 80,
                "protocol": 6,
                "source_address": "1.2.3.4",
                "source_port": 123,
            },
            offset_time=parse_datetime("2020-01-01T08:00:00Z"),
        )
        assert_matches_type(PCAPCreateResponse, pcap, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Cloudflare) -> None:
        response = client.magic_transit.pcaps.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            packet_limit=10000,
            system="magic-transit",
            time_limit=300,
            type="simple",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pcap = response.parse()
        assert_matches_type(PCAPCreateResponse, pcap, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Cloudflare) -> None:
        with client.magic_transit.pcaps.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            packet_limit=10000,
            system="magic-transit",
            time_limit=300,
            type="simple",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pcap = response.parse()
            assert_matches_type(PCAPCreateResponse, pcap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.pcaps.with_raw_response.create(
                account_id="",
                packet_limit=10000,
                system="magic-transit",
                time_limit=300,
                type="simple",
            )

    @parametrize
    def test_method_create_overload_2(self, client: Cloudflare) -> None:
        pcap = client.magic_transit.pcaps.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            colo_name="ord02",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
            system="magic-transit",
            time_limit=300,
            type="simple",
        )
        assert_matches_type(PCAPCreateResponse, pcap, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Cloudflare) -> None:
        pcap = client.magic_transit.pcaps.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            colo_name="ord02",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
            system="magic-transit",
            time_limit=300,
            type="simple",
            byte_limit=500000,
            filter_v1={
                "destination_address": "1.2.3.4",
                "destination_port": 80,
                "protocol": 6,
                "source_address": "1.2.3.4",
                "source_port": 123,
            },
            packet_limit=10000,
        )
        assert_matches_type(PCAPCreateResponse, pcap, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Cloudflare) -> None:
        response = client.magic_transit.pcaps.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            colo_name="ord02",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
            system="magic-transit",
            time_limit=300,
            type="simple",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pcap = response.parse()
        assert_matches_type(PCAPCreateResponse, pcap, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Cloudflare) -> None:
        with client.magic_transit.pcaps.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            colo_name="ord02",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
            system="magic-transit",
            time_limit=300,
            type="simple",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pcap = response.parse()
            assert_matches_type(PCAPCreateResponse, pcap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.pcaps.with_raw_response.create(
                account_id="",
                colo_name="ord02",
                destination_conf="s3://pcaps-bucket?region=us-east-1",
                system="magic-transit",
                time_limit=300,
                type="simple",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        pcap = client.magic_transit.pcaps.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[PCAPListResponse], pcap, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.magic_transit.pcaps.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pcap = response.parse()
        assert_matches_type(SyncSinglePage[PCAPListResponse], pcap, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.magic_transit.pcaps.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pcap = response.parse()
            assert_matches_type(SyncSinglePage[PCAPListResponse], pcap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.pcaps.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        pcap = client.magic_transit.pcaps.get(
            pcap_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PCAPGetResponse, pcap, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.magic_transit.pcaps.with_raw_response.get(
            pcap_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pcap = response.parse()
        assert_matches_type(PCAPGetResponse, pcap, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.magic_transit.pcaps.with_streaming_response.get(
            pcap_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pcap = response.parse()
            assert_matches_type(PCAPGetResponse, pcap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.pcaps.with_raw_response.get(
                pcap_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pcap_id` but received ''"):
            client.magic_transit.pcaps.with_raw_response.get(
                pcap_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncPCAPs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        pcap = await async_client.magic_transit.pcaps.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            packet_limit=10000,
            system="magic-transit",
            time_limit=300,
            type="simple",
        )
        assert_matches_type(PCAPCreateResponse, pcap, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        pcap = await async_client.magic_transit.pcaps.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            packet_limit=10000,
            system="magic-transit",
            time_limit=300,
            type="simple",
            filter_v1={
                "destination_address": "1.2.3.4",
                "destination_port": 80,
                "protocol": 6,
                "source_address": "1.2.3.4",
                "source_port": 123,
            },
            offset_time=parse_datetime("2020-01-01T08:00:00Z"),
        )
        assert_matches_type(PCAPCreateResponse, pcap, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.pcaps.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            packet_limit=10000,
            system="magic-transit",
            time_limit=300,
            type="simple",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pcap = await response.parse()
        assert_matches_type(PCAPCreateResponse, pcap, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.pcaps.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            packet_limit=10000,
            system="magic-transit",
            time_limit=300,
            type="simple",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pcap = await response.parse()
            assert_matches_type(PCAPCreateResponse, pcap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.pcaps.with_raw_response.create(
                account_id="",
                packet_limit=10000,
                system="magic-transit",
                time_limit=300,
                type="simple",
            )

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        pcap = await async_client.magic_transit.pcaps.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            colo_name="ord02",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
            system="magic-transit",
            time_limit=300,
            type="simple",
        )
        assert_matches_type(PCAPCreateResponse, pcap, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        pcap = await async_client.magic_transit.pcaps.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            colo_name="ord02",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
            system="magic-transit",
            time_limit=300,
            type="simple",
            byte_limit=500000,
            filter_v1={
                "destination_address": "1.2.3.4",
                "destination_port": 80,
                "protocol": 6,
                "source_address": "1.2.3.4",
                "source_port": 123,
            },
            packet_limit=10000,
        )
        assert_matches_type(PCAPCreateResponse, pcap, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.pcaps.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            colo_name="ord02",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
            system="magic-transit",
            time_limit=300,
            type="simple",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pcap = await response.parse()
        assert_matches_type(PCAPCreateResponse, pcap, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.pcaps.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            colo_name="ord02",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
            system="magic-transit",
            time_limit=300,
            type="simple",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pcap = await response.parse()
            assert_matches_type(PCAPCreateResponse, pcap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.pcaps.with_raw_response.create(
                account_id="",
                colo_name="ord02",
                destination_conf="s3://pcaps-bucket?region=us-east-1",
                system="magic-transit",
                time_limit=300,
                type="simple",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        pcap = await async_client.magic_transit.pcaps.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[PCAPListResponse], pcap, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.pcaps.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pcap = await response.parse()
        assert_matches_type(AsyncSinglePage[PCAPListResponse], pcap, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.pcaps.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pcap = await response.parse()
            assert_matches_type(AsyncSinglePage[PCAPListResponse], pcap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.pcaps.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        pcap = await async_client.magic_transit.pcaps.get(
            pcap_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PCAPGetResponse, pcap, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.pcaps.with_raw_response.get(
            pcap_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pcap = await response.parse()
        assert_matches_type(PCAPGetResponse, pcap, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.pcaps.with_streaming_response.get(
            pcap_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pcap = await response.parse()
            assert_matches_type(PCAPGetResponse, pcap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.pcaps.with_raw_response.get(
                pcap_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pcap_id` but received ''"):
            await async_client.magic_transit.pcaps.with_raw_response.get(
                pcap_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
