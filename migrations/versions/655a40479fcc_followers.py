"""followers

Revision ID: 655a40479fcc
Revises: 548f6e8c11df
Create Date: 2018-12-27 11:28:00.123687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '655a40479fcc'
down_revision = '548f6e8c11df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
