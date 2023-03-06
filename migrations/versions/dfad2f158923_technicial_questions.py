"""Technicial Questions

Revision ID: dfad2f158923
Revises: e3b158a2ceab
Create Date: 2023-03-06 22:48:22.130869

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfad2f158923'
down_revision = 'e3b158a2ceab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('technicial_question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('company_username', sa.String(length=100), nullable=True))
        batch_op.drop_column('company_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('technicial_question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('company_name', sa.VARCHAR(length=100), nullable=True))
        batch_op.drop_column('company_username')

    # ### end Alembic commands ###