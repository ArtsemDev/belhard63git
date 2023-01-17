from sqlalchemy import (
    Column,
    INT,
    VARCHAR,
    ForeignKey,
    select,
)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    id = Column(INT, primary_key=True)

    engine = create_async_engine("postgresql+asyncpg://milvus:qwerty12345678@0.0.0.0:5432/bh63")
    _Session = async_sessionmaker(bind=engine)

    @staticmethod
    def create_session(func):
        async def wrapper(*args, **kwargs):
            async with Base._Session() as session:
                return await func(*args, **kwargs, session=session)

        return wrapper

    @create_session
    async def save(self, session: AsyncSession = None):
        session.add(self)
        await session.commit()
        await session.refresh(self)

    @classmethod
    @create_session
    async def get(cls, pk, session: AsyncSession = None):
        return await session.get(cls, pk)

    @classmethod
    @create_session
    async def all(
        cls,
        order_by: str = "id",
        limit: int = None,
        offset: int = None,
        session: AsyncSession = None,
        **kwargs
    ):
        objs = await session.scalars(
            select(cls)
            .filter_by(**kwargs)
            .order_by(order_by)
            .limit(limit)
            .offset(offset)
        )
        return objs.all()

    @create_session
    async def delete(self, session: AsyncSession = None):
        await session.delete(self)
        await session.commit()

    # @classmethod
    # @create_session
    # async def join(cls, right, session: AsyncSession = None, **kwargs):
    #     response = session.query(cls, right).join(right).filter_by(**kwargs)
    #     return response.all()

    @classmethod
    async def save_to_csv(cls, filename: str, mode: str, **kwargs):
        from csv import DictWriter

        objs = await cls.all(**kwargs)
        objs = list(map(lambda x: x.dict(), objs))
        fieldnames = list(objs[0].keys())
        with open(filename, mode) as file:
            writer = DictWriter(file, fieldnames=fieldnames)
            if mode == "w":
                writer.writeheader()
            writer.writerows(objs)

    @classmethod
    async def upload_from_csv(cls, filename: str, separator: str = ","):
        with open(filename, "r") as file:
            fieldnames = file.readline().strip().split(separator)
            for line in file:
                line = line.strip().split(separator)
                obj = {}
                for i in range(len(line)):
                    if line[i].lower() in ("true", "false"):
                        obj[fieldnames[i]] = (
                            True if line[i].lower() == "true" else False
                        )
                    elif line[i].lower() in ("null", "none", "nonetype", ""):
                        obj[fieldnames[i]] = None
                    elif line[i].isdigit():
                        obj[fieldnames[i]] = int(line[i])
                    else:
                        try:
                            obj[fieldnames[i]] = float(line[i])
                        except ValueError:
                            obj[fieldnames[i]] = line[i]

                obj = cls(**obj)
                try:
                    await obj.save()
                except IntegrityError:
                    pass

    async def dict(self):
        data = self.__dict__
        if "_sa_instance_state" in data:
            del data["_sa_instance_state"]
        return data

    def __call__(self, *args, **kwargs):
        self._i = 0
        self._filter = kwargs
        return self.__aiter__()

    def __aiter__(self):
        return self

    @create_session
    async def __anext__(self, session: AsyncSession = None):
        obj = await session.scalars(
            select(self.__class__)
            .where(self.__class__.id > self._i)
            .filter_by(**self._filter)
            .limit(1)
        )
        obj = obj.all()
        if obj:
            self._i += 1
            self._filter = {}
            return obj[0]
        else:
            self._i = 0
            raise StopIteration


class Category(Base):
    __tablename__ = 'categories'

    name = Column(VARCHAR(24), nullable=False)
    parent_id = Column(INT, ForeignKey('categories.id', ondelete='CASCADE'), nullable=True)


# class Category(Base):
#     __tablename__ = "categories"
#
#     name = Column(VARCHAR(24), nullable=False, unique=True)
#     is_published = Column(BOOLEAN, default=True, nullable=False)
#
#
# class Product(Base):
#     __tablename__ = "products"
#
#     title = Column(VARCHAR(36), nullable=False)
#     descr = Column(VARCHAR(1024), nullable=True)
#     price = Column(DECIMAL(8, 2), nullable=False, default=0)
#     category_id = Column(
#         INT, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False
#     )
#
#
# class User(Base):
#     __tablename__ = "users"
#
#     name = Column(VARCHAR(24), nullable=False)
#     email = Column(VARCHAR(24), nullable=False, unique=True)
#     surname = Column(VARCHAR(24), nullable=True)
