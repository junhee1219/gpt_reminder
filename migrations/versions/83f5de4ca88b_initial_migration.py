"""Initial migration.

Revision ID: 83f5de4ca88b
Revises: 
Create Date: 2024-10-20 22:01:48.647773

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '83f5de4ca88b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_completed', sa.Boolean(), nullable=True))
        batch_op.alter_column('deadline',
               existing_type=mysql.VARCHAR(length=19),
               nullable=True)
        batch_op.drop_constraint('todo_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(length=255),
               type_=sa.String(length=150),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=150),
               type_=mysql.VARCHAR(length=255),
               existing_nullable=False)

    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('todo_ibfk_1', 'user', ['user_id'], ['id'], ondelete='CASCADE')
        batch_op.alter_column('deadline',
               existing_type=mysql.VARCHAR(length=19),
               nullable=False)
        batch_op.drop_column('is_completed')

    # ### end Alembic commands ###
