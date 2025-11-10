from bson import ObjectId

def str_to_oid(s: str) -> ObjectId | None:
    if not ObjectId.is_valid(s):
        return None
    return ObjectId(s)
    