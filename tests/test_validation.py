import pytest
from sqlmodel import Field, SQLModel


def test_mutation_1(clear_sqlmodel):
    """Test mutable model with immutable field.

    For consistency with pydantic, this test should pass.

    https://github.com/tiangolo/sqlmodel/issues/262

    """

    class TestModel(SQLModel):
        id: int
        data: str = Field(allow_mutation=False)

        class Config:
            allow_mutation = True
            validate_assignment = True

    test_model = TestModel(id=1, data="foo")
    with pytest.raises(TypeError):
        test_model.data = "bar"


def test_mutation_2(clear_sqlmodel):
    """Test immutable model with mutable field.

    For consistency with pydantic, this test should pass.

    https://github.com/tiangolo/sqlmodel/issues/262

    """

    class TestModel(SQLModel):
        id: int
        data: str = Field(allow_mutation=True)

        class Config:
            allow_mutation = False
            validate_assignment = True

    test_model = TestModel(id=1, data="foo")
    with pytest.raises(TypeError):
        test_model.data = "bar"

