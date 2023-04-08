from .base import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean

class Projects(Base):
    __tablename__ = 'projects'
    project_id = Column(Integer, primary_key=True)
    project_name = Column(String(50), nullable=False)
    project_description = Column(String(100), nullable=False)
    UCRA_id = Column(String(50), ForeignKey('UCRA.UCRA_id'))
    model_id = Column(String(50), ForeignKey('model.model_id'))
    status_id = Column(Integer, ForeignKey('project_status.status_id'))


class ProjectOfferCodes(Base):
    __tablename__ = 'project_offer_codes'
    project_id = Column(Integer, ForeignKey('projects.project_id'), primary_key=True)
    offer_code = Column(String(50), primary_key=True)


class ProjectChannels(Base):
    __tablename__ = 'project_channels'
    project_id = Column(Integer, ForeignKey('projects.project_id'), primary_key=True)
    channel_id = Column(Integer, ForeignKey('channels.channel_id'), primary_key=True)
    offer_code = Column(String(50), ForeignKey('offer_codes.offer_code'), primary_key=True) 


class ProjectTasks(Base):
    __tablename__ = 'tasks'
    task_id = Column(Integer, primary_key=True)
    task_name = Column(String(100), nullable=False)
    task_description = Column(String(100), nullable=False)
    task_category_id = Column(Integer, ForeignKey('task_categories.task_category_id'))
    task_flow_id = Column(Integer, ForeignKey('task_flow.task_flow_id'))
    task_status_id = Column(Integer, ForeignKey('task_status.task_status_id'))
    task_due_date = Column(DateTime)
    task_completed_date = Column(DateTime)
    # these are used to join back to the project_channels table
    project_id = Column(Integer, ForeignKey('project_channels.project_id'))
    offer_code = Column(String(50), ForeignKey('project_channels.offer_code'))
    channel_id = Column(Integer, ForeignKey('project_channels.channel_id'))
    

class ProjectStatus(Base):
    __tablename__ = 'project_status'
    status_id = Column(Integer, primary_key=True, autoincrement=True)
    status_name = Column(String(50), nullable=False)
    status_description = Column(String(100), nullable=False)


class TaskNotes(Base):
    __tablename__ = 'task_notes'
    task_note_id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(Integer, ForeignKey('tasks.task_id'))
    task_note = Column(String(100), nullable=False)
    

class TaskCategories(Base):
    __tablename__ = 'task_categories'
    task_category_id = Column(Integer, primary_key=True, autoincrement=True)
    task_category_name = Column(String(50), nullable=False)
    task_category_description = Column(String(100), nullable=False)


class TaskFlow(Base):
    __tablename__ = 'task_flow'
    task_flow_id = Column(Integer, primary_key=True, autoincrement=True)
    task_flow_name = Column(String(50), nullable=False)
    task_flow_description = Column(String(100), nullable=False)


class TaskStatus(Base):
    __tablename__ = 'task_status'
    task_status_id = Column(Integer, primary_key=True, autoincrement=True)
    task_status_name = Column(String(50), nullable=False)
    task_status_description = Column(String(100), nullable=False)


class Channels(Base):
    __tablename__ = 'channels'
    channel_id = Column(Integer, primary_key=True, autoincrement=True)
    channel_level_1 = Column(String(50), nullable=False)
    channel_level_2 = Column(String(50), nullable=False)
    channel_level_3 = Column(String(50), nullable=False)
    channel_description = Column(String(100), nullable=False)


class OfferCodes(Base):
    __tablename__ = 'offer_codes'
    offer_code = Column(String(50), primary_key=True)
    offer_code_name = Column(String(50), nullable=False)
    offer_code_description = Column(String(100), nullable=False)
    campaign_id = Column(Integer, ForeignKey('campaigns.campaign_id'))


class Campaigns(Base):
    __tablename__ = 'campaigns'
    campaign_id = Column(Integer, primary_key=True, autoincrement=True)
    campaign_name = Column(String(50), nullable=False)
    campaign_description = Column(String(100), nullable=False)
    LOB_id = Column(Integer, ForeignKey('LOB.LOB_id'))


class LOB(Base):
    __tablename__ = 'LOB'
    LOB_id = Column(Integer, primary_key=True, autoincrement=True)
    LOB_name = Column(String(50), nullable=False)
    LOB_description = Column(String(100), nullable=False)


class UCRA(Base):
    __tablename__ = 'UCRA'
    UCRA_id = Column(Integer, primary_key=True, autoincrement=True)
    UCRA_name = Column(String(50), nullable=False)
    UCRA_description = Column(String(100), nullable=False)


class Model(Base):
    __tablename__ = 'model'
    model_id = Column(Integer, primary_key=True, autoincrement=True)
    model_name = Column(String(50), nullable=False)
    model_description = Column(String(100), nullable=False)
    model_type = Column(String(50), nullable=False)


class Log(Base):
    __tablename__ = 'log'
    log_id = Column(Integer, primary_key=True, autoincrement=True)
    log_date = Column(DateTime, nullable=False)
    log_message = Column(String(100), nullable=False)
    log_type = Column(String(50), nullable=False)
    table_name = Column(String(50), nullable=False)
