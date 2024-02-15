# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, cast, Optional

from cloudflare.types.pcaps import (
    OwnershipMagicPcapCollectionAddBucketsForFullPacketCapturesResponse,
    OwnershipMagicPcapCollectionListPcaPsBucketOwnershipResponse,
)

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.pcaps import ownership_magic_pcap_collection_add_buckets_for_full_packet_captures_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOwnerships:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        ownership = client.pcaps.ownerships.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert ownership is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.pcaps.ownerships.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = response.parse()
        assert ownership is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.pcaps.ownerships.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = response.parse()
            assert ownership is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.pcaps.ownerships.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.pcaps.ownerships.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_magic_pcap_collection_add_buckets_for_full_packet_captures(self, client: Cloudflare) -> None:
        ownership = client.pcaps.ownerships.magic_pcap_collection_add_buckets_for_full_packet_captures(
            "023e105f4ecef8ad9ca31a8372d0c353",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
        )
        assert_matches_type(
            OwnershipMagicPcapCollectionAddBucketsForFullPacketCapturesResponse, ownership, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_magic_pcap_collection_add_buckets_for_full_packet_captures(self, client: Cloudflare) -> None:
        response = client.pcaps.ownerships.with_raw_response.magic_pcap_collection_add_buckets_for_full_packet_captures(
            "023e105f4ecef8ad9ca31a8372d0c353",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = response.parse()
        assert_matches_type(
            OwnershipMagicPcapCollectionAddBucketsForFullPacketCapturesResponse, ownership, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_magic_pcap_collection_add_buckets_for_full_packet_captures(
        self, client: Cloudflare
    ) -> None:
        with client.pcaps.ownerships.with_streaming_response.magic_pcap_collection_add_buckets_for_full_packet_captures(
            "023e105f4ecef8ad9ca31a8372d0c353",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = response.parse()
            assert_matches_type(
                OwnershipMagicPcapCollectionAddBucketsForFullPacketCapturesResponse, ownership, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_magic_pcap_collection_add_buckets_for_full_packet_captures(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.pcaps.ownerships.with_raw_response.magic_pcap_collection_add_buckets_for_full_packet_captures(
                "",
                destination_conf="s3://pcaps-bucket?region=us-east-1",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_magic_pcap_collection_list_pca_ps_bucket_ownership(self, client: Cloudflare) -> None:
        ownership = client.pcaps.ownerships.magic_pcap_collection_list_pca_ps_bucket_ownership(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[OwnershipMagicPcapCollectionListPcaPsBucketOwnershipResponse], ownership, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_magic_pcap_collection_list_pca_ps_bucket_ownership(self, client: Cloudflare) -> None:
        response = client.pcaps.ownerships.with_raw_response.magic_pcap_collection_list_pca_ps_bucket_ownership(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = response.parse()
        assert_matches_type(
            Optional[OwnershipMagicPcapCollectionListPcaPsBucketOwnershipResponse], ownership, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_magic_pcap_collection_list_pca_ps_bucket_ownership(self, client: Cloudflare) -> None:
        with client.pcaps.ownerships.with_streaming_response.magic_pcap_collection_list_pca_ps_bucket_ownership(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = response.parse()
            assert_matches_type(
                Optional[OwnershipMagicPcapCollectionListPcaPsBucketOwnershipResponse], ownership, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_magic_pcap_collection_list_pca_ps_bucket_ownership(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.pcaps.ownerships.with_raw_response.magic_pcap_collection_list_pca_ps_bucket_ownership(
                "",
            )


class TestAsyncOwnerships:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        ownership = await async_client.pcaps.ownerships.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert ownership is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pcaps.ownerships.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = await response.parse()
        assert ownership is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pcaps.ownerships.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = await response.parse()
            assert ownership is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.pcaps.ownerships.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.pcaps.ownerships.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_magic_pcap_collection_add_buckets_for_full_packet_captures(
        self, async_client: AsyncCloudflare
    ) -> None:
        ownership = await async_client.pcaps.ownerships.magic_pcap_collection_add_buckets_for_full_packet_captures(
            "023e105f4ecef8ad9ca31a8372d0c353",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
        )
        assert_matches_type(
            OwnershipMagicPcapCollectionAddBucketsForFullPacketCapturesResponse, ownership, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_magic_pcap_collection_add_buckets_for_full_packet_captures(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.pcaps.ownerships.with_raw_response.magic_pcap_collection_add_buckets_for_full_packet_captures(
            "023e105f4ecef8ad9ca31a8372d0c353",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = await response.parse()
        assert_matches_type(
            OwnershipMagicPcapCollectionAddBucketsForFullPacketCapturesResponse, ownership, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_magic_pcap_collection_add_buckets_for_full_packet_captures(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.pcaps.ownerships.with_streaming_response.magic_pcap_collection_add_buckets_for_full_packet_captures(
            "023e105f4ecef8ad9ca31a8372d0c353",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = await response.parse()
            assert_matches_type(
                OwnershipMagicPcapCollectionAddBucketsForFullPacketCapturesResponse, ownership, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_magic_pcap_collection_add_buckets_for_full_packet_captures(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.pcaps.ownerships.with_raw_response.magic_pcap_collection_add_buckets_for_full_packet_captures(
                "",
                destination_conf="s3://pcaps-bucket?region=us-east-1",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_magic_pcap_collection_list_pca_ps_bucket_ownership(
        self, async_client: AsyncCloudflare
    ) -> None:
        ownership = await async_client.pcaps.ownerships.magic_pcap_collection_list_pca_ps_bucket_ownership(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[OwnershipMagicPcapCollectionListPcaPsBucketOwnershipResponse], ownership, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_magic_pcap_collection_list_pca_ps_bucket_ownership(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.pcaps.ownerships.with_raw_response.magic_pcap_collection_list_pca_ps_bucket_ownership(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = await response.parse()
        assert_matches_type(
            Optional[OwnershipMagicPcapCollectionListPcaPsBucketOwnershipResponse], ownership, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_magic_pcap_collection_list_pca_ps_bucket_ownership(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.pcaps.ownerships.with_streaming_response.magic_pcap_collection_list_pca_ps_bucket_ownership(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = await response.parse()
            assert_matches_type(
                Optional[OwnershipMagicPcapCollectionListPcaPsBucketOwnershipResponse], ownership, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_magic_pcap_collection_list_pca_ps_bucket_ownership(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.pcaps.ownerships.with_raw_response.magic_pcap_collection_list_pca_ps_bucket_ownership(
                "",
            )
