"""
Схемы ответа на запрос
"""

pet_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "category": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"}
            },
            "required": ["id", "name"]
        },
        "status": {"type": "string"}
    },
    "required": ["id", "name", "category", "status"]
}
