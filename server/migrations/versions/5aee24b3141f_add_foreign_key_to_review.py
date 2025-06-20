"""add foreign key to Review

Revision ID: 5aee24b3141f
Revises: 954aeec15153
Create Date: 2025-06-11 00:23:17.681424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5aee24b3141f'
down_revision = '954aeec15153'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews') as batch_op:batch_op.create_foreign_key(batch_op.f('fk_reviews_employee_id_employees'),'employees',['employee_id'],['id']
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews') as batch_op:batch_op.drop_constraint(batch_op.f('fk_reviews_employee_id_employees'),
    type_='foreignkey')
    batch_op.drop_column('employee_id')

    # ### end Alembic commands ###
