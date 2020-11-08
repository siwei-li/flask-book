"""'init'

Revision ID: fdd665b4e69b
Revises: 
Create Date: 2020-11-05 14:17:59.329890

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fdd665b4e69b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nickname', sa.String(length=20), nullable=False),
    sa.Column('mobile', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=16), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('books',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('category', sa.String(length=100), nullable=True),
    sa.Column('price', mysql.FLOAT(precision=7, scale=2), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.Enum('0', '1'), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    op.drop_table('users')
    # ### end Alembic commands ###