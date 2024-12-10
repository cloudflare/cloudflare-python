# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.dns.zone_transfers import (
    OutgoingGetResponse,
    OutgoingCreateResponse,
    OutgoingDeleteResponse,
    OutgoingUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOutgoing:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        outgoing = client.dns.zone_transfers.outgoing.create(
            zone_id="269d8f4853475ca241c4e730be286b20",
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )
        assert_matches_type(Optional[OutgoingCreateResponse], outgoing, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.dns.zone_transfers.outgoing.with_raw_response.create(
            zone_id="269d8f4853475ca241c4e730be286b20",
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = response.parse()
        assert_matches_type(Optional[OutgoingCreateResponse], outgoing, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.dns.zone_transfers.outgoing.with_streaming_response.create(
            zone_id="269d8f4853475ca241c4e730be286b20",
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = response.parse()
            assert_matches_type(Optional[OutgoingCreateResponse], outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.zone_transfers.outgoing.with_raw_response.create(
                zone_id="",
                name="www.example.com.",
                peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        outgoing = client.dns.zone_transfers.outgoing.update(
            zone_id="269d8f4853475ca241c4e730be286b20",
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )
        assert_matches_type(Optional[OutgoingUpdateResponse], outgoing, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.dns.zone_transfers.outgoing.with_raw_response.update(
            zone_id="269d8f4853475ca241c4e730be286b20",
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = response.parse()
        assert_matches_type(Optional[OutgoingUpdateResponse], outgoing, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.dns.zone_transfers.outgoing.with_streaming_response.update(
            zone_id="269d8f4853475ca241c4e730be286b20",
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = response.parse()
            assert_matches_type(Optional[OutgoingUpdateResponse], outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.zone_transfers.outgoing.with_raw_response.update(
                zone_id="",
                name="www.example.com.",
                peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        outgoing = client.dns.zone_transfers.outgoing.delete(
            zone_id="269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(Optional[OutgoingDeleteResponse], outgoing, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.dns.zone_transfers.outgoing.with_raw_response.delete(
            zone_id="269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = response.parse()
        assert_matches_type(Optional[OutgoingDeleteResponse], outgoing, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.dns.zone_transfers.outgoing.with_streaming_response.delete(
            zone_id="269d8f4853475ca241c4e730be286b20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = response.parse()
            assert_matches_type(Optional[OutgoingDeleteResponse], outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.zone_transfers.outgoing.with_raw_response.delete(
                zone_id="",
            )

    @parametrize
    def test_method_disable(self, client: Cloudflare) -> None:
        outgoing = client.dns.zone_transfers.outgoing.disable(
            zone_id="269d8f4853475ca241c4e730be286b20",
            body={},
        )
        assert_matches_type(str, outgoing, path=["response"])

    @parametrize
    def test_raw_response_disable(self, client: Cloudflare) -> None:
        response = client.dns.zone_transfers.outgoing.with_raw_response.disable(
            zone_id="269d8f4853475ca241c4e730be286b20",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = response.parse()
        assert_matches_type(str, outgoing, path=["response"])

    @parametrize
    def test_streaming_response_disable(self, client: Cloudflare) -> None:
        with client.dns.zone_transfers.outgoing.with_streaming_response.disable(
            zone_id="269d8f4853475ca241c4e730be286b20",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = response.parse()
            assert_matches_type(str, outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_disable(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.zone_transfers.outgoing.with_raw_response.disable(
                zone_id="",
                body={},
            )

    @parametrize
    def test_method_enable(self, client: Cloudflare) -> None:
        outgoing = client.dns.zone_transfers.outgoing.enable(
            zone_id="269d8f4853475ca241c4e730be286b20",
            body={},
        )
        assert_matches_type(str, outgoing, path=["response"])

    @parametrize
    def test_raw_response_enable(self, client: Cloudflare) -> None:
        response = client.dns.zone_transfers.outgoing.with_raw_response.enable(
            zone_id="269d8f4853475ca241c4e730be286b20",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = response.parse()
        assert_matches_type(str, outgoing, path=["response"])

    @parametrize
    def test_streaming_response_enable(self, client: Cloudflare) -> None:
        with client.dns.zone_transfers.outgoing.with_streaming_response.enable(
            zone_id="269d8f4853475ca241c4e730be286b20",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = response.parse()
            assert_matches_type(str, outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_enable(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.zone_transfers.outgoing.with_raw_response.enable(
                zone_id="",
                body={},
            )

    @parametrize
    def test_method_force_notify(self, client: Cloudflare) -> None:
        outgoing = client.dns.zone_transfers.outgoing.force_notify(
            zone_id="269d8f4853475ca241c4e730be286b20",
            body={},
        )
        assert_matches_type(str, outgoing, path=["response"])

    @parametrize
    def test_raw_response_force_notify(self, client: Cloudflare) -> None:
        response = client.dns.zone_transfers.outgoing.with_raw_response.force_notify(
            zone_id="269d8f4853475ca241c4e730be286b20",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = response.parse()
        assert_matches_type(str, outgoing, path=["response"])

    @parametrize
    def test_streaming_response_force_notify(self, client: Cloudflare) -> None:
        with client.dns.zone_transfers.outgoing.with_streaming_response.force_notify(
            zone_id="269d8f4853475ca241c4e730be286b20",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = response.parse()
            assert_matches_type(str, outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_force_notify(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.zone_transfers.outgoing.with_raw_response.force_notify(
                zone_id="",
                body={},
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        outgoing = client.dns.zone_transfers.outgoing.get(
            zone_id="269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(Optional[OutgoingGetResponse], outgoing, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.dns.zone_transfers.outgoing.with_raw_response.get(
            zone_id="269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = response.parse()
        assert_matches_type(Optional[OutgoingGetResponse], outgoing, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.dns.zone_transfers.outgoing.with_streaming_response.get(
            zone_id="269d8f4853475ca241c4e730be286b20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = response.parse()
            assert_matches_type(Optional[OutgoingGetResponse], outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.zone_transfers.outgoing.with_raw_response.get(
                zone_id="",
            )


class TestAsyncOutgoing:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        outgoing = await async_client.dns.zone_transfers.outgoing.create(
            zone_id="269d8f4853475ca241c4e730be286b20",
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )
        assert_matches_type(Optional[OutgoingCreateResponse], outgoing, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.zone_transfers.outgoing.with_raw_response.create(
            zone_id="269d8f4853475ca241c4e730be286b20",
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = await response.parse()
        assert_matches_type(Optional[OutgoingCreateResponse], outgoing, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.zone_transfers.outgoing.with_streaming_response.create(
            zone_id="269d8f4853475ca241c4e730be286b20",
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = await response.parse()
            assert_matches_type(Optional[OutgoingCreateResponse], outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.zone_transfers.outgoing.with_raw_response.create(
                zone_id="",
                name="www.example.com.",
                peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        outgoing = await async_client.dns.zone_transfers.outgoing.update(
            zone_id="269d8f4853475ca241c4e730be286b20",
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )
        assert_matches_type(Optional[OutgoingUpdateResponse], outgoing, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.zone_transfers.outgoing.with_raw_response.update(
            zone_id="269d8f4853475ca241c4e730be286b20",
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = await response.parse()
        assert_matches_type(Optional[OutgoingUpdateResponse], outgoing, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.zone_transfers.outgoing.with_streaming_response.update(
            zone_id="269d8f4853475ca241c4e730be286b20",
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = await response.parse()
            assert_matches_type(Optional[OutgoingUpdateResponse], outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.zone_transfers.outgoing.with_raw_response.update(
                zone_id="",
                name="www.example.com.",
                peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        outgoing = await async_client.dns.zone_transfers.outgoing.delete(
            zone_id="269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(Optional[OutgoingDeleteResponse], outgoing, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.zone_transfers.outgoing.with_raw_response.delete(
            zone_id="269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = await response.parse()
        assert_matches_type(Optional[OutgoingDeleteResponse], outgoing, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.zone_transfers.outgoing.with_streaming_response.delete(
            zone_id="269d8f4853475ca241c4e730be286b20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = await response.parse()
            assert_matches_type(Optional[OutgoingDeleteResponse], outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.zone_transfers.outgoing.with_raw_response.delete(
                zone_id="",
            )

    @parametrize
    async def test_method_disable(self, async_client: AsyncCloudflare) -> None:
        outgoing = await async_client.dns.zone_transfers.outgoing.disable(
            zone_id="269d8f4853475ca241c4e730be286b20",
            body={},
        )
        assert_matches_type(str, outgoing, path=["response"])

    @parametrize
    async def test_raw_response_disable(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.zone_transfers.outgoing.with_raw_response.disable(
            zone_id="269d8f4853475ca241c4e730be286b20",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = await response.parse()
        assert_matches_type(str, outgoing, path=["response"])

    @parametrize
    async def test_streaming_response_disable(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.zone_transfers.outgoing.with_streaming_response.disable(
            zone_id="269d8f4853475ca241c4e730be286b20",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = await response.parse()
            assert_matches_type(str, outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_disable(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.zone_transfers.outgoing.with_raw_response.disable(
                zone_id="",
                body={},
            )

    @parametrize
    async def test_method_enable(self, async_client: AsyncCloudflare) -> None:
        outgoing = await async_client.dns.zone_transfers.outgoing.enable(
            zone_id="269d8f4853475ca241c4e730be286b20",
            body={},
        )
        assert_matches_type(str, outgoing, path=["response"])

    @parametrize
    async def test_raw_response_enable(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.zone_transfers.outgoing.with_raw_response.enable(
            zone_id="269d8f4853475ca241c4e730be286b20",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = await response.parse()
        assert_matches_type(str, outgoing, path=["response"])

    @parametrize
    async def test_streaming_response_enable(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.zone_transfers.outgoing.with_streaming_response.enable(
            zone_id="269d8f4853475ca241c4e730be286b20",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = await response.parse()
            assert_matches_type(str, outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_enable(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.zone_transfers.outgoing.with_raw_response.enable(
                zone_id="",
                body={},
            )

    @parametrize
    async def test_method_force_notify(self, async_client: AsyncCloudflare) -> None:
        outgoing = await async_client.dns.zone_transfers.outgoing.force_notify(
            zone_id="269d8f4853475ca241c4e730be286b20",
            body={},
        )
        assert_matches_type(str, outgoing, path=["response"])

    @parametrize
    async def test_raw_response_force_notify(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.zone_transfers.outgoing.with_raw_response.force_notify(
            zone_id="269d8f4853475ca241c4e730be286b20",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = await response.parse()
        assert_matches_type(str, outgoing, path=["response"])

    @parametrize
    async def test_streaming_response_force_notify(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.zone_transfers.outgoing.with_streaming_response.force_notify(
            zone_id="269d8f4853475ca241c4e730be286b20",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = await response.parse()
            assert_matches_type(str, outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_force_notify(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.zone_transfers.outgoing.with_raw_response.force_notify(
                zone_id="",
                body={},
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        outgoing = await async_client.dns.zone_transfers.outgoing.get(
            zone_id="269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(Optional[OutgoingGetResponse], outgoing, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.zone_transfers.outgoing.with_raw_response.get(
            zone_id="269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = await response.parse()
        assert_matches_type(Optional[OutgoingGetResponse], outgoing, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.zone_transfers.outgoing.with_streaming_response.get(
            zone_id="269d8f4853475ca241c4e730be286b20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = await response.parse()
            assert_matches_type(Optional[OutgoingGetResponse], outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.zone_transfers.outgoing.with_raw_response.get(
                zone_id="",
            )
