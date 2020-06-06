"""empty message

Revision ID: 2d3891ee346f
Revises: b0159e473c2f
Create Date: 2020-06-06 14:55:29.690334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d3891ee346f'
down_revision = 'b0159e473c2f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('roles_usuarios',
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.Column('rol_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['rol_id'], ['Roles.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['Usuarios.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roles_usuarios')
    op.drop_table('Roles')
    # ### end Alembic commands ###
