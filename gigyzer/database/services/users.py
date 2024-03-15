from gigyzer.database import UserModel, UserSchema, db_session


def create_user(data: UserSchema) -> UserModel:
    try:
        old_user_with_username = get_user({"username": data.username})
        if old_user_with_username:
            raise Exception("User with this <username> already exists")
        old_user_with_user_id = get_user({"user_id": data.user_id})
        if old_user_with_user_id:
            raise Exception("User with this <user_id> already exists")
        user = UserModel(**data.dict())
        db_session.add(user)
        db_session.commit()
        db_session.refresh(user)
        return user
    except Exception as e:
        db_session.rollback()
        raise e


def get_user(filters: dict | None = None) -> UserModel | None:
    query = db_session.query(UserModel)
    if filters:
        query = query.filter_by(**filters)
    return query.first()


def update_user(user_id: int, data: dict) -> UserModel:
    user = get_user({"user_id": user_id})
    if not user:
        raise Exception("User not found")
    for key, value in data.items():
        setattr(user, key, value)
    db_session.commit()
    db_session.refresh(user)
    return user


def delete_user(user_id: int) -> bool:
    user = get_user({"user_id": user_id})
    if not user:
        raise Exception("User not found")
    db_session.delete(user)
    db_session.commit()
    return True


__all__ = ["create_user", "get_user", "update_user", "delete_user"]
