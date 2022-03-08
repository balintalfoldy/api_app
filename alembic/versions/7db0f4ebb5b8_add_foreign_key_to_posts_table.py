"""add foreign-key to posts table

Revision ID: 7db0f4ebb5b8
Revises: aa649178c795
Create Date: 2022-03-08 20:26:02.265744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7db0f4ebb5b8'
down_revision = 'aa649178c795'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts",
        referent_table="users", local_cols=["owner_id"], remote_cols=['id'],
            ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
