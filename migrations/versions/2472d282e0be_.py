"""empty message

Revision ID: 2472d282e0be
Revises: 
Create Date: 2022-02-23 21:12:47.889326

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2472d282e0be'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pname', sa.String(length=80), nullable=False),
    sa.Column('color', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('pname')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('people')
    # ### end Alembic commands ###
