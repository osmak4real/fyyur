"""empty message

Revision ID: 117c5e840fba
Revises: 035d77620f7c
Create Date: 2022-06-12 06:39:38.200807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '117c5e840fba'
down_revision = '035d77620f7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('shows')
    op.add_column('artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.alter_column('artist', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('artist', 'city',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.drop_column('artist', 'looking_venue')
    op.add_column('venue', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    op.drop_column('venue', 'looking_talent')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('looking_talent', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('venue', 'seeking_talent')
    op.add_column('artist', sa.Column('looking_venue', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.alter_column('artist', 'city',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('artist', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('artist', 'seeking_venue')
    op.create_table('shows',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('start_time', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], name='shows_artist_id_fkey'),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], name='shows_venue_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='shows_pkey')
    )
    op.drop_table('show')
    # ### end Alembic commands ###
