"""empty message

Revision ID: 02e90d95b9e8
Revises: 
Create Date: 2021-06-10 15:55:56.198381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02e90d95b9e8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('confirmation', sa.Boolean(), nullable=True),
    sa.Column('paid', sa.Boolean(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('team', sa.String(), nullable=True),
    sa.Column('login_type', sa.String(), nullable=True),
    sa.Column('_password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
