import uuid
from datetime import date, datetime

from sqlalchemy import (
    UUID,
    Boolean,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Text,
    func,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

metadata = MetaData()


class BaseModel(DeclarativeBase):
    __abstract__ = True
    metadata = metadata

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)

    def to_dict(self):
        return {field.name: getattr(self, field.name) for field in self.__table__.c}


class User(BaseModel):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    guid: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), unique=True, default=uuid.uuid4)
    password: Mapped[str] = mapped_column(String(128))
    username: Mapped[str] = mapped_column(String(150), unique=True)
    name: Mapped[str] = mapped_column(String(150), default="")
    email: Mapped[str] = mapped_column(String(254), unique=True)
    brithday: Mapped[str] = mapped_column(String(64), default="")
    phone: Mapped[str] = mapped_column(String(15), default="")
    address: Mapped[str] = mapped_column(String(254), default="")
    last_login: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=True)

    tasks: Mapped[list["Task"]] = relationship(back_populates="user")


class Task(BaseModel):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    guid: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), unique=True, default=uuid.uuid4)
    priority: Mapped[int] = mapped_column(Integer)
    text: Mapped[str] = mapped_column(String)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)
    posted_at: Mapped[date] = mapped_column(Date)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="tasks")


class Experience(BaseModel):
    __tablename__ = "experiences"

    id: Mapped[int] = mapped_column(primary_key=True)
    company_name: Mapped[str] = mapped_column(String, nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=False)
    date_start: Mapped[str | None] = mapped_column(String, nullable=True)
    date_end: Mapped[str | None] = mapped_column(String, nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)


class Education(BaseModel):
    __tablename__ = "educations"

    id: Mapped[int] = mapped_column(primary_key=True)
    school_name: Mapped[str] = mapped_column(String, nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=False)
    date_start: Mapped[str | None] = mapped_column(String, nullable=True)
    date_end: Mapped[str | None] = mapped_column(String, nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)


class Certificate(BaseModel):
    __tablename__ = "certificates"

    id: Mapped[int] = mapped_column(primary_key=True)
    issuer: Mapped[str] = mapped_column(String, nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=False)
    icon_url: Mapped[str | None] = mapped_column(String, nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)


class Languages(BaseModel):
    __tablename__ = "languages"

    id: Mapped[int] = mapped_column(primary_key=True)
    language_name: Mapped[str] = mapped_column(String, nullable=False)
    level: Mapped[str] = mapped_column(String, nullable=False)


class Interest(BaseModel):
    __tablename__ = "interests"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)


class SkillCategory(BaseModel):
    __tablename__ = "skill_categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    skills: Mapped[list["Skill"]] = relationship(back_populates="category")


class Skill(BaseModel):
    __tablename__ = "skills"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    skill_category_id: Mapped[int] = mapped_column(
        ForeignKey("skill_categories.id"))

    category: Mapped["SkillCategory"] = relationship(back_populates="skills")
