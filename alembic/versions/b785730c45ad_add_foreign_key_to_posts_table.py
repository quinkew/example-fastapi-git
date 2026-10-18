"""add foreign key to posts table

Revision ID: b785730c45ad
Revises: 6e24771e6cb5
Create Date: 2026-10-13 22:42:03.425021

"""
from operator import truediv
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b785730c45ad'
down_revision: Union[str, Sequence[str], None] = '6e24771e6cb5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    pass


def downgrade() -> None:

    pass
