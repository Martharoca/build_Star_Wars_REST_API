"""empty message

Revision ID: 7171a7da1fcf
Revises: 478c0005eabd
Create Date: 2024-04-19 09:31:12.404348

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7171a7da1fcf'
down_revision = '478c0005eabd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('birth_year', sa.String(length=80), nullable=True),
    sa.Column('eye_color', sa.String(length=80), nullable=True),
    sa.Column('gender', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('character')
    # ### end Alembic commands ###
