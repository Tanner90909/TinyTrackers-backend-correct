"""empty message

Revision ID: 68a0ab8e84d8
Revises: 9772bc5566e0
Create Date: 2023-12-06 15:38:52.403474

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '68a0ab8e84d8'
down_revision: Union[str, None] = '9772bc5566e0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('children', 'unique_child_id_code')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('children', sa.Column('unique_child_id_code', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
