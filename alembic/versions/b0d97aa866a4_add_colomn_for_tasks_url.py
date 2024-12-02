"""Add colomn for tasks url

Revision ID: b0d97aa866a4
Revises: 9f1e05db874e
Create Date: 2024-12-02 21:59:48.595377

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b0d97aa866a4'
down_revision: Union[str, None] = '9f1e05db874e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'url')
    # ### end Alembic commands ###