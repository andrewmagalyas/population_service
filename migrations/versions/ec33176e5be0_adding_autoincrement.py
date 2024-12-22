"""Adding autoincrement

Revision ID: ec33176e5be0
Revises: 86b7261317be
Create Date: 2024-12-22 18:07:42.035772

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ec33176e5be0'
down_revision: Union[str, None] = '86b7261317be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('countries', sa.Column('country_name', sa.String(), nullable=True))
    op.alter_column('countries', 'population',
               existing_type=sa.INTEGER(),
               type_=sa.BigInteger(),
               existing_nullable=True)
    op.drop_index('ix_countries_name', table_name='countries')
    op.create_index(op.f('ix_countries_country_name'), 'countries', ['country_name'], unique=False)
    op.drop_column('countries', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('countries', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_countries_country_name'), table_name='countries')
    op.create_index('ix_countries_name', 'countries', ['name'], unique=False)
    op.alter_column('countries', 'population',
               existing_type=sa.BigInteger(),
               type_=sa.INTEGER(),
               existing_nullable=True)
    op.drop_column('countries', 'country_name')
    # ### end Alembic commands ###
