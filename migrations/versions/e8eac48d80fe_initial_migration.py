"""Initial Migration

Revision ID: e8eac48d80fe
Revises: 
Create Date: 2020-09-25 12:33:54.204543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8eac48d80fe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pizza',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('flavor', sa.Column('pizza', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'flavor', 'pizza', ['pizza'], ['id'])
    op.add_column('sizes', sa.Column('pizza', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'sizes', 'pizza', ['pizza'], ['id'])
    op.add_column('toppings', sa.Column('pizza', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'toppings', 'pizza', ['pizza'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'toppings', type_='foreignkey')
    op.drop_column('toppings', 'pizza')
    op.drop_constraint(None, 'sizes', type_='foreignkey')
    op.drop_column('sizes', 'pizza')
    op.drop_constraint(None, 'flavor', type_='foreignkey')
    op.drop_column('flavor', 'pizza')
    op.drop_table('pizza')
    # ### end Alembic commands ###
