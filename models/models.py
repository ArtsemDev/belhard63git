from sqlalchemy import Column, INT, VARCHAR, BOOLEAN, DECIMAL, ForeignKey, create_engine, select
from sqlalchemy.orm import declarative_base, sessionmaker, Session


Base = declarative_base()


class BaseMixin:
    id = Column(INT, primary_key=True)

    engine = create_engine('postgresql://milvus:qwerty12345678@0.0.0.0:5432/bh63')
    _Session = sessionmaker(bind=engine)

    @staticmethod
    def create_session(func):
        def wrapper(*args, **kwargs):
            with BaseMixin._Session() as session:
                return func(*args, **kwargs, session=session)

        return wrapper

    @create_session
    def save(self, session: Session = None):
        session.add(self)
        session.commit()
        session.refresh(self)

    @classmethod
    @create_session
    def get(cls, pk, session: Session = None):
        return session.get(cls, pk)

    @classmethod
    @create_session
    def all(
            cls,
            order_by: str = 'id',
            limit: int = None,
            offset: int = None,
            session: Session = None,
            **kwargs
    ):
        objs = session.scalars(
            select(cls)
            .filter_by(**kwargs)
            .order_by(order_by)
            .limit(limit)
            .offset(offset)
        )
        return objs.all()

    @create_session
    def delete(self, session: Session = None):
        session.delete(self)
        session.commit()

    def dict(self):
        data = self.__dict__
        if '_sa_instance_state' in data:
            del data['_sa_instance_state']
        return data

    def __call__(self, *args, **kwargs):
        self._i = 0
        self._filter = kwargs
        return self.__iter__()

    def __iter__(self):
        return self

    @create_session
    def __next__(self, session: Session = None):
        obj = session.scalars(
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


class Category(BaseMixin, Base):
    __tablename__ = 'categories'

    name = Column(VARCHAR(24), nullable=False, unique=True)
    is_published = Column(BOOLEAN, default=True, nullable=False)


class Product(BaseMixin, Base):
    __tablename__ = 'products'

    title = Column(VARCHAR(36), nullable=False)
    descr = Column(VARCHAR(1024), nullable=True)
    price = Column(DECIMAL(8, 2), nullable=False, default=0)
    category_id = Column(INT, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)


class User(BaseMixin, Base):
    __tablename__ = 'users'

    name = Column(VARCHAR(24), nullable=False)
    email = Column(VARCHAR(24), nullable=False, unique=True)
    surname = Column(VARCHAR(24), nullable=True)
