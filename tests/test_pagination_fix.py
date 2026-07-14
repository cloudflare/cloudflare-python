import pytest
from cloudflare.pagination import AsyncV4PagePaginationArray, V4PagePaginationArrayResultInfo

class MockOptions:
    """Mock object to simulate the options/params passed to the paginator."""
    def __init__(self, page_number: int):
        self.params = {"page": page_number}

@pytest.mark.asyncio
async def test_async_pagination_stops_iteration_when_total_pages_reached() -> None:
    """
    Ensures the AsyncV4PagePaginationArray iterator correctly terminates when
    the current page number matches the 'total_pages' field in the response metadata.
    
    This prevents infinite loops when the API returns the last page's data
    repeatedly for out-of-bound page requests.
    """
    result_info = V4PagePaginationArrayResultInfo(
        page=5,
        per_page=20,
        total_pages=5,
        total_count=100,
        count=20
    )
    
    paginator = AsyncV4PagePaginationArray(
        result=[], 
        result_info=result_info
    )
    
    # Manually inject private _options to simulate the current page state
    object.__setattr__(paginator, "_options", MockOptions(page_number=5))
    
    next_info = paginator.next_page_info()
    
    assert next_info is None

@pytest.mark.asyncio
async def test_async_pagination_continues_when_more_pages_exist() -> None:
    """
    Ensures the iterator calculates the next page parameters correctly
    when the current page is less than 'total_pages'.
    """
    result_info = V4PagePaginationArrayResultInfo(
        page=1,
        per_page=20,
        total_pages=5, 
        total_count=100,
        count=20
    )
    
    paginator = AsyncV4PagePaginationArray(
        result=[],
        result_info=result_info,
    )
    
    object.__setattr__(paginator, "_options", MockOptions(page_number=1))
    
    next_info = paginator.next_page_info()
    
    assert next_info is not None
    assert next_info.params["page"] == 2
