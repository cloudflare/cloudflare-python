# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types import (
    PageruleCreateResponse,
    PageruleUpdateResponse,
    PageruleListResponse,
    PageruleDeleteResponse,
    PageruleGetResponse,
)

from typing import Any, cast, Optional

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import pagerule_create_params
from cloudflare.types import pagerule_update_params
from cloudflare.types import pagerule_list_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPagerules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        pagerule = client.pagerules.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{}, {}, {}],
            targets=[
                {
                    "constraint": {
                        "operator": "matches",
                        "value": "*example.com/images/*",
                    },
                    "target": "url",
                }
            ],
        )
        assert_matches_type(PageruleCreateResponse, pagerule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        pagerule = client.pagerules.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "name": "forward_url",
                    "value": {
                        "type": "temporary",
                        "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                    },
                },
                {
                    "name": "forward_url",
                    "value": {
                        "type": "temporary",
                        "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                    },
                },
                {
                    "name": "forward_url",
                    "value": {
                        "type": "temporary",
                        "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                    },
                },
            ],
            targets=[
                {
                    "constraint": {
                        "operator": "matches",
                        "value": "*example.com/images/*",
                    },
                    "target": "url",
                }
            ],
            priority=0,
            status="active",
        )
        assert_matches_type(PageruleCreateResponse, pagerule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.pagerules.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{}, {}, {}],
            targets=[
                {
                    "constraint": {
                        "operator": "matches",
                        "value": "*example.com/images/*",
                    },
                    "target": "url",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerule = response.parse()
        assert_matches_type(PageruleCreateResponse, pagerule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.pagerules.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{}, {}, {}],
            targets=[
                {
                    "constraint": {
                        "operator": "matches",
                        "value": "*example.com/images/*",
                    },
                    "target": "url",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pagerule = response.parse()
            assert_matches_type(PageruleCreateResponse, pagerule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.pagerules.with_raw_response.create(
                "",
                actions=[{}, {}, {}],
                targets=[
                    {
                        "constraint": {
                            "operator": "matches",
                            "value": "*example.com/images/*",
                        },
                        "target": "url",
                    }
                ],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        pagerule = client.pagerules.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{}, {}, {}],
            targets=[
                {
                    "constraint": {
                        "operator": "matches",
                        "value": "*example.com/images/*",
                    },
                    "target": "url",
                }
            ],
        )
        assert_matches_type(PageruleUpdateResponse, pagerule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        pagerule = client.pagerules.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "name": "forward_url",
                    "value": {
                        "type": "temporary",
                        "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                    },
                },
                {
                    "name": "forward_url",
                    "value": {
                        "type": "temporary",
                        "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                    },
                },
                {
                    "name": "forward_url",
                    "value": {
                        "type": "temporary",
                        "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                    },
                },
            ],
            targets=[
                {
                    "constraint": {
                        "operator": "matches",
                        "value": "*example.com/images/*",
                    },
                    "target": "url",
                }
            ],
            priority=0,
            status="active",
        )
        assert_matches_type(PageruleUpdateResponse, pagerule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.pagerules.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{}, {}, {}],
            targets=[
                {
                    "constraint": {
                        "operator": "matches",
                        "value": "*example.com/images/*",
                    },
                    "target": "url",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerule = response.parse()
        assert_matches_type(PageruleUpdateResponse, pagerule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.pagerules.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{}, {}, {}],
            targets=[
                {
                    "constraint": {
                        "operator": "matches",
                        "value": "*example.com/images/*",
                    },
                    "target": "url",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pagerule = response.parse()
            assert_matches_type(PageruleUpdateResponse, pagerule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.pagerules.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                actions=[{}, {}, {}],
                targets=[
                    {
                        "constraint": {
                            "operator": "matches",
                            "value": "*example.com/images/*",
                        },
                        "target": "url",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pagerule_id` but received ''"):
            client.pagerules.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                actions=[{}, {}, {}],
                targets=[
                    {
                        "constraint": {
                            "operator": "matches",
                            "value": "*example.com/images/*",
                        },
                        "target": "url",
                    }
                ],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        pagerule = client.pagerules.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PageruleListResponse, pagerule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        pagerule = client.pagerules.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            direction="desc",
            match="any",
            order="status",
            status="active",
        )
        assert_matches_type(PageruleListResponse, pagerule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.pagerules.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerule = response.parse()
        assert_matches_type(PageruleListResponse, pagerule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.pagerules.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pagerule = response.parse()
            assert_matches_type(PageruleListResponse, pagerule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.pagerules.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        pagerule = client.pagerules.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PageruleDeleteResponse], pagerule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.pagerules.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerule = response.parse()
        assert_matches_type(Optional[PageruleDeleteResponse], pagerule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.pagerules.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pagerule = response.parse()
            assert_matches_type(Optional[PageruleDeleteResponse], pagerule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.pagerules.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pagerule_id` but received ''"):
            client.pagerules.with_raw_response.delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        pagerule = client.pagerules.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PageruleGetResponse, pagerule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.pagerules.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerule = response.parse()
        assert_matches_type(PageruleGetResponse, pagerule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.pagerules.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pagerule = response.parse()
            assert_matches_type(PageruleGetResponse, pagerule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.pagerules.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pagerule_id` but received ''"):
            client.pagerules.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncPagerules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        pagerule = await async_client.pagerules.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{}, {}, {}],
            targets=[
                {
                    "constraint": {
                        "operator": "matches",
                        "value": "*example.com/images/*",
                    },
                    "target": "url",
                }
            ],
        )
        assert_matches_type(PageruleCreateResponse, pagerule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        pagerule = await async_client.pagerules.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "name": "forward_url",
                    "value": {
                        "type": "temporary",
                        "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                    },
                },
                {
                    "name": "forward_url",
                    "value": {
                        "type": "temporary",
                        "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                    },
                },
                {
                    "name": "forward_url",
                    "value": {
                        "type": "temporary",
                        "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                    },
                },
            ],
            targets=[
                {
                    "constraint": {
                        "operator": "matches",
                        "value": "*example.com/images/*",
                    },
                    "target": "url",
                }
            ],
            priority=0,
            status="active",
        )
        assert_matches_type(PageruleCreateResponse, pagerule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pagerules.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{}, {}, {}],
            targets=[
                {
                    "constraint": {
                        "operator": "matches",
                        "value": "*example.com/images/*",
                    },
                    "target": "url",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerule = await response.parse()
        assert_matches_type(PageruleCreateResponse, pagerule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pagerules.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{}, {}, {}],
            targets=[
                {
                    "constraint": {
                        "operator": "matches",
                        "value": "*example.com/images/*",
                    },
                    "target": "url",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pagerule = await response.parse()
            assert_matches_type(PageruleCreateResponse, pagerule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.pagerules.with_raw_response.create(
                "",
                actions=[{}, {}, {}],
                targets=[
                    {
                        "constraint": {
                            "operator": "matches",
                            "value": "*example.com/images/*",
                        },
                        "target": "url",
                    }
                ],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        pagerule = await async_client.pagerules.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{}, {}, {}],
            targets=[
                {
                    "constraint": {
                        "operator": "matches",
                        "value": "*example.com/images/*",
                    },
                    "target": "url",
                }
            ],
        )
        assert_matches_type(PageruleUpdateResponse, pagerule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        pagerule = await async_client.pagerules.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "name": "forward_url",
                    "value": {
                        "type": "temporary",
                        "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                    },
                },
                {
                    "name": "forward_url",
                    "value": {
                        "type": "temporary",
                        "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                    },
                },
                {
                    "name": "forward_url",
                    "value": {
                        "type": "temporary",
                        "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                    },
                },
            ],
            targets=[
                {
                    "constraint": {
                        "operator": "matches",
                        "value": "*example.com/images/*",
                    },
                    "target": "url",
                }
            ],
            priority=0,
            status="active",
        )
        assert_matches_type(PageruleUpdateResponse, pagerule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pagerules.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{}, {}, {}],
            targets=[
                {
                    "constraint": {
                        "operator": "matches",
                        "value": "*example.com/images/*",
                    },
                    "target": "url",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerule = await response.parse()
        assert_matches_type(PageruleUpdateResponse, pagerule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pagerules.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{}, {}, {}],
            targets=[
                {
                    "constraint": {
                        "operator": "matches",
                        "value": "*example.com/images/*",
                    },
                    "target": "url",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pagerule = await response.parse()
            assert_matches_type(PageruleUpdateResponse, pagerule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.pagerules.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                actions=[{}, {}, {}],
                targets=[
                    {
                        "constraint": {
                            "operator": "matches",
                            "value": "*example.com/images/*",
                        },
                        "target": "url",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pagerule_id` but received ''"):
            await async_client.pagerules.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                actions=[{}, {}, {}],
                targets=[
                    {
                        "constraint": {
                            "operator": "matches",
                            "value": "*example.com/images/*",
                        },
                        "target": "url",
                    }
                ],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        pagerule = await async_client.pagerules.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PageruleListResponse, pagerule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        pagerule = await async_client.pagerules.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            direction="desc",
            match="any",
            order="status",
            status="active",
        )
        assert_matches_type(PageruleListResponse, pagerule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pagerules.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerule = await response.parse()
        assert_matches_type(PageruleListResponse, pagerule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pagerules.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pagerule = await response.parse()
            assert_matches_type(PageruleListResponse, pagerule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.pagerules.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        pagerule = await async_client.pagerules.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PageruleDeleteResponse], pagerule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pagerules.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerule = await response.parse()
        assert_matches_type(Optional[PageruleDeleteResponse], pagerule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pagerules.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pagerule = await response.parse()
            assert_matches_type(Optional[PageruleDeleteResponse], pagerule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.pagerules.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pagerule_id` but received ''"):
            await async_client.pagerules.with_raw_response.delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        pagerule = await async_client.pagerules.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PageruleGetResponse, pagerule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pagerules.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerule = await response.parse()
        assert_matches_type(PageruleGetResponse, pagerule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pagerules.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pagerule = await response.parse()
            assert_matches_type(PageruleGetResponse, pagerule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.pagerules.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pagerule_id` but received ''"):
            await async_client.pagerules.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
