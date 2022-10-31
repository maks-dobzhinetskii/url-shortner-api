"""test

Revision ID: d268d85d3a92
Revises:
Create Date: 2022-10-26 13:38:53.975875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd268d85d3a92'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'urlshortener',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_ip_address', sa.String(), nullable=True),
        sa.Column('longurl', sa.String(), nullable=True),
        sa.Column('shorturl', sa.String(length=8), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(op.f('ix_urlshortener_id'), 'urlshortener', ['id'], unique=False)
    op.create_index(op.f('ix_urlshortener_longurl'), 'urlshortener', ['longurl'], unique=False)
    op.create_index(op.f('ix_urlshortener_shorturl'), 'urlshortener', ['shorturl'], unique=False)
    op.create_index(op.f('ix_urlshortener_user_ip_address'), 'urlshortener', ['user_ip_address'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_urlshortener_user_ip_address'), table_name='urlshortener')
    op.drop_index(op.f('ix_urlshortener_shorturl'), table_name='urlshortener')
    op.drop_index(op.f('ix_urlshortener_longurl'), table_name='urlshortener')
    op.drop_index(op.f('ix_urlshortener_id'), table_name='urlshortener')
    op.drop_table('urlshortener')
    # ### end Alembic commands ###