"""empty message

Revision ID: aa242678211c
Revises: 68a0ab8e84d8
Create Date: 2023-12-07 16:09:51.422901

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aa242678211c'
down_revision: Union[str, None] = '68a0ab8e84d8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('children', sa.Column('unique_child_code', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('children', 'unique_child_code')
    # ### end Alembic commands ###
