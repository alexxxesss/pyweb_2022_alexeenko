from typing import Optional
from django.db.models.query import QuerySet


def note_filter_by_author_id(queryset: QuerySet, author_id: Optional[int]):
    if author_id is not None:
        return queryset.filter(author_id=author_id)
    else:
        return queryset