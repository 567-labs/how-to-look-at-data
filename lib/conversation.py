from kura.types import Message, Conversation
from datetime import datetime


def process_query_obj(obj: dict):
    return Conversation(
        chat_id=obj["query_id"],
        created_at=datetime.now(),
        messages=[
            Message(
                created_at=datetime.now(),
                role="user",
                content=f"""
User Query: {obj["query"]}
Retrieved Information : {obj["matching_document"]}
""",
            )
        ],
        metadata={"query_weight": obj["query_weight"], "query_id": obj["query_id"]},
    )
