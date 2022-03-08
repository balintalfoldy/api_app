"""add content column

Revision ID: b3638e032032
Revises: 6ad2d6b4be3c
Create Date: 2022-03-08 09:26:27.216931

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3638e032032'
down_revision = '6ad2d6b4be3c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass    


def downgrade():
    op.drop_column('posts', 'content')
    pass
