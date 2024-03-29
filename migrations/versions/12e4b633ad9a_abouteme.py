"""abouteme

Revision ID: 12e4b633ad9a
Revises: 74fa4ac61b57
Create Date: 2023-03-10 21:14:33.288554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12e4b633ad9a'
down_revision = '74fa4ac61b57'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('candidate', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(length=500), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('candidate', schema=None) as batch_op:
        batch_op.drop_column('about_me')

    # ### end Alembic commands ###
