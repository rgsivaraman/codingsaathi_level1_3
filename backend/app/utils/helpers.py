"""Helper utility functions."""
from datetime import datetime
from typing import Any, Dict


def format_datetime(dt: datetime) -> str:
    """Format datetime to ISO format string."""
    if dt:
        return dt.isoformat()
    return None


def dict_to_model(model_class, data: Dict[str, Any]):
    """Convert dictionary to model instance."""
    return model_class(**data)


def paginate(items: list, skip: int = 0, limit: int = 10) -> list:
    """Paginate a list of items."""
    return items[skip : skip + limit]


def get_pagination_params(skip: int = 0, limit: int = 10) -> Dict[str, int]:
    """Validate and return pagination parameters."""
    skip = max(0, skip)
    limit = max(1, min(limit, 100))
    return {"skip": skip, "limit": limit}
