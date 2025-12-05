"""Rename enrolled_date to enrollment_date

Revision ID: a124258550b8
Revises: 791279dd0760
Create Date: 2025-12-05 08:30:26.058174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a124258550b8'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'enrolled_date', new_column_name='enrollment_date')


def downgrade() -> None:
    op.alter_column('students', 'enrollment_date', new_column_name='enrolled_date')
