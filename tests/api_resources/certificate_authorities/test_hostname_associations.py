# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.certificate_authorities import (
    HostnameAssociationGetResponse,
    HostnameAssociationUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHostnameAssociations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        hostname_association = client.certificate_authorities.hostname_associations.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[HostnameAssociationUpdateResponse], hostname_association, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        hostname_association = client.certificate_authorities.hostname_associations.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostnames=["api.example.com"],
            mtls_certificate_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(Optional[HostnameAssociationUpdateResponse], hostname_association, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.certificate_authorities.hostname_associations.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hostname_association = response.parse()
        assert_matches_type(Optional[HostnameAssociationUpdateResponse], hostname_association, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.certificate_authorities.hostname_associations.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hostname_association = response.parse()
            assert_matches_type(Optional[HostnameAssociationUpdateResponse], hostname_association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.certificate_authorities.hostname_associations.with_raw_response.update(
                zone_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        hostname_association = client.certificate_authorities.hostname_associations.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[HostnameAssociationGetResponse], hostname_association, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        hostname_association = client.certificate_authorities.hostname_associations.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            mtls_certificate_id="b2134436-2555-4acf-be5b-26c48136575e",
        )
        assert_matches_type(Optional[HostnameAssociationGetResponse], hostname_association, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.certificate_authorities.hostname_associations.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hostname_association = response.parse()
        assert_matches_type(Optional[HostnameAssociationGetResponse], hostname_association, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.certificate_authorities.hostname_associations.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hostname_association = response.parse()
            assert_matches_type(Optional[HostnameAssociationGetResponse], hostname_association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.certificate_authorities.hostname_associations.with_raw_response.get(
                zone_id="",
            )


class TestAsyncHostnameAssociations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        hostname_association = await async_client.certificate_authorities.hostname_associations.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[HostnameAssociationUpdateResponse], hostname_association, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        hostname_association = await async_client.certificate_authorities.hostname_associations.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostnames=["api.example.com"],
            mtls_certificate_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(Optional[HostnameAssociationUpdateResponse], hostname_association, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.certificate_authorities.hostname_associations.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hostname_association = await response.parse()
        assert_matches_type(Optional[HostnameAssociationUpdateResponse], hostname_association, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.certificate_authorities.hostname_associations.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hostname_association = await response.parse()
            assert_matches_type(Optional[HostnameAssociationUpdateResponse], hostname_association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.certificate_authorities.hostname_associations.with_raw_response.update(
                zone_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        hostname_association = await async_client.certificate_authorities.hostname_associations.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[HostnameAssociationGetResponse], hostname_association, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        hostname_association = await async_client.certificate_authorities.hostname_associations.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            mtls_certificate_id="b2134436-2555-4acf-be5b-26c48136575e",
        )
        assert_matches_type(Optional[HostnameAssociationGetResponse], hostname_association, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.certificate_authorities.hostname_associations.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hostname_association = await response.parse()
        assert_matches_type(Optional[HostnameAssociationGetResponse], hostname_association, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.certificate_authorities.hostname_associations.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hostname_association = await response.parse()
            assert_matches_type(Optional[HostnameAssociationGetResponse], hostname_association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.certificate_authorities.hostname_associations.with_raw_response.get(
                zone_id="",
            )
