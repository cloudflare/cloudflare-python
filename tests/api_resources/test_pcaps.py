# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import PCAPGetResponse, PCAPListResponse, PCAPCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPCAPs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        pcap = client.pcaps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            system="magic-transit",
            time_limit=300,
            type="simple",
        )
        assert_matches_type(PCAPCreateResponse, pcap, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        pcap = client.pcaps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            system="magic-transit",
            time_limit=300,
            type="simple",
            byte_limit=500000,
            colo_name="ord02",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
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

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.pcaps.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            system="magic-transit",
            time_limit=300,
            type="simple",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pcap = response.parse()
        assert_matches_type(PCAPCreateResponse, pcap, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.pcaps.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            system="magic-transit",
            time_limit=300,
            type="simple",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pcap = response.parse()
            assert_matches_type(PCAPCreateResponse, pcap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pcaps.with_raw_response.create(
                "",
                system="magic-transit",
                time_limit=300,
                type="simple",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        pcap = client.pcaps.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PCAPListResponse], pcap, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.pcaps.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pcap = response.parse()
        assert_matches_type(Optional[PCAPListResponse], pcap, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.pcaps.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pcap = response.parse()
            assert_matches_type(Optional[PCAPListResponse], pcap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pcaps.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        pcap = client.pcaps.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PCAPGetResponse, pcap, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.pcaps.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pcap = response.parse()
        assert_matches_type(PCAPGetResponse, pcap, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.pcaps.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pcap = response.parse()
            assert_matches_type(PCAPGetResponse, pcap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pcaps.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pcap_id` but received ''"):
            client.pcaps.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncPCAPs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        pcap = await async_client.pcaps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            system="magic-transit",
            time_limit=300,
            type="simple",
        )
        assert_matches_type(PCAPCreateResponse, pcap, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        pcap = await async_client.pcaps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            system="magic-transit",
            time_limit=300,
            type="simple",
            byte_limit=500000,
            colo_name="ord02",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
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

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pcaps.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            system="magic-transit",
            time_limit=300,
            type="simple",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pcap = await response.parse()
        assert_matches_type(PCAPCreateResponse, pcap, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pcaps.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            system="magic-transit",
            time_limit=300,
            type="simple",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pcap = await response.parse()
            assert_matches_type(PCAPCreateResponse, pcap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pcaps.with_raw_response.create(
                "",
                system="magic-transit",
                time_limit=300,
                type="simple",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        pcap = await async_client.pcaps.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PCAPListResponse], pcap, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pcaps.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pcap = await response.parse()
        assert_matches_type(Optional[PCAPListResponse], pcap, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pcaps.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pcap = await response.parse()
            assert_matches_type(Optional[PCAPListResponse], pcap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pcaps.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        pcap = await async_client.pcaps.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PCAPGetResponse, pcap, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pcaps.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pcap = await response.parse()
        assert_matches_type(PCAPGetResponse, pcap, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pcaps.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pcap = await response.parse()
            assert_matches_type(PCAPGetResponse, pcap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pcaps.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pcap_id` but received ''"):
            await async_client.pcaps.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
