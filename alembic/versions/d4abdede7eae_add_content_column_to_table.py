"""add content column to table

Revision ID: d4abdede7eae
Revises: ab2c382daac6
Create Date: 2026-10-06 22:27:47.144931

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd4abdede7eae'
down_revision: Union[str, Sequence[str], None] = 'ab2c382daac6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
