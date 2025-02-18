# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.magic_transit.sites import (
    ACL,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestACLs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        acl = client.magic_transit.sites.acls.create(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            lan_1={"lan_id": "lan_id"},
            lan_2={"lan_id": "lan_id"},
            name="PIN Pad - Cash Register",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        acl = client.magic_transit.sites.acls.create(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            lan_1={
                "lan_id": "lan_id",
                "lan_name": "lan_name",
                "port_ranges": ["8080-9000"],
                "ports": [1],
                "subnets": ["192.0.2.1"],
            },
            lan_2={
                "lan_id": "lan_id",
                "lan_name": "lan_name",
                "port_ranges": ["8080-9000"],
                "ports": [1],
                "subnets": ["192.0.2.1"],
            },
            name="PIN Pad - Cash Register",
            description="Allows local traffic between PIN pads and cash register.",
            forward_locally=True,
            protocols=["tcp"],
            unidirectional=True,
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.magic_transit.sites.acls.with_raw_response.create(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            lan_1={"lan_id": "lan_id"},
            lan_2={"lan_id": "lan_id"},
            name="PIN Pad - Cash Register",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.magic_transit.sites.acls.with_streaming_response.create(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            lan_1={"lan_id": "lan_id"},
            lan_2={"lan_id": "lan_id"},
            name="PIN Pad - Cash Register",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.sites.acls.with_raw_response.create(
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                lan_1={"lan_id": "lan_id"},
                lan_2={"lan_id": "lan_id"},
                name="PIN Pad - Cash Register",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            client.magic_transit.sites.acls.with_raw_response.create(
                site_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                lan_1={"lan_id": "lan_id"},
                lan_2={"lan_id": "lan_id"},
                name="PIN Pad - Cash Register",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        acl = client.magic_transit.sites.acls.update(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        acl = client.magic_transit.sites.acls.update(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            description="Allows local traffic between PIN pads and cash register.",
            forward_locally=True,
            lan_1={
                "lan_id": "lan_id",
                "lan_name": "lan_name",
                "port_ranges": ["8080-9000"],
                "ports": [1],
                "subnets": ["192.0.2.1"],
            },
            lan_2={
                "lan_id": "lan_id",
                "lan_name": "lan_name",
                "port_ranges": ["8080-9000"],
                "ports": [1],
                "subnets": ["192.0.2.1"],
            },
            name="PIN Pad - Cash Register",
            protocols=["tcp"],
            unidirectional=True,
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.magic_transit.sites.acls.with_raw_response.update(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.magic_transit.sites.acls.with_streaming_response.update(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.sites.acls.with_raw_response.update(
                acl_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            client.magic_transit.sites.acls.with_raw_response.update(
                acl_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `acl_id` but received ''"):
            client.magic_transit.sites.acls.with_raw_response.update(
                acl_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        acl = client.magic_transit.sites.acls.list(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[ACL], acl, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.magic_transit.sites.acls.with_raw_response.list(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = response.parse()
        assert_matches_type(SyncSinglePage[ACL], acl, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.magic_transit.sites.acls.with_streaming_response.list(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = response.parse()
            assert_matches_type(SyncSinglePage[ACL], acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.sites.acls.with_raw_response.list(
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            client.magic_transit.sites.acls.with_raw_response.list(
                site_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        acl = client.magic_transit.sites.acls.delete(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.magic_transit.sites.acls.with_raw_response.delete(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.magic_transit.sites.acls.with_streaming_response.delete(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.sites.acls.with_raw_response.delete(
                acl_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            client.magic_transit.sites.acls.with_raw_response.delete(
                acl_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `acl_id` but received ''"):
            client.magic_transit.sites.acls.with_raw_response.delete(
                acl_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        acl = client.magic_transit.sites.acls.edit(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        acl = client.magic_transit.sites.acls.edit(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            description="Allows local traffic between PIN pads and cash register.",
            forward_locally=True,
            lan_1={
                "lan_id": "lan_id",
                "lan_name": "lan_name",
                "port_ranges": ["8080-9000"],
                "ports": [1],
                "subnets": ["192.0.2.1"],
            },
            lan_2={
                "lan_id": "lan_id",
                "lan_name": "lan_name",
                "port_ranges": ["8080-9000"],
                "ports": [1],
                "subnets": ["192.0.2.1"],
            },
            name="PIN Pad - Cash Register",
            protocols=["tcp"],
            unidirectional=True,
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.magic_transit.sites.acls.with_raw_response.edit(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.magic_transit.sites.acls.with_streaming_response.edit(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.sites.acls.with_raw_response.edit(
                acl_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            client.magic_transit.sites.acls.with_raw_response.edit(
                acl_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `acl_id` but received ''"):
            client.magic_transit.sites.acls.with_raw_response.edit(
                acl_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        acl = client.magic_transit.sites.acls.get(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.magic_transit.sites.acls.with_raw_response.get(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.magic_transit.sites.acls.with_streaming_response.get(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.sites.acls.with_raw_response.get(
                acl_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            client.magic_transit.sites.acls.with_raw_response.get(
                acl_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `acl_id` but received ''"):
            client.magic_transit.sites.acls.with_raw_response.get(
                acl_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncACLs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        acl = await async_client.magic_transit.sites.acls.create(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            lan_1={"lan_id": "lan_id"},
            lan_2={"lan_id": "lan_id"},
            name="PIN Pad - Cash Register",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        acl = await async_client.magic_transit.sites.acls.create(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            lan_1={
                "lan_id": "lan_id",
                "lan_name": "lan_name",
                "port_ranges": ["8080-9000"],
                "ports": [1],
                "subnets": ["192.0.2.1"],
            },
            lan_2={
                "lan_id": "lan_id",
                "lan_name": "lan_name",
                "port_ranges": ["8080-9000"],
                "ports": [1],
                "subnets": ["192.0.2.1"],
            },
            name="PIN Pad - Cash Register",
            description="Allows local traffic between PIN pads and cash register.",
            forward_locally=True,
            protocols=["tcp"],
            unidirectional=True,
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.sites.acls.with_raw_response.create(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            lan_1={"lan_id": "lan_id"},
            lan_2={"lan_id": "lan_id"},
            name="PIN Pad - Cash Register",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = await response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.sites.acls.with_streaming_response.create(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            lan_1={"lan_id": "lan_id"},
            lan_2={"lan_id": "lan_id"},
            name="PIN Pad - Cash Register",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = await response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.sites.acls.with_raw_response.create(
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                lan_1={"lan_id": "lan_id"},
                lan_2={"lan_id": "lan_id"},
                name="PIN Pad - Cash Register",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            await async_client.magic_transit.sites.acls.with_raw_response.create(
                site_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                lan_1={"lan_id": "lan_id"},
                lan_2={"lan_id": "lan_id"},
                name="PIN Pad - Cash Register",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        acl = await async_client.magic_transit.sites.acls.update(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        acl = await async_client.magic_transit.sites.acls.update(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            description="Allows local traffic between PIN pads and cash register.",
            forward_locally=True,
            lan_1={
                "lan_id": "lan_id",
                "lan_name": "lan_name",
                "port_ranges": ["8080-9000"],
                "ports": [1],
                "subnets": ["192.0.2.1"],
            },
            lan_2={
                "lan_id": "lan_id",
                "lan_name": "lan_name",
                "port_ranges": ["8080-9000"],
                "ports": [1],
                "subnets": ["192.0.2.1"],
            },
            name="PIN Pad - Cash Register",
            protocols=["tcp"],
            unidirectional=True,
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.sites.acls.with_raw_response.update(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = await response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.sites.acls.with_streaming_response.update(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = await response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.sites.acls.with_raw_response.update(
                acl_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            await async_client.magic_transit.sites.acls.with_raw_response.update(
                acl_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `acl_id` but received ''"):
            await async_client.magic_transit.sites.acls.with_raw_response.update(
                acl_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        acl = await async_client.magic_transit.sites.acls.list(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[ACL], acl, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.sites.acls.with_raw_response.list(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = await response.parse()
        assert_matches_type(AsyncSinglePage[ACL], acl, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.sites.acls.with_streaming_response.list(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = await response.parse()
            assert_matches_type(AsyncSinglePage[ACL], acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.sites.acls.with_raw_response.list(
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            await async_client.magic_transit.sites.acls.with_raw_response.list(
                site_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        acl = await async_client.magic_transit.sites.acls.delete(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.sites.acls.with_raw_response.delete(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = await response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.sites.acls.with_streaming_response.delete(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = await response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.sites.acls.with_raw_response.delete(
                acl_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            await async_client.magic_transit.sites.acls.with_raw_response.delete(
                acl_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `acl_id` but received ''"):
            await async_client.magic_transit.sites.acls.with_raw_response.delete(
                acl_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        acl = await async_client.magic_transit.sites.acls.edit(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        acl = await async_client.magic_transit.sites.acls.edit(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            description="Allows local traffic between PIN pads and cash register.",
            forward_locally=True,
            lan_1={
                "lan_id": "lan_id",
                "lan_name": "lan_name",
                "port_ranges": ["8080-9000"],
                "ports": [1],
                "subnets": ["192.0.2.1"],
            },
            lan_2={
                "lan_id": "lan_id",
                "lan_name": "lan_name",
                "port_ranges": ["8080-9000"],
                "ports": [1],
                "subnets": ["192.0.2.1"],
            },
            name="PIN Pad - Cash Register",
            protocols=["tcp"],
            unidirectional=True,
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.sites.acls.with_raw_response.edit(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = await response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.sites.acls.with_streaming_response.edit(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = await response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.sites.acls.with_raw_response.edit(
                acl_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            await async_client.magic_transit.sites.acls.with_raw_response.edit(
                acl_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `acl_id` but received ''"):
            await async_client.magic_transit.sites.acls.with_raw_response.edit(
                acl_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        acl = await async_client.magic_transit.sites.acls.get(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.sites.acls.with_raw_response.get(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = await response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.sites.acls.with_streaming_response.get(
            acl_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = await response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.sites.acls.with_raw_response.get(
                acl_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            await async_client.magic_transit.sites.acls.with_raw_response.get(
                acl_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `acl_id` but received ''"):
            await async_client.magic_transit.sites.acls.with_raw_response.get(
                acl_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
