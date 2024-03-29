"""Technicial Questions

Revision ID: 54523e72916d
Revises: 3e8a1ba55e27
Create Date: 2023-03-06 18:59:00.385810

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54523e72916d'
down_revision = '3e8a1ba55e27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mcq_option')
    with op.batch_alter_table('technicial_question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('option1', sa.String(length=2000), nullable=False))
        batch_op.add_column(sa.Column('option2', sa.String(length=2000), nullable=False))
        batch_op.add_column(sa.Column('option3', sa.String(length=2000), nullable=False))
        batch_op.add_column(sa.Column('correctoption', sa.String(length=2000), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('technicial_question', schema=None) as batch_op:
        batch_op.drop_column('correctoption')
        batch_op.drop_column('option3')
        batch_op.drop_column('option2')
        batch_op.drop_column('option1')

    op.create_table('mcq_option',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('question_id', sa.INTEGER(), nullable=False),
    sa.Column('text', sa.VARCHAR(length=2000), nullable=False),
    sa.Column('is_correct', sa.BOOLEAN(), nullable=False),
    sa.Column('is_image', sa.BOOLEAN(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['technicial_question.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
