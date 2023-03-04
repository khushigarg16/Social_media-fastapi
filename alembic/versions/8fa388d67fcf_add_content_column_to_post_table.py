"""add content column to post table

Revision ID: 8fa388d67fcf
Revises: 6b243dac9c73
Create Date: 2023-03-02 21:17:29.703117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fa388d67fcf'
down_revision = '6b243dac9c73'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
