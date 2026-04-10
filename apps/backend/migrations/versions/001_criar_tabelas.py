"""Criar tabelas characters, dragons, houses e swords

Revision ID: 001
Revises: 
Create Date: 2026-04-10
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

revision: str = '001'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'characters',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('description', sa.String),
    )

    op.create_table(
        'dragons',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('description', sa.String),
    )

    op.create_table(
        'houses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('description', sa.String),
    )

    op.create_table(
        'swords',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('description', sa.String),
    )


def downgrade() -> None:
    op.drop_table('characters')
    op.drop_table('dragons')
    op.drop_table('houses')
    op.drop_table('swords')