from typing import Optional
from django.db.models import QuerySet


def note_filter_by_author_id(queryset: QuerySet, author_id: Optional[int]):
    if author_id:
        return queryset.filter(author_id=author_id)
    else:
        return queryset
