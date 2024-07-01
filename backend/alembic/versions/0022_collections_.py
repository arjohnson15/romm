"""empty message

Revision ID: 0022_collections
Revises: 0021_rom_user
Create Date: 2024-07-01 23:23:39.090219

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "0022_collections"
down_revision = "0021_rom_user"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "collections",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=400), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("logo_path", sa.String(length=1000), nullable=True),
        sa.Column("roms", sa.JSON(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("is_public", sa.Boolean(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("rom_user", schema=None) as batch_op:
        batch_op.alter_column(
            "is_main_sibling",
            existing_type=mysql.TINYINT(display_width=1),
            nullable=True,
        )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("rom_user", schema=None) as batch_op:
        batch_op.alter_column(
            "is_main_sibling",
            existing_type=mysql.TINYINT(display_width=1),
            nullable=False,
        )

    op.drop_table("collections")
    # ### end Alembic commands ###
