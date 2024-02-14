# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.ssls import (
    CertificatePackGetResponse,
    CertificatePackDeleteResponse,
    CertificatePackUpdateResponse,
    CertificatePackCertificatePacksListCertificatePacksResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCertificatePacks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        certificate_pack = client.ssls.certificate_packs.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CertificatePackUpdateResponse, certificate_pack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.ssls.certificate_packs.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate_pack = response.parse()
        assert_matches_type(CertificatePackUpdateResponse, certificate_pack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.ssls.certificate_packs.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate_pack = response.parse()
            assert_matches_type(CertificatePackUpdateResponse, certificate_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.ssls.certificate_packs.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_pack_id` but received ''"):
            client.ssls.certificate_packs.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        certificate_pack = client.ssls.certificate_packs.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CertificatePackDeleteResponse, certificate_pack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.ssls.certificate_packs.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate_pack = response.parse()
        assert_matches_type(CertificatePackDeleteResponse, certificate_pack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.ssls.certificate_packs.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate_pack = response.parse()
            assert_matches_type(CertificatePackDeleteResponse, certificate_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.ssls.certificate_packs.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_pack_id` but received ''"):
            client.ssls.certificate_packs.with_raw_response.delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_certificate_packs_list_certificate_packs(self, client: Cloudflare) -> None:
        certificate_pack = client.ssls.certificate_packs.certificate_packs_list_certificate_packs(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[CertificatePackCertificatePacksListCertificatePacksResponse], certificate_pack, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_certificate_packs_list_certificate_packs_with_all_params(self, client: Cloudflare) -> None:
        certificate_pack = client.ssls.certificate_packs.certificate_packs_list_certificate_packs(
            "023e105f4ecef8ad9ca31a8372d0c353",
            status="all",
        )
        assert_matches_type(
            Optional[CertificatePackCertificatePacksListCertificatePacksResponse], certificate_pack, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_certificate_packs_list_certificate_packs(self, client: Cloudflare) -> None:
        response = client.ssls.certificate_packs.with_raw_response.certificate_packs_list_certificate_packs(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate_pack = response.parse()
        assert_matches_type(
            Optional[CertificatePackCertificatePacksListCertificatePacksResponse], certificate_pack, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_certificate_packs_list_certificate_packs(self, client: Cloudflare) -> None:
        with client.ssls.certificate_packs.with_streaming_response.certificate_packs_list_certificate_packs(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate_pack = response.parse()
            assert_matches_type(
                Optional[CertificatePackCertificatePacksListCertificatePacksResponse],
                certificate_pack,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_certificate_packs_list_certificate_packs(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.ssls.certificate_packs.with_raw_response.certificate_packs_list_certificate_packs(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        certificate_pack = client.ssls.certificate_packs.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CertificatePackGetResponse, certificate_pack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.ssls.certificate_packs.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate_pack = response.parse()
        assert_matches_type(CertificatePackGetResponse, certificate_pack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.ssls.certificate_packs.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate_pack = response.parse()
            assert_matches_type(CertificatePackGetResponse, certificate_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.ssls.certificate_packs.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_pack_id` but received ''"):
            client.ssls.certificate_packs.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncCertificatePacks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        certificate_pack = await async_client.ssls.certificate_packs.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CertificatePackUpdateResponse, certificate_pack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ssls.certificate_packs.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate_pack = await response.parse()
        assert_matches_type(CertificatePackUpdateResponse, certificate_pack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ssls.certificate_packs.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate_pack = await response.parse()
            assert_matches_type(CertificatePackUpdateResponse, certificate_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.ssls.certificate_packs.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_pack_id` but received ''"):
            await async_client.ssls.certificate_packs.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        certificate_pack = await async_client.ssls.certificate_packs.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CertificatePackDeleteResponse, certificate_pack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ssls.certificate_packs.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate_pack = await response.parse()
        assert_matches_type(CertificatePackDeleteResponse, certificate_pack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ssls.certificate_packs.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate_pack = await response.parse()
            assert_matches_type(CertificatePackDeleteResponse, certificate_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.ssls.certificate_packs.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_pack_id` but received ''"):
            await async_client.ssls.certificate_packs.with_raw_response.delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_certificate_packs_list_certificate_packs(self, async_client: AsyncCloudflare) -> None:
        certificate_pack = await async_client.ssls.certificate_packs.certificate_packs_list_certificate_packs(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[CertificatePackCertificatePacksListCertificatePacksResponse], certificate_pack, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_certificate_packs_list_certificate_packs_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        certificate_pack = await async_client.ssls.certificate_packs.certificate_packs_list_certificate_packs(
            "023e105f4ecef8ad9ca31a8372d0c353",
            status="all",
        )
        assert_matches_type(
            Optional[CertificatePackCertificatePacksListCertificatePacksResponse], certificate_pack, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_certificate_packs_list_certificate_packs(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ssls.certificate_packs.with_raw_response.certificate_packs_list_certificate_packs(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate_pack = await response.parse()
        assert_matches_type(
            Optional[CertificatePackCertificatePacksListCertificatePacksResponse], certificate_pack, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_certificate_packs_list_certificate_packs(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.ssls.certificate_packs.with_streaming_response.certificate_packs_list_certificate_packs(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate_pack = await response.parse()
            assert_matches_type(
                Optional[CertificatePackCertificatePacksListCertificatePacksResponse],
                certificate_pack,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_certificate_packs_list_certificate_packs(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.ssls.certificate_packs.with_raw_response.certificate_packs_list_certificate_packs(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        certificate_pack = await async_client.ssls.certificate_packs.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CertificatePackGetResponse, certificate_pack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ssls.certificate_packs.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate_pack = await response.parse()
        assert_matches_type(CertificatePackGetResponse, certificate_pack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ssls.certificate_packs.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate_pack = await response.parse()
            assert_matches_type(CertificatePackGetResponse, certificate_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.ssls.certificate_packs.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_pack_id` but received ''"):
            await async_client.ssls.certificate_packs.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
