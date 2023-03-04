"""add user table

Revision ID: bc48eb413eb3
Revises: 8fa388d67fcf
Create Date: 2023-03-02 21:45:12.592678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc48eb413eb3'
down_revision = '8fa388d67fcf'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', 
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
