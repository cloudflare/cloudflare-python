# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from cloudflare.pagination import SyncSinglePage, AsyncSinglePage

from typing import Any, cast, Optional

from cloudflare.types.ssl import CertificatePackDeleteResponse, CertificatePackEditResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.ssl import certificate_pack_list_params
from cloudflare.types.ssl import certificate_pack_edit_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCertificatePacks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        certificate_pack = client.ssl.certificate_packs.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[object], certificate_pack, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        certificate_pack = client.ssl.certificate_packs.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            status="all",
        )
        assert_matches_type(SyncSinglePage[object], certificate_pack, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.ssl.certificate_packs.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate_pack = response.parse()
        assert_matches_type(SyncSinglePage[object], certificate_pack, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.ssl.certificate_packs.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate_pack = response.parse()
            assert_matches_type(SyncSinglePage[object], certificate_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.ssl.certificate_packs.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        certificate_pack = client.ssl.certificate_packs.delete(
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CertificatePackDeleteResponse], certificate_pack, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.ssl.certificate_packs.with_raw_response.delete(
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate_pack = response.parse()
        assert_matches_type(Optional[CertificatePackDeleteResponse], certificate_pack, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.ssl.certificate_packs.with_streaming_response.delete(
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate_pack = response.parse()
            assert_matches_type(Optional[CertificatePackDeleteResponse], certificate_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.ssl.certificate_packs.with_raw_response.delete(
                certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_pack_id` but received ''"):
            client.ssl.certificate_packs.with_raw_response.delete(
                certificate_pack_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        certificate_pack = client.ssl.certificate_packs.edit(
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[CertificatePackEditResponse], certificate_pack, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.ssl.certificate_packs.with_raw_response.edit(
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate_pack = response.parse()
        assert_matches_type(Optional[CertificatePackEditResponse], certificate_pack, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.ssl.certificate_packs.with_streaming_response.edit(
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate_pack = response.parse()
            assert_matches_type(Optional[CertificatePackEditResponse], certificate_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.ssl.certificate_packs.with_raw_response.edit(
                certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_pack_id` but received ''"):
            client.ssl.certificate_packs.with_raw_response.edit(
                certificate_pack_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        certificate_pack = client.ssl.certificate_packs.get(
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, certificate_pack, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.ssl.certificate_packs.with_raw_response.get(
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate_pack = response.parse()
        assert_matches_type(object, certificate_pack, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.ssl.certificate_packs.with_streaming_response.get(
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate_pack = response.parse()
            assert_matches_type(object, certificate_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.ssl.certificate_packs.with_raw_response.get(
                certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_pack_id` but received ''"):
            client.ssl.certificate_packs.with_raw_response.get(
                certificate_pack_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncCertificatePacks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        certificate_pack = await async_client.ssl.certificate_packs.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[object], certificate_pack, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        certificate_pack = await async_client.ssl.certificate_packs.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            status="all",
        )
        assert_matches_type(AsyncSinglePage[object], certificate_pack, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ssl.certificate_packs.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate_pack = await response.parse()
        assert_matches_type(AsyncSinglePage[object], certificate_pack, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ssl.certificate_packs.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate_pack = await response.parse()
            assert_matches_type(AsyncSinglePage[object], certificate_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.ssl.certificate_packs.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        certificate_pack = await async_client.ssl.certificate_packs.delete(
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CertificatePackDeleteResponse], certificate_pack, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ssl.certificate_packs.with_raw_response.delete(
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate_pack = await response.parse()
        assert_matches_type(Optional[CertificatePackDeleteResponse], certificate_pack, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ssl.certificate_packs.with_streaming_response.delete(
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate_pack = await response.parse()
            assert_matches_type(Optional[CertificatePackDeleteResponse], certificate_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.ssl.certificate_packs.with_raw_response.delete(
                certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_pack_id` but received ''"):
            await async_client.ssl.certificate_packs.with_raw_response.delete(
                certificate_pack_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        certificate_pack = await async_client.ssl.certificate_packs.edit(
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[CertificatePackEditResponse], certificate_pack, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ssl.certificate_packs.with_raw_response.edit(
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate_pack = await response.parse()
        assert_matches_type(Optional[CertificatePackEditResponse], certificate_pack, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ssl.certificate_packs.with_streaming_response.edit(
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate_pack = await response.parse()
            assert_matches_type(Optional[CertificatePackEditResponse], certificate_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.ssl.certificate_packs.with_raw_response.edit(
                certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_pack_id` but received ''"):
            await async_client.ssl.certificate_packs.with_raw_response.edit(
                certificate_pack_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        certificate_pack = await async_client.ssl.certificate_packs.get(
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, certificate_pack, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ssl.certificate_packs.with_raw_response.get(
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate_pack = await response.parse()
        assert_matches_type(object, certificate_pack, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ssl.certificate_packs.with_streaming_response.get(
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate_pack = await response.parse()
            assert_matches_type(object, certificate_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.ssl.certificate_packs.with_raw_response.get(
                certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_pack_id` but received ''"):
            await async_client.ssl.certificate_packs.with_raw_response.get(
                certificate_pack_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
