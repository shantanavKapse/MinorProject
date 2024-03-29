"""Technical Answer

Revision ID: e9862c5bf58a
Revises: 12e4b633ad9a
Create Date: 2023-03-16 22:26:45.913915

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9862c5bf58a'
down_revision = '12e4b633ad9a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('technical_answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('candidate_username', sa.String(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('answer', sa.String(length=2000), nullable=False),
    sa.Column('is_correct', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['candidate_username'], ['candidate.username'], ),
    sa.ForeignKeyConstraint(['question_id'], ['technical_question.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('technical_answer')
    # ### end Alembic commands ###
