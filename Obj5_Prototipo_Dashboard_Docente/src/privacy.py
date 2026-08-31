"""Utilidades de minimización de identificadores mostrados en pantalla."""

from __future__ import annotations

import hashlib


def public_student_code(value: object) -> str:
    """Genera un código estable no reversible para visualización."""
    digest = hashlib.sha256(str(value).encode("utf-8")).hexdigest()[:10].upper()
    return f"EST-{digest}"
