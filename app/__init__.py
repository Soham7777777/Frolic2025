from flask import Flask
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from flask_sqlalchemy import SQLAlchemy
import app.commands as commands
import os


class Base(MappedAsDataclass, DeclarativeBase):
  pass


db = SQLAlchemy(model_class=Base)


def make_app() -> Flask:
    application = Flask(__name__, instance_relative_config=True)
    application.cli.add_command(commands.test)

    application.config.from_object(f'instance.{os.getenv('PROFILE', 'Development')}')

    from app.models import User, Coordinator, Organizer, BranchAdmin, Participant, Team, TeamWiseParticipants, Event, EventThumbnail, UserWiseProfilePicture # type: ignore
    db.init_app(application)
    with application.app_context():
      db.create_all()

    from .blueprints import admin
    application.register_blueprint(admin.bp)

    return application