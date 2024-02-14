# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.pcaps.ownerships import ValidateMagicPcapCollectionValidateBucketsForFullPacketCapturesResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.pcaps.ownerships import (
    validate_magic_pcap_collection_validate_buckets_for_full_packet_captures_params,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestValidates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_magic_pcap_collection_validate_buckets_for_full_packet_captures(self, client: Cloudflare) -> None:
        validate = client.pcaps.ownerships.validates.magic_pcap_collection_validate_buckets_for_full_packet_captures(
            "023e105f4ecef8ad9ca31a8372d0c353",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
            ownership_challenge="ownership-challenge-9883874ecac311ec8475433579a6bf5f.txt",
        )
        assert_matches_type(
            ValidateMagicPcapCollectionValidateBucketsForFullPacketCapturesResponse, validate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_magic_pcap_collection_validate_buckets_for_full_packet_captures(
        self, client: Cloudflare
    ) -> None:
        response = client.pcaps.ownerships.validates.with_raw_response.magic_pcap_collection_validate_buckets_for_full_packet_captures(
            "023e105f4ecef8ad9ca31a8372d0c353",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
            ownership_challenge="ownership-challenge-9883874ecac311ec8475433579a6bf5f.txt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate = response.parse()
        assert_matches_type(
            ValidateMagicPcapCollectionValidateBucketsForFullPacketCapturesResponse, validate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_magic_pcap_collection_validate_buckets_for_full_packet_captures(
        self, client: Cloudflare
    ) -> None:
        with client.pcaps.ownerships.validates.with_streaming_response.magic_pcap_collection_validate_buckets_for_full_packet_captures(
            "023e105f4ecef8ad9ca31a8372d0c353",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
            ownership_challenge="ownership-challenge-9883874ecac311ec8475433579a6bf5f.txt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate = response.parse()
            assert_matches_type(
                ValidateMagicPcapCollectionValidateBucketsForFullPacketCapturesResponse, validate, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_magic_pcap_collection_validate_buckets_for_full_packet_captures(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.pcaps.ownerships.validates.with_raw_response.magic_pcap_collection_validate_buckets_for_full_packet_captures(
                "",
                destination_conf="s3://pcaps-bucket?region=us-east-1",
                ownership_challenge="ownership-challenge-9883874ecac311ec8475433579a6bf5f.txt",
            )


class TestAsyncValidates:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_magic_pcap_collection_validate_buckets_for_full_packet_captures(
        self, async_client: AsyncCloudflare
    ) -> None:
        validate = await async_client.pcaps.ownerships.validates.magic_pcap_collection_validate_buckets_for_full_packet_captures(
            "023e105f4ecef8ad9ca31a8372d0c353",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
            ownership_challenge="ownership-challenge-9883874ecac311ec8475433579a6bf5f.txt",
        )
        assert_matches_type(
            ValidateMagicPcapCollectionValidateBucketsForFullPacketCapturesResponse, validate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_magic_pcap_collection_validate_buckets_for_full_packet_captures(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.pcaps.ownerships.validates.with_raw_response.magic_pcap_collection_validate_buckets_for_full_packet_captures(
            "023e105f4ecef8ad9ca31a8372d0c353",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
            ownership_challenge="ownership-challenge-9883874ecac311ec8475433579a6bf5f.txt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate = await response.parse()
        assert_matches_type(
            ValidateMagicPcapCollectionValidateBucketsForFullPacketCapturesResponse, validate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_magic_pcap_collection_validate_buckets_for_full_packet_captures(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.pcaps.ownerships.validates.with_streaming_response.magic_pcap_collection_validate_buckets_for_full_packet_captures(
            "023e105f4ecef8ad9ca31a8372d0c353",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
            ownership_challenge="ownership-challenge-9883874ecac311ec8475433579a6bf5f.txt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate = await response.parse()
            assert_matches_type(
                ValidateMagicPcapCollectionValidateBucketsForFullPacketCapturesResponse, validate, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_magic_pcap_collection_validate_buckets_for_full_packet_captures(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.pcaps.ownerships.validates.with_raw_response.magic_pcap_collection_validate_buckets_for_full_packet_captures(
                "",
                destination_conf="s3://pcaps-bucket?region=us-east-1",
                ownership_challenge="ownership-challenge-9883874ecac311ec8475433579a6bf5f.txt",
            )
